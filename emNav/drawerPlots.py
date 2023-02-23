from matplotlib import pyplot as plt


def draw_plots(gps_x_points, gps_y_points, z_points, no_gps_x_points, no_gps_y_points,
               no_gps_mean_x_points, no_gps_mean_y_points, no_gps_trim_x_points, no_gps_trim_y_points):

    plt.ion()
    global fg
    fg = plt.figure()
    ax = fg.gca()
    h = None
    fg.show()

    global fg2
    fg2 = plt.figure()
    ax2 = fg2.add_subplot(projection='3d')
    ax2.set_xlim(50, 52)
    ax2.set_ylim(85, 86)
    ax2.set_zlim(0, 450)
    ax2.set_xlabel('$X$')
    ax2.set_ylabel('$Y$')
    ax2.set_zlabel('$Z$')
    h2 = ax2.scatter(gps_x_points, gps_y_points, z_points, color='blue')
    h3 = ax2.scatter(no_gps_x_points, no_gps_y_points, z_points, color='red')
    h4 = ax2.scatter(no_gps_mean_x_points, no_gps_mean_y_points, z_points, color='green')
    h5 = ax2.scatter(no_gps_trim_x_points, no_gps_trim_y_points, z_points, color='grey')
    fg2.show()
    return h, h2, h3, h4, h5, ax, plt


def update_plots(h, h2, h3, h4, h5, first_step, ax, compared_images,
                 gps_x_points, gps_y_points, z_points, no_gps_x_points, no_gps_y_points,
                 no_gps_mean_x_points, no_gps_mean_y_points, no_gps_trim_x_points, no_gps_trim_y_points):
    h2._offsets3d = (gps_x_points, gps_y_points, z_points)
    h3._offsets3d = (no_gps_x_points, no_gps_y_points, z_points)
    h4._offsets3d = (no_gps_mean_x_points, no_gps_mean_y_points, z_points)
    h5._offsets3d = (no_gps_trim_x_points, no_gps_trim_y_points, z_points)
    if first_step:
        h = ax.imshow(compared_images)
        first_step = False
    else:
        h.set_data(compared_images)
    plt.draw(), plt.pause(0.01)
    return h, h2, h3, h4, h5, first_step
