import dronekit
import cv2
from emNav.drawerPlots import draw_plots, update_plots
from emNav.params import video_src
from emNav.simController import single_step_controller
from threading import Thread
from time import sleep

vehicle = dronekit.connect('tcp:51.145.133.68:5763', baud=115200)
vid_cap = cv2.VideoCapture(video_src)
fps = vid_cap.get(cv2.CAP_PROP_FPS)

first_step = True
count = 0
factor = 0
factor_mean = 0
factor_trim = 0

current_x = 0
current_y = 0
current_x_mean = 0
current_y_mean = 0
current_x_trim = 0
current_y_trim = 0

last_lat = None
last_lon = None
dist_lon_lat_tab = []
dist_x_y_tab = []

last_image = None
key_points_1 = None
descriptors_1 = None
best_key_points_1 = None

gps_x_points = []
gps_y_points = []
z_points = []
no_gps_x_points = []
no_gps_y_points = []
no_gps_mean_x_points = []
no_gps_mean_y_points = []
no_gps_trim_x_points = []
no_gps_trim_y_points = []

drone_height = 0
compas_angle = 0

compared_images = None


def single_step_calculation(frame):
    global factor, factor_mean, factor_trim, compared_images, gps_x_points, gps_y_points, z_points, no_gps_x_points, \
        no_gps_y_points, no_gps_mean_x_points, no_gps_mean_y_points, no_gps_trim_x_points, no_gps_trim_y_points, \
        last_lat, last_lon, current_x_mean, current_y_mean, current_x_trim, current_y_trim, best_key_points_1, count, \
        current_x, current_y, descriptors_1, dist_lon_lat_tab, dist_x_y_tab, key_points_1, last_image, vehicle

    center_width = int(frame.shape[1] / 2)
    center_height = int(frame.shape[0] / 2)
    center_point = (center_width, center_height)

    factor, factor_mean, factor_trim, new_img, key_points_2, descriptors_2, best_key_points_2, compared_images, \
    gps_x_points, gps_y_points, z_points, no_gps_x_points, no_gps_y_points, no_gps_mean_x_points, \
    no_gps_mean_y_points, no_gps_trim_x_points, no_gps_trim_y_points, last_lat, last_lon, current_x, current_y, \
    current_x_mean, current_y_mean, current_x_trim, current_y_trim = \
        single_step_controller(vehicle, count, frame, last_image, factor, factor_mean, factor_trim,
                               center_point, key_points_1, descriptors_1, best_key_points_1, z_points,
                               last_lat, last_lon, gps_x_points, gps_y_points, no_gps_x_points,
                               no_gps_y_points, no_gps_mean_x_points, no_gps_mean_y_points,
                               no_gps_trim_x_points, no_gps_trim_y_points, dist_lon_lat_tab, dist_x_y_tab,
                               current_x, current_y, current_x_mean,
                               current_y_mean, current_x_trim, current_y_trim)

    last_image = new_img
    key_points_1 = key_points_2
    descriptors_1 = descriptors_2
    best_key_points_1 = best_key_points_2
    compared_images = compared_images


def get_frame():
    success = True
    global count
    count = 0
    while success:
        success, frame = vid_cap.read()
        count += 1
        print("time stamp current frame:", count / fps)
        if count % fps / 2 == 0:
            yield frame

    vid_cap.release()
    cv2.destroyAllWindows()


def handle_message(self, name, message):
    global best_key_points_1, descriptors_1, key_points_1, last_image, compared_images
    print(message)
    if str(message).find('Reached waypoint #3') != -1:
        while True:
            frame = next(gen)
            t1 = Thread(target=single_step_calculation, args=[frame])
            t1.start()
            sleep(0.5)


gen = get_frame()
vehicle.add_message_listener('STATUSTEXT', handle_message)
h, h2, h3, h4, h5, ax, plt = draw_plots(gps_x_points, gps_y_points, z_points, no_gps_x_points, no_gps_y_points,
                                        no_gps_mean_x_points, no_gps_mean_y_points, no_gps_trim_x_points,
                                        no_gps_trim_y_points)

while True:
    if compared_images is not None:
        h, h2, h3, h4, h5, first_step = update_plots(h, h2, h3, h4, h5, first_step, ax, compared_images,
                                                     gps_x_points, gps_y_points, z_points,
                                                     no_gps_x_points, no_gps_y_points,
                                                     no_gps_mean_x_points, no_gps_mean_y_points,
                                                     no_gps_trim_x_points, no_gps_trim_y_points)
