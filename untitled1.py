# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I0Z-GmHfOu_yy2I3VS5NxXBYbRt6twgU
"""

import cv2
import matplotlib.pyplot as plt

def convert_to_colored_image(grayscale_image_path):
    # Read the grayscale image
    grayscale_image = cv2.imread(grayscale_image_path, cv2.IMREAD_GRAYSCALE)

    # Apply a colormap (here using the 'COLORMAP_JET' colormap, you can choose others)
    colored_image = cv2.applyColorMap(grayscale_image, cv2.COLORMAP_JET)

    # Display the images using matplotlib
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(grayscale_image, cmap='gray')
    plt.title('Grayscale Image')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(colored_image, cv2.COLOR_BGR2RGB))
    plt.title('Colored Image')

    plt.show()

# Example usage
input_image_path = "grayscale.jpeg"
convert_to_colored_image(input_image_path)

"""# New Section"""