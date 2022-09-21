=====================
Modules and functions
=====================
This package contains several modules that contain functions sorted by operating principle. This is made for the convenience of using the package.

transform
*********
This module contains functions that transform images.

img_prep
--------
This function is used if you want to find contours in the image within a certain color range.

Usage
~~~~~
.. code-block:: python
    img_prep(img, low=, high, iterations, blur_blur_strength)
Parameters:
    * img: image to be processed. It must be a numpy array.
    * low: lower color range in HSV color space. Default is tuple (0, 0, 0)
    * high: upper color range in HSV color space. Default is tuple (255, 255, 255)
    * iterations: number of iterations for the morphological transformation. Default is 1. Must be an integer.
    * blur_blur_strength: strength of the blur. Default is 0. Must be an integer.
Returns:
    * img: processed image
    * contours: list of contours found in the image
    * hierarchy: list of hierarchy found in the image

Examples
~~~~~~~~
WIP

figures
*******
This module contains functions that create frame on the image.

draw_rect_frame
---------------

draw_circle_frame
-----------------

