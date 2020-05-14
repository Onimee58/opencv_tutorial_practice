# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:28:03 2020

@author: Saif
"""

import cv2
import numpy as np

def call_back(x):
    pass

img = cv2.imread('video_13_image.jpg', 0)
img = cv2.resize(img, (500,500))
cv2.namedWindow('trace')
cv2.createTrackbar('thresh', 'trace', 0, 255, call_back)

while True:    
    thr = cv2.getTrackbarPos('thresh', 'trace')
    adpt_mean_thresh_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)
    adpt_gauss_thresh_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
    
    
    cv2.imshow('image1', adpt_mean_thresh_img)
    cv2.imshow('image2', adpt_gauss_thresh_img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()