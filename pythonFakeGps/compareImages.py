import cv2 as cv
import concurrent.futures

import numpy as np

accuracy = 100
flann_index_kdtree = 1
index_params = dict(algorithm=flann_index_kdtree, trees=5)
search_params = dict(checks=50)
sift = cv.SIFT_create()
flann = cv.FlannBasedMatcher(index_params, search_params)


def generate_data_img(img):
    return sift.detectAndCompute(img, None)


def get_distance(item):
    return item.distance


def compare_images(first_img, second_img, mono):
    if mono:
        first_img = cv.cvtColor(first_img, cv.COLOR_BGR2GRAY)
        second_img = cv.cvtColor(second_img, cv.COLOR_BGR2GRAY)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        t1 = executor.submit(generate_data_img, first_img)
        t2 = executor.submit(generate_data_img, second_img)

        key_points_1, descriptors_1 = t1.result()
        key_points_2, descriptors_2 = t2.result()

    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)
    good_matches = sorted(good_matches, key=lambda x: x.distance)

    img_matches = np.empty((max(first_img.shape[0], second_img.shape[0]), first_img.shape[1] + second_img.shape[1], 3),
                           dtype=np.uint8)
    compared_images = cv.drawMatches(first_img, key_points_1, second_img, key_points_2, good_matches[:1], img_matches,
                                     flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    best_key_points_1 = [key_points_1[m.queryIdx] for m in good_matches][:accuracy]
    best_key_points_2 = [key_points_2[m.trainIdx] for m in good_matches][:accuracy]

    x_difference = 0
    y_difference = 0
    if len(best_key_points_1) > accuracy and len(best_key_points_2) > accuracy:
        for i in range(accuracy):
            x_difference += best_key_points_1[i].pt[0] - best_key_points_2[i].pt[0]
            y_difference += best_key_points_2[i].pt[1] - best_key_points_1[i].pt[1]
    else:
        if len(best_key_points_1) > len(best_key_points_2):
            for i in range(len(best_key_points_2)):
                x_difference += best_key_points_1[i].pt[0] - best_key_points_2[i].pt[0]
                y_difference += best_key_points_2[i].pt[1] - best_key_points_1[i].pt[1]
        else:
            for i in range(len(best_key_points_1)):
                x_difference += best_key_points_1[i].pt[0] - best_key_points_2[i].pt[0]
                y_difference += best_key_points_2[i].pt[1] - best_key_points_1[i].pt[1]

    x_difference = x_difference / (accuracy * 100)
    y_difference = y_difference / (accuracy * 100)

    return compared_images, x_difference, y_difference
