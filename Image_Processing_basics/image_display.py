import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread('ameya.jpeg')
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

plt.imshow(image1)