1.2. find_center()
========
This function is used if you want to find center of mass of the contour on image in x-y range.

Usage
~~~~~

.. code-block:: python

    transform.find_center(img, low, high, iterations, blur_strength, x_range, y_range)

Parameters:
    * **img**: image to be processed. Must be a numpy array;
    * **low**: lower color range in HSV color space. Default is tuple (0, 0, 0). Must be a tuple of 3 integers;
    * **high**: upper color range in HSV color space. Default is tuple (255, 255, 255). Must be a tuple of 3 integers;
    * **iterations**: number of iterations for the morphological transformation. Default is 1. Must be an integer;
    * **blur_strength**: strength of the blur. Default is 0. Must be an integer;
    * **x_range**: Pixel x-coordinates to cut off the image. Must not exceed the total number of pixels in the image. Must be a tuple of 2 integers;
    * **y_range**: Pixel y-coordinates to cut off the image. Must not exceed the total number of pixels in the image. Must be a tuple of 2 integers.

Returns:
    * **found**: True if the center of mass is found, False otherwise;
    * **center**: (x, y) coordinates of the center of mass. If the center is not found, it returns (0, 0).
    * **img**: Cut image by x-y range

Examples
~~~~~~~~

WIP