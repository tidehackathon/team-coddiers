import math
import numpy as np
from emNav.compareImages import compare_images
from emNav.params import rescale_frame_percent
from emNav.rescaleFrame import rescale_frame
from scipy import stats


def single_step_controller(vehicle_lon, vehicle_lat, vehicle_alt, vehicle_heading, count, image, last_image, factor, 
                           factor_mean, factor_trim, center_point,
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
            current_x = vehicle_lon % 10 * 10
            current_y = vehicle_lat % 10 * 10
            current_x_mean = vehicle_lon % 10 * 10
            current_y_mean = vehicle_lat % 10 * 10
            current_x_trim = vehicle_lon % 10 * 10
            current_y_trim = vehicle_lat % 10 * 10
            current_z = vehicle_alt
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
            theta_rad = math.pi / 2 - math.radians(vehicle_heading)
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

            current_z = vehicle_alt
            print('Heading: ', vehicle_heading)
            print('GPS: ', vehicle_lon % 10 * 10, vehicle_lat % 10 * 10, vehicle_alt)
            print('NO GPS: ', current_x, current_y, current_z)
            print('NO GPS mean: ', current_x_mean, current_y_mean, current_z)
            print('NO GPS trim: ', current_x_trim, current_y_trim, current_z)
            print('DIFF: ', vehicle_lon % 10 * 10 - current_x, vehicle_lat % 10 * 10 - current_y)
            print('DIFF mean: ', vehicle_lon % 10 * 10 - current_x_mean,
                  vehicle_lat % 10 * 10 - current_y_mean)
            print('DIFF trim: ', vehicle_lon % 10 * 10 - current_x_trim,
                  vehicle_lat % 10 * 10 - current_y_trim)
            no_gps_x_points.append(current_x)
            no_gps_y_points.append(current_y)
            no_gps_mean_x_points.append(current_x_mean)
            no_gps_mean_y_points.append(current_y_mean)
            no_gps_trim_x_points.append(current_x_trim)
            no_gps_trim_y_points.append(current_y_trim)
            z_points.append(current_z)
            gps_x_points.append(vehicle_lon % 10 * 10)
            gps_y_points.append(vehicle_lat % 10 * 10)

    return factor, factor_mean, factor_trim, new_img, key_points_2, descriptors_2, best_key_points_2, compared_images, \
           gps_x_points, gps_y_points, z_points, no_gps_x_points, no_gps_y_points, no_gps_mean_x_points, \
           no_gps_mean_y_points, no_gps_trim_x_points, no_gps_trim_y_points, last_lat, last_lon, current_x, current_y, \
           current_x_mean, current_y_mean, current_x_trim, current_y_trim
