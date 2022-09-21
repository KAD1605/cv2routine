from setuptools import setup
# import os


# def requirements():
#     with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), encoding='utf-8') as f:
#         return f.read().splitlines()


setup(install_requires=[
    "setuptools==65.3.0",
    "opencv-python==4.6.0.66",
    "numpy==1.23.3",
    ],
    name='cv2routine',
    version='0.0.1',
    description='Helps with routines in OpenCV',
    author="Klinovitskij Andrey",
    author_email="adk160501@gmail.com",
    url="",
    license="MIT",
    packages=['cv2routine'],
    zip_safe=False)
