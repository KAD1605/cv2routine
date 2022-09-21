import cv2
import numpy as np
import cv2routine.transform

from typing import Tuple


def draw_rect_frame(img: np.array, lower: Tuple[int, int, int], upper: Tuple[int, int, int], label: str = "",
                    iterations: int = 1, blur_strength: int = 5, min_area: int = 1000, only_max: bool = False,
                    text_color: Tuple[int, int, int] = (255, 0, 0)):
    """
    The function finds objects by color mask and displays a frame with label on the image.

    :param img: image to search objects and draw frame
    :param lower: lower bound of color to search for (HSV).
    :param upper: upper bound of color to search for (HSV).
    :param label: label for drawing in the center of the frame.
    :param iterations: number of iterations to dilate image (increase to find smaller contours but accuracy decreases).
    :param blur_strength: strength of blur to apply to image.
    :min_area: minimum area of object to draw frame.
    :param only_max: draw frame only for the largest object.
    :param text_color: BGR color of text to draw.

    :type img: numpy.array
    :type lower: tuple of 3 int
    :type upper: tuple of 3 int
    :type label: str
    :type iterations: int
    :type blur_strength: int
    :type min_area: int
    :type only_max: bool
    :type text_color: tuple of 3 int

    :return: image with frame and label, dilated image after mask and blur.
    :rtype: tuple of 2 numpy.array
    """
    # Prepare image for contour search.
    dilated, contours, hierarchy = transform.img_prep(img, lower, upper, iterations, blur_strength)

    # Get text size to draw it in the center of the frame.
    (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 1, 1)

    # Draw frame only for the largest contour.
    if only_max:
        # Find the largest contour.
        if len(contours) > 0:
            max_cnt = max(contours, key=cv2.contourArea)
            if cv2.contourArea(max_cnt) < min_area:
                return img, dilated
            # Find coordinates of the frame for the largest contour.
            x, y, w, h = cv2.boundingRect(max_cnt)
            # Draw frame.
            cv2.rectangle(img, (x, y), (x + w, y + h), text_color, 2)
            # Draw label in the center of the frame.
            cv2.putText(img, label, (int(x + (w - text_width) / 2), int(y + (h + text_height) / 2)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

    # Draw frame for all contours.
    else:
        for cnt in contours:
            # If the contour area is less than the minimum area, skip it.
            if cv2.contourArea(cnt) < min_area:
                continue
            # Find coordinates of the frame for the contour.
            x, y, w, h = cv2.boundingRect(cnt)
            # Draw frame.
            cv2.rectangle(img, (x, y), (x + w, y + h), text_color, 2)
            # Draw label in the center of the frame.
            cv2.putText(img, label, (int(x + (w - text_width) / 2), int(y + (h + text_height) / 2)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

    # Return image with frame and label.
    return img, dilated
    # cv2.imshow('mask', mask)
    # cv2.imshow('dilated', dilated)


def draw_ellipse_frame(img: np.array, lower: Tuple[int, int, int], upper: Tuple[int, int, int], label: str = "",
                       iterations: int = 1, blur_strength: int = 5, min_area: int = 1000, only_max: bool = False,
                       text_color: Tuple[int, int, int] = (255, 0, 0)):
    """
        The function finds objects by color mask and displays a circumscribed ellipse with label on the image.

        :param img: image to search objects and draw ellipse
        :param lower: lower bound of color to search for (HSV).
        :param upper: upper bound of color to search for (HSV).
        :param label: label for drawing in the center of the ellipse.
        :param iterations: number of iterations to dilate image
            (increase to find smaller contours but accuracy decreases).
        :param blur_strength: strength of blur to apply to image.
        :min_area: minimum area of object to draw ellipse.
        :param only_max: draw ellipse only for the largest object.
        :param text_color: BGR color of text to draw.

        :type img: numpy.array
        :type lower: tuple of 3 int
        :type upper: tuple of 3 int
        :type label: str
        :type iterations: int
        :type blur_strength: int
        :type min_area: int
        :type only_max: bool
        :type text_color: tuple of 3 int

        :return: image with ellipse and label, dilated image after mask and blur
            and angle of the ellipse (if only_max is True).
        :rtype: tuple of 2 numpy.array, float
        """
    # Prepare image for contour search.
    dilated, contours, hierarchy = transform.img_prep(img, lower, upper, iterations, blur_strength)

    # Get text size to draw it in the center of the frame.
    (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 1, 1)

    # Draw ellipse only for the largest contour.
    if only_max:
        # Find the largest contour.
        if len(contours) > 0:
            max_cnt = max(contours, key=cv2.contourArea)
            if cv2.contourArea(max_cnt) < min_area:
                return img, dilated, None
            # Find coordinates of the frame for the largest contour.
            (x, y), (MA, ma), angle = cv2.fitEllipse(max_cnt)
            # Draw frame.
            cv2.ellipse(img, (int(x), int(y)), (int(MA / 2), int(ma / 2)), angle, 0, 360, text_color, 2)
            # Draw label in the center of the frame.
            cv2.putText(img, label, (int(x - text_width / 2), int(y + text_height / 2)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
            return img, dilated, angle

    # Draw ellipse for all contours.
    else:
        for cnt in contours:
            # If the contour area is less than the minimum area, skip it.
            if cv2.contourArea(cnt) < min_area:
                continue
            # Find coordinates of the ellipse for the contour.
            (x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
            # Draw frame.
            cv2.ellipse(img, (int(x), int(y)), (int(MA / 2), int(ma / 2)), angle, 0, 360, text_color, 2)
            # Draw label in the center of the frame.
            cv2.putText(img, label, (int(x - text_width / 2), int(y + text_height / 2)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

    # Return image with ellipse and label.
    return img, dilated, None
