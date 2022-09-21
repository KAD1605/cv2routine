from setuptools import setup

# import os

SHORT_DESCRIPTION = 'Helps with routines in OpenCV'

# def requirements():
#     with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), encoding='utf-8') as f:
#         return f.read().splitlines()
try:
    with open('README.md', encoding='utf8') as readme:
        LONG_DESCRIPTION = readme.read()

except FileNotFoundError:
    LONG_DESCRIPTION = SHORT_DESCRIPTION

setup(install_requires=[
    "setuptools==65.3.0",
    "opencv-python==4.6.0.66",
    "numpy==1.23.3",
],
    name='cv2routine',
    version='0.0.2',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author="Klinovitskij Andrey",
    author_email="adk160501@gmail.com",
    url="",
    license="MIT",
    packages=['cv2routine'],
    zip_safe=False)