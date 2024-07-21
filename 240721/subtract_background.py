import numpy as np
import cv2
import matplotlib.pyplot as plt

bg1_img = cv2.imread('NewBackground.jpg', 1)
height, width, channels = bg1_img.shape

bg2_img = cv2.imread('GreenBackground.png',1)
bg2_img = cv2.resize(bg2_img,(width,height))

ob_img = cv2.imread('Object.png', 1)
ob_img = cv2.resize(ob_img,(width,height))
plt.imshow(bg1_img)

# def compute_difference(bg_img, input_img):







