import cv2 as cv
import numpy as np


def get_distance(item):
    return item.distance


def compare_images(first_img, second_img, mono):
    if mono:
        first_img = cv.cvtColor(first_img, cv.COLOR_BGR2GRAY)
        second_img = cv.cvtColor(second_img, cv.COLOR_BGR2GRAY)

    sift = cv.SIFT_create()

    key_points_1, descriptors_1 = sift.detectAndCompute(first_img, None)
    key_points_2, descriptors_2 = sift.detectAndCompute(second_img, None)

    flann_index_kdtree = 1
    index_params = dict(algorithm=flann_index_kdtree, trees=5)
    search_params = dict(checks=100)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    img_matches = np.empty((max(first_img.shape[0], second_img.shape[0]), first_img.shape[1] + second_img.shape[1], 3),
                           dtype=np.uint8)
    compared_images = cv.drawMatches(first_img, key_points_1, second_img, key_points_2, good_matches, img_matches,
                                     flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    return compared_images
