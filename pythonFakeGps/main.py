import cv2
import numpy as np

from compareImages import compare_images
import matplotlib.pyplot as plt

vic_cap = cv2.VideoCapture('rec\sample2a-gimbal.MOV')
last_image = None
compared_images = None
first_step = True
count = 0
x_points = []
y_points = []
z_points = []

plt.ion()
fg = plt.figure()
ax = fg.gca()
h = None
fg.show()

fg2 = plt.figure()
ax2 = fg2.add_subplot(projection='3d')
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 100)
ax2.set_zlim(0, 100)
h2 = ax2.scatter(x_points, y_points, z_points)
fg2.show()

success, image = vic_cap.read()
while success:
    success, image = vic_cap.read()
    print('[', count, '] Read a new frame: ', success)
    if last_image is not None:
        compared_images = compare_images(last_image, image, True)
        x_points.append(count)
        y_points.append(count)
        z_points.append(count)
        h2._offsets3d = (x_points, y_points, z_points)
        if first_step:
            h = ax.imshow(compared_images)
            first_step = False
        else:
            h.set_data(compared_images)
            # plt.draw(), plt.pause(1e-3)
            plt.draw(), plt.pause(1)
    last_image = image
    count += 1
