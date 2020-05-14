# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:07:46 2020

@author: Saif
"""

#%% making a gs image

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.ones((255,255), dtype=np.uint8)
height, width = img.shape

for h in range(height):
    for w in range(width):
        img[h,w] = w

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
plt.imshow(img)
plt.imsave('video_12_image.jpg', img)
print('done')

#%% thresholding

import cv2
import numpy as np

def call_back(x):
    pass

img = cv2.imread('video_12_image.jpg', 0)
cv2.namedWindow('trace')
cv2.createTrackbar('thresh', 'trace', 0, 255, call_back)

while True:    
    thr = cv2.getTrackbarPos('thresh', 'trace')
    _, thresh_bin_img = cv2.threshold(img, thr, 255, cv2.THRESH_BINARY)
    _, thresh_bin_inv_img = cv2.threshold(img, thr, 255, cv2.THRESH_BINARY_INV)
    _, thresh_trunc_img = cv2.threshold(img, thr, 255, cv2.THRESH_TRUNC)
    _, thresh_tozero_img = cv2.threshold(img, thr, 255, cv2.THRESH_TOZERO)
    _, thresh_tozero_inv_img = cv2.threshold(img, thr, 255, cv2.THRESH_TOZERO_INV)
    
    
    cv2.imshow('thresh_bin_image', thresh_bin_img)
    cv2.imshow('thresh_bin_inv_image', thresh_bin_inv_img)
    cv2.imshow('thresh_trunc_image', thresh_trunc_img)
    cv2.imshow('thresh_tozero_image', thresh_tozero_img)
    cv2.imshow('thresh_tozero_inv_image', thresh_tozero_inv_img)    
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
