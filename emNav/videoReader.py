import math
import time
from math import pi, radians, cos, sin
import cv2
import numpy as np
from scipy import stats

from compareImages import compare_images
import matplotlib.pyplot as plt

from emNav.latLngToMeters import lat_lon_to_meters
from vehicleData import get_heading, get_alt, get_lat, get_lon
from rescaleFrame import rescale_frame
from params import video_src, rescale_frame_percent

check = False
count = 0


def handle_message(self, name, message):
    global check, count
    print(message)
    if str(message).find('Reached waypoint #3'):
        check = True
        count = 0
        return True


def video_reader(vehicle):
    global count
    vic_cap = cv2.VideoCapture(video_src)
    fps = vic_cap.get(cv2.CAP_PROP_FPS)
    vehicle.add_message_listener('STATUSTEXT', handle_message)

    while not check:
        pass

    first_step = True
    current_x = 0
    current_y = 0
    current_x_mean = 0
    current_y_mean = 0
    current_x_trim = 0
    current_y_trim = 0
    gps_x_points = []
    gps_y_points = []
    z_points = []
    x_points = []
    y_points = []
    x_points_mean = []
    y_points_mean = []
    x_points_trim = []
    y_points_trim = []

    last_lat = None
    last_lon = None
    dist_lon_lat_tab = []
    dist_x_y_tab = []
    factor = 0
    factor_mean = 0
    factor_trim = 0

    last_image = None
    key_points_1 = None
    descriptors_1 = None
    best_key_points_1 = None

    plt.ion()
    fg = plt.figure()
    ax = fg.gca()
    h = None
    fg.show()

    fg2 = plt.figure()
    ax2 = fg2.add_subplot(projection='3d')
    ax2.set_xlim(50, 52)
    ax2.set_ylim(85, 86)
    ax2.set_zlim(0, 450)
    ax2.set_xlabel('$X$')
    ax2.set_ylabel('$Y$')
    ax2.set_zlabel('$Z$')
    h2 = ax2.scatter(gps_x_points, gps_y_points, z_points, color='blue')
    h3 = ax2.scatter(x_points, y_points, z_points, color='red')
    h4 = ax2.scatter(x_points_mean, y_points_mean, z_points, color='green')
    h5 = ax2.scatter(x_points_trim, y_points_trim, z_points, color='grey')
    fg2.show()

    success, image = vic_cap.read()
    center_width = int(image.shape[1] / 2)
    center_height = int(image.shape[0] / 2)
    center_point = (center_width, center_height)
    while success:
        success, image = vic_cap.read()
        if count % fps/2 == 0 and check:
            start = time.time()
            image = rescale_frame(image, percent=rescale_frame_percent)

            compared_images, dist_difference, new_img, key_points_2, descriptors_2, best_key_points_2 = \
                compare_images(image, True, center_point, last_image,
                               key_points_1, descriptors_1, best_key_points_1)
            if compared_images is not None and dist_difference is not None and best_key_points_2 is not None:
                if count < 6000:
                    print('Step: ', count)
                    current_x = get_lon(vehicle) % 10 * 10
                    current_y = get_lat(vehicle) % 10 * 10
                    current_x_mean = get_lon(vehicle) % 10 * 10
                    current_y_mean = get_lat(vehicle) % 10 * 10
                    current_x_trim = get_lon(vehicle) % 10 * 10
                    current_y_trim = get_lat(vehicle) % 10 * 10
                    current_z = get_alt(vehicle)
                    print('GPS: ', current_x, current_y, current_z)
                    gps_x_points.append(current_x)
                    gps_y_points.append(current_y)
                    x_points.append(current_x)
                    y_points.append(current_y)
                    x_points_mean.append(current_x)
                    y_points_mean.append(current_y)
                    x_points_trim.append(current_x)
                    y_points_trim.append(current_y)
                    z_points.append(current_z)
                    if last_lat is not None and last_lon is not None:
                        dist_lon_lat_tab.append(math.dist((last_lon, last_lat), (current_x, current_y)))
                        dist_x_y_tab.append(dist_difference)
                    last_lon = current_x
                    last_lat = current_y
                else:
                    if count == 6000:
                        factor = np.median(np.array(dist_lon_lat_tab)) / np.mean(np.array(dist_x_y_tab))
                        factor_mean = stats.trim_mean(np.array(dist_lon_lat_tab), 0.2) / \
                                      stats.trim_mean(np.array(dist_x_y_tab), 0.2)
                        factor_trim = stats.trim_mean(np.array(dist_lon_lat_tab), 0.2) / np.mean(np.array(dist_x_y_tab))
                        print(np.mean(np.array(dist_lon_lat_tab)))
                        print(np.mean(np.array(dist_x_y_tab[3:])))
                        print('Factor: ', factor)
                    print('Step: ', count, ' - NO GPS!')
                    theta_rad = pi / 2 - radians(get_heading(vehicle))
                    current_x = current_x + dist_difference * factor * cos(theta_rad)
                    current_y = current_y + dist_difference * factor * sin(theta_rad)
                    current_x_mean = current_x_mean + dist_difference * factor_mean * cos(theta_rad)
                    current_y_mean = current_y_mean + dist_difference * factor_mean * sin(theta_rad)
                    current_x_trim = current_x_trim + dist_difference * factor_trim * cos(theta_rad)
                    current_y_trim = current_y_trim + dist_difference * factor_trim * sin(theta_rad)
                    current_z = get_alt(vehicle)
                    print('Heading: ', get_heading(vehicle))
                    print('GPS: ', get_lon(vehicle) % 10, get_lat(vehicle) % 10, get_alt(vehicle))
                    print('NO GPS: ', current_x / 10, current_y / 10, current_z)
                    print('NO GPS mean: ', current_x_mean / 10, current_y_mean / 10, current_z)
                    print('NO GPS trim: ', current_x_trim / 10, current_y_trim / 10, current_z)
                    print('DIFF: ',
                          get_lon(vehicle) % 10 - current_x / 10, get_lat(vehicle) % 10 - current_y / 10)
                    print('DIFF in meters: ',
                          lat_lon_to_meters(get_lat(vehicle) % 10, get_lon(vehicle) % 10,
                                            current_y / 10, current_x / 10), ' meters')
                    print('DIFF mean: ',
                          get_lon(vehicle) % 10 - current_x_mean / 10, get_lat(vehicle) % 10 - current_y_mean / 10)
                    print('DIFF mean in meters',
                          lat_lon_to_meters(get_lat(vehicle) % 10, get_lon(vehicle) % 10,
                                            current_y_mean / 10, current_x_mean / 10), ' meters')
                    print('DIFF trim: ',
                          get_lon(vehicle) % 10 - current_x_trim / 10, get_lat(vehicle) % 10 - current_y_trim / 10)
                    print('DIFF trim in meters',
                          lat_lon_to_meters(get_lat(vehicle) % 10, get_lon(vehicle) % 10,
                                            current_y_trim / 10, current_x_trim / 10), ' meters')
                    x_points.append(current_x)
                    y_points.append(current_y)
                    x_points_mean.append(current_x_mean)
                    y_points_mean.append(current_y_mean)
                    x_points_trim.append(current_x_trim)
                    y_points_trim.append(current_y_trim)
                    z_points.append(current_z)
                    gps_x_points.append(get_lon(vehicle) % 10 * 10)
                    gps_y_points.append(get_lat(vehicle) % 10 * 10)

                h2._offsets3d = (gps_x_points, gps_y_points, z_points)
                h3._offsets3d = (x_points, y_points, z_points)
                h4._offsets3d = (x_points_mean, y_points_mean, z_points)
                h5._offsets3d = (x_points_trim, y_points_trim, z_points)
                if first_step:
                    h = ax.imshow(compared_images)
                    first_step = False
                else:
                    h.set_data(compared_images)
            plt.draw(), plt.pause(0.05)
            last_image = new_img
            key_points_1 = key_points_2
            descriptors_1 = descriptors_2
            best_key_points_1 = best_key_points_2
            while time.time() - start < 0.95:
                pass
        count += 1

    plt.show(block=True)
    vic_cap.release()
    cv2.destroyAllWindows()
