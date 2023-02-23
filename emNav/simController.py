import math
import numpy as np
from emNav.compareImages import compare_images
from emNav.params import rescale_frame_percent
from emNav.rescaleFrame import rescale_frame
from emNav.vehicleData import get_lon, get_lat, get_alt, get_heading
from scipy import stats


def single_step_controller(vehicle, count, image, last_image, factor, factor_mean, factor_trim, center_point,
                           key_points_1, descriptors_1, best_key_points_1, z_points, last_lat, last_lon,
                           gps_x_points, gps_y_points, no_gps_x_points, no_gps_y_points,
                           no_gps_mean_x_points, no_gps_mean_y_points, no_gps_trim_x_points, no_gps_trim_y_points,
                           dist_lon_lat_tab, dist_x_y_tab,
                           current_x, current_y, current_x_mean, current_y_mean, current_x_trim, current_y_trim):
    image = rescale_frame(image, percent=rescale_frame_percent)

    compared_images, dist_difference, new_img, key_points_2, descriptors_2, best_key_points_2 = \
        compare_images(image, True, center_point, last_image,
                       key_points_1, descriptors_1, best_key_points_1)
    if compared_images is not None and dist_difference is not None and best_key_points_2 is not None:
        if count < 1000:
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
            no_gps_x_points.append(current_x)
            no_gps_y_points.append(current_y)
            no_gps_mean_x_points.append(current_x)
            no_gps_mean_y_points.append(current_y)
            no_gps_trim_x_points.append(current_x)
            no_gps_trim_y_points.append(current_y)
            z_points.append(current_z)
            if last_lat is not None and last_lon is not None:
                dist_lon_lat_tab.append(math.dist((last_lon, last_lat), (current_x, current_y)))
                dist_x_y_tab.append(dist_difference)
            last_lon = current_x
            last_lat = current_y
        else:
            if count == 1000:
                factor = np.median(np.array(dist_lon_lat_tab)) / np.mean(np.array(dist_x_y_tab))
                factor_mean = np.mean(np.array(dist_lon_lat_tab)) / np.mean(np.array(dist_x_y_tab))
                factor_trim = stats.trim_mean(np.array(dist_lon_lat_tab), 0.1) / np.mean(np.array(dist_x_y_tab))
            print('Step: ', count, ' - NO GPS!')
            theta_rad = math.pi / 2 - math.radians(get_heading(vehicle))
            print('dist_difference', dist_difference)
            print('Factor: ', factor)
            print('Factor_mean: ', factor_mean)
            print('Factor_trim: ', factor_trim)
            dist_difference = dist_difference
            current_x = current_x + factor * dist_difference * math.cos(theta_rad)
            current_y = current_y + factor * dist_difference * math.sin(theta_rad)

            current_x_mean = current_x_mean + factor_mean * dist_difference * math.cos(theta_rad)
            current_y_mean = current_y_mean + factor_mean * dist_difference * math.sin(theta_rad)

            current_x_trim = current_x_trim + factor_trim * dist_difference * math.cos(theta_rad)
            current_y_trim = current_y_trim + factor_trim * dist_difference * math.sin(theta_rad)

            current_z = get_alt(vehicle)
            print('Heading: ', get_heading(vehicle))
            print('GPS: ', get_lon(vehicle) % 10 * 10, get_lat(vehicle) % 10 * 10, get_alt(vehicle))
            print('NO GPS: ', current_x, current_y, current_z)
            print('NO GPS mean: ', current_x_mean, current_y_mean, current_z)
            print('NO GPS trim: ', current_x_trim, current_y_trim, current_z)
            print('DIFF: ', get_lon(vehicle) % 10 * 10 - current_x, get_lat(vehicle) % 10 * 10 - current_y)
            print('DIFF mean: ', get_lon(vehicle) % 10 * 10 - current_x_mean,
                  get_lat(vehicle) % 10 * 10 - current_y_mean)
            print('DIFF trim: ', get_lon(vehicle) % 10 * 10 - current_x_trim,
                  get_lat(vehicle) % 10 * 10 - current_y_trim)
            no_gps_x_points.append(current_x)
            no_gps_y_points.append(current_y)
            no_gps_mean_x_points.append(current_x_mean)
            no_gps_mean_y_points.append(current_y_mean)
            no_gps_trim_x_points.append(current_x_trim)
            no_gps_trim_y_points.append(current_y_trim)
            z_points.append(current_z)
            gps_x_points.append(get_lon(vehicle) % 10 * 10)
            gps_y_points.append(get_lat(vehicle) % 10 * 10)

    return factor, factor_mean, factor_trim, new_img, key_points_2, descriptors_2, best_key_points_2, compared_images, \
           gps_x_points, gps_y_points, z_points, no_gps_x_points, no_gps_y_points, no_gps_mean_x_points, \
           no_gps_mean_y_points, no_gps_trim_x_points, no_gps_trim_y_points, last_lat, last_lon, current_x, current_y, \
           current_x_mean, current_y_mean, current_x_trim, current_y_trim
