import cv2
import numpy as np

from typing import Tuple


def img_prep(img: np.array, lower: Tuple[int, int, int] = (0, 0, 0), upper: Tuple[int, int, int] = (255, 255, 255),
             iterations: int = 1, blur_strength: int = 0):
    """
    Prepare image. Apply mask, blur and dilation.

    :param img: image to search objects and draw frame
    :param lower: lower bound of color to search for (HSV).
    :param upper: upper bound of color to search for (HSV).
    :param iterations: number of iterations to dilate image (increase to find smaller contours but accuracy decreases).
    :param blur_strength: strength of blur to apply to image.

    :type img: numpy.array
    :type lower: tuple of 3 int
    :type upper: tuple of 3 int
    :type iterations: int
    :type blur_strength: int

    :return: dilated image after mask and blur, contours, hierarchy.
    :rtype: tuple of 3 numpy.array
    """
    # Blur image to remove noise.
    blur_img = cv2.GaussianBlur(img, (15, 15), blur_strength)

    # Convert image to HSV color space.
    hsv = cv2.cvtColor(blur_img, cv2.COLOR_BGR2HSV)

    # Create mask for color in range.
    mask = cv2.inRange(hsv, lower, upper)

    # Close fuzzy contours by creating ellipses on the contour ends and dilate them.
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.dilate(mask, kernel, iterations=iterations)

    # Find all contours on image.
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return dilated, contours, hierarchy
