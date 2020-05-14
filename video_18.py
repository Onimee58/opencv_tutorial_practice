# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:43:31 2020

@author: Saif
"""

#%% canny edge detection

import cv2
import numpy as np
import matplotlib.pyplot as plt

def call_back(x):
    pass

img = cv2.imread('video_18_image.jpg', 0)
cv2.namedWindow('track')
cv2.createTrackbar('tr1', 'track', 0, 255, call_back)
cv2.createTrackbar('tr2', 'track', 0, 255, call_back)


while True:
    tr1 = cv2.getTrackbarPos('tr1', 'track')
    tr2 = cv2.getTrackbarPos('tr2', 'track')
    canny = cv2.Canny(img, tr1, tr2)
    
    cv2.imshow('image', img)
    cv2.imshow('canny', canny)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break


image = [img, canny]
title = ['original', 'canny']
n = len(title)

# for i in range(n):
#     plt.subplot(1, n, i+1)
#     plt.imshow(image[i], 'gray')
#     plt.title(title[i])
#     plt.xticks([])
#     plt.yticks([])
    
# plt.show()
cv2.destroyAllWindows()


