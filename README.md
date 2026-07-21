# Invisible Cloak using OpenCV

## Overview

This project implements the famous **Invisible Cloak** effect using **Python, OpenCV, and NumPy**. It works by detecting a red-colored cloth in real time through a webcam and replacing that region with a previously captured background, creating the illusion of invisibility.

## Features

* Real-time webcam capture
* Detects red-colored objects using HSV color space
* Background subtraction for invisibility effect
* Noise reduction using Gaussian Blur and morphological operations
* Live display of the invisible cloak effect

## Technologies Used

* Python
* OpenCV
* NumPy

## How It Works

1. The webcam starts and captures the static background for a few seconds.
2. Each video frame is converted from BGR to HSV color space.
3. A mask is created to detect red-colored regions.
4. Morphological operations remove noise and improve mask quality.
5. The detected red region is replaced with the stored background image.
6. The processed frame is displayed in real time, making the red cloth appear invisible.

## Requirements

Install the required libraries:

pip install opencv-python numpy


## How to Run

1. Save the Python script.
2. Open a terminal in the project folder.
3. Run:

python invisible_cloak.py


4. Stand away from the camera while the background is being captured (about 3 seconds).
5. Hold a **plain red cloth** in front of the camera to see the invisible cloak effect.
6. Press **`d`** to exit the application.

## Project Structure


Invisible-Cloak/
│── invisible_cloak.py
│── README.md


## Notes

* Use a plain, bright red cloth for the best results.
* Ensure the background remains static after it is captured.
* Avoid having other red objects in the camera's view, as they may also become invisible.
* Good lighting improves color detection and overall performance.

## Future Improvements

* Automatic color selection for different cloak colors.
* Adaptive HSV thresholding for varying lighting conditions.
* Edge smoothing for more realistic blending.
* Background averaging over multiple frames for a cleaner effect.
* Support for higher-resolution cameras and performance optimization.

## Author

Developed as a Computer Vision project using Python, OpenCV, and NumPy.
