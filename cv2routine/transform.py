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
    if blur_strength > 0:
        img = cv2.GaussianBlur(img, (blur_strength, blur_strength), 0)

    # Convert image to HSV color space.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create mask for color in range.
    mask = cv2.inRange(hsv, lower, upper)

    # Close fuzzy contours by creating ellipses on the contour ends and dilate them.
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.dilate(mask, kernel, iterations=iterations)

    # Find all contours on image.
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return dilated, contours, hierarchy

def find_center(img: np.array, lower: Tuple[int, int, int] = (0, 0, 0),
                   upper: Tuple[int, int, int] = (255, 255, 255),
                   iterations: int = 1, blur_strength: int = 0, x_range: Tuple[int, int] = (0, 0),
                   y_range: Tuple[int, int] = (0, 0)):
    """
    The function finds objects by color mask and displays a frame with label on the image.

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

    :return: image with frame and label, dilated image after mask and blur.
    :rtype: tuple of 2 numpy.array
    """
    # Prepare image for contour search.
    img = img[x_range[0]:x_range[1], y_range[0]:y_range[1]]

    dilated, contours, hierarchy = img_prep(img, lower, upper, iterations, blur_strength)
    center = (0, 0)

    if len(contours) > 0:
        max_cnt = max(contours, key=cv2.contourArea)
        # find center of max_cnt
        M = cv2.moments(max_cnt)
        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        else:
            return False, center, img
    else:
        return False, center, img

    return True, center, img
