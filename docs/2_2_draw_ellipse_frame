2.2. draw_ellipse_frame()
=================
This function is used if you want to find contours in the image within a certain color range and display the circumscribed ellipse with the label

Usage
~~~~~

.. code-block:: python

    draw_ellipse_frame(img, low, high, label, iterations, blur_strength, min_area, only_max, text_color)

Parameters:
    * **img**: image to be processed. It must be a numpy array;
    * **low**: lower color range in HSV color space. Default is tuple (0, 0, 0). Must be a tuple of 3 integers;
    * **high**: upper color range in HSV color space. Default is tuple (255, 255, 255). Must be a tuple of 3 integers;
    * **label**: label to be displayed on the frame. Default is "". Must be a string;
    * **iterations**: number of iterations for the morphological transformation. Default is 1. Must be an integer;
    * **blur_strength**: strength of the blur. Default is 0. Must be an integer;
    * **min_area**: minimum area of the contour for detect. Default is 1000. Must be an integer;
    * **only_max**: if True, only the largest contour will be detected. Default is False. Must be a boolean;
    * **text_color**: color of the text in BGR. Default is (255, 0, 0). Must be a tuple of 3 integers.

Returns:
    * **img**: processed image
    * **dilated**: dilated image (for debug)
    * **angle**: tilt angle of the ellipse if only_max is True. If only_max is False, returns None.

Examples
~~~~~~~~
WIP