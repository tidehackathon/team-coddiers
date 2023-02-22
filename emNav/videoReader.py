import time
from math import pi, radians, cos, sin
import cv2
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
    ax2.set_xlim(35.08, 35.12)
    ax2.set_ylim(48.55, 48.56)
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
            if count < 1000:
                x_points.append(get_lon(vehicle))
                y_points.append(get_lat(vehicle))
                z_points.append(get_alt(vehicle))
            else:
                theta_rad = pi / 2 - radians(get_heading(vehicle))
                current_x = current_x + dist_difference * cos(theta_rad)
                current_y = current_y + dist_difference * sin(theta_rad)
                x_points.append(get_lon(vehicle))
                y_points.append(get_lat(vehicle))
                z_points.append(get_alt(vehicle))

            h2._offsets3d = (x_points, y_points, z_points)
            if first_step:
                h = ax.imshow(compared_images)
                first_step = False
            else:
                h.set_data(compared_images)
        plt.draw(), plt.pause(1e-3)
        last_image = new_img
        key_points_1 = key_points_2
        descriptors_1 = descriptors_2
        best_key_points_1 = best_key_points_2
        count += 1
    vic_cap.release()
    cv2.destroyAllWindows()
