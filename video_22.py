# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:56:32 2020

@author: Saif
"""

#%% Finding contours

import cv2
import numpy as np
import matplotlib.pyplot as plt

def call_back(x):
    pass

img = cv2.imread('video_22_image.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray_img, 150, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('Number of contours = ' + str(len(contours)))
cv2.drawContours(img, contours, -1, (0, 0, 0), 3)

cv2.imshow('image', img)
cv2.imshow('gray image', gray_img)
cv2.imshow('threshed image', thresh)




cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()