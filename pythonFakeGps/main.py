import cv2

from compareImages import compare_images
import matplotlib.pyplot as plt

from pythonFakeGps.rescaleFrame import rescale_frame

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
fg = plt.figure()
ax = fg.gca()
h = None
fg.show()

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
center_width = int(image.shape[1] / 2)
center_height = int(image.shape[0] / 2)
center_point = (center_width, center_height)
while success:
    success, image = vic_cap.read()
    image = rescale_frame(image, percent=50)
    if last_image is not None:
        compared_images, dist_difference = compare_images(last_image, image, True, center_point)
        current_x = current_x + dist_difference
        x_points.append(current_x)
        y_points.append(current_y)
        z_points.append(current_z)
        h2._offsets3d = (x_points, y_points, z_points)
        if first_step:
            h = ax.imshow(compared_images)
            first_step = False
        else:
            h.set_data(compared_images)
        plt.draw(), plt.pause(0.05)
    last_image = image
    count += 1

vic_cap.release()
cv2.destroyAllWindows()
