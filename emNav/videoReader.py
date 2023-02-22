import math
import time
from math import pi, radians, cos, sin
import cv2
import numpy as np

from compareImages import compare_images
import matplotlib.pyplot as plt

from emNav.vehicleData import get_heading, get_alt, get_lat, get_lon
from rescaleFrame import rescale_frame
from params import video_src, rescale_frame_percent


def video_reader(drone_height, vehicle):
    vic_cap = cv2.VideoCapture(video_src)
    first_step = True
    count = 0
    current_x = 0
    current_y = 0
    x_points = []
    y_points = []
    z_points = []

    last_lat = None
    last_lon = None
    dist_lon_lat_tab = []
    dist_x_y_tab = []
    factor = 0

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
    h2 = ax2.scatter(x_points, y_points, z_points)
    fg2.show()

    success, image = vic_cap.read()
    center_width = int(image.shape[1] / 2)
    center_height = int(image.shape[0] / 2)
    center_point = (center_width, center_height)
    while success:
        success, image = vic_cap.read()
        image = rescale_frame(image, percent=rescale_frame_percent)
        compared_images, dist_difference, new_img, key_points_2, descriptors_2, best_key_points_2 = \
            compare_images(image, True, center_point, last_image, key_points_1, descriptors_1, best_key_points_1)
        if compared_images is not None and dist_difference is not None and best_key_points_2 is not None:
            if count < 100:
                print('Step: ', count)
                current_x = get_lon(vehicle) % 10 * 10
                current_y = get_lat(vehicle) % 10 * 10
                current_z = get_alt(vehicle)
                print('GPS: ', current_x, current_y, current_z)
                x_points.append(current_x)
                y_points.append(current_y)
                z_points.append(current_z)
                if last_lat is not None and last_lon is not None:
                    dist_lon_lat_tab.append(math.dist((last_lon, last_lat), (current_x, current_y)))
                    dist_x_y_tab.append(dist_difference)
                last_lon = current_x
                last_lat = current_y

            else:
                if count == 100:
                    factor = np.mean(np.array(dist_lon_lat_tab)) / np.mean(np.array(dist_x_y_tab))
                    print(dist_lon_lat_tab)
                    print(dist_x_y_tab[3:])
                    print(np.mean(np.array(dist_lon_lat_tab)))
                    print(np.mean(np.array(dist_x_y_tab[3:])))
                    print('Factor: ', factor)
                print('Step: ', count, ' - NO GPS!')
                dist_difference = factor
                theta_rad = pi / 2 - radians(get_heading(vehicle))
                current_x = current_x + dist_difference * cos(theta_rad)
                current_y = current_y + dist_difference * sin(theta_rad)
                current_z = get_alt(vehicle)
                print('Heading: ', get_heading(vehicle))
                print('GPS: ', get_lon(vehicle) % 10 * 10, get_lat(vehicle) % 10 * 10, get_alt(vehicle))
                print('NO GPS: ', current_x, current_y, current_z)
                print('DIFF: ', get_lon(vehicle) % 10 * 10 - current_x, get_lat(vehicle) % 10 * 10 - current_y)
                x_points.append(current_x)
                y_points.append(current_y)
                z_points.append(current_z)

            h2._offsets3d = (x_points, y_points, z_points)
            if first_step:
                h = ax.imshow(compared_images)
                first_step = False
            else:
                h.set_data(compared_images)
        plt.draw(), plt.pause(0.5)
        last_image = new_img
        key_points_1 = key_points_2
        descriptors_1 = descriptors_2
        best_key_points_1 = best_key_points_2
        count += 1
    vic_cap.release()
    cv2.destroyAllWindows()
