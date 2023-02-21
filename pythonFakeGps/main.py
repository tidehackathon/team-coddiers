import cv2
import time

from compareImages import compare_images
import matplotlib.pyplot as plt

vic_cap = cv2.VideoCapture('rec\sample2a-gimbal.MOV')
last_image = None
compared_images = None
first_step = True
count = 0
current_x = 0
current_y = 0
current_z = 0
x_points = []
y_points = []
z_points = []

plt.ion()
fg2 = plt.figure()
ax2 = fg2.add_subplot(projection='3d')
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)
ax2.set_zlim(0, 10)
ax2.set_xlabel('$X$')
ax2.set_ylabel('$Y$')
ax2.set_zlabel('$Z$')
h2 = ax2.scatter(x_points, y_points, z_points)
fg2.show()

success, image = vic_cap.read()
while success:
    start = time.time()
    success, image = vic_cap.read()
    if last_image is not None:
        x_difference, y_difference = compare_images(last_image, image, True)
        current_x = current_x + x_difference
        current_y = current_y + y_difference
        x_points.append(current_x)
        y_points.append(current_y)
        z_points.append(current_z)
        h2._offsets3d = (x_points, y_points, z_points)
        plt.draw(), plt.pause(0.05)
    last_image = image
    count += 1
    print(time.time() - start)
