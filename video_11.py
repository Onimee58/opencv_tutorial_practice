# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:31:54 2020

@author: Saif
"""

#%% image color space object trace

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def call_back(x):
    pass
cv2.namedWindow('tracking')

cv2.createTrackbar('lower_hue', 'tracking', 0, 255, call_back)
cv2.createTrackbar('upper_hue', 'tracking', 255, 255, call_back)
cv2.createTrackbar('lower_saturation', 'tracking', 0, 255, call_back)
cv2.createTrackbar('upper_saturation', 'tracking', 255, 255, call_back)
cv2.createTrackbar('lower_value', 'tracking', 0, 255, call_back)
cv2.createTrackbar('upper_value', 'tracking', 255, 255, call_back)

while True:
    #img = cv2.imread('video_11_image.jpg')
    _, img = cap.read()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   
    
    LH = cv2.getTrackbarPos('lower_hue', 'tracking')
    UH = cv2.getTrackbarPos('upper_hue', 'tracking')
    LS = cv2.getTrackbarPos('lower_saturation', 'tracking')
    US = cv2.getTrackbarPos('upper_saturation', 'tracking')
    LV = cv2.getTrackbarPos('lower_value', 'tracking')
    UV = cv2.getTrackbarPos('upper_value', 'tracking')
    
    lower_limit = np.array([LH, LS, LV])
    upper_limit = np.array([UH, US, UV])
    
    mask = cv2.inRange(hsv_img, lower_limit, upper_limit)    
    hsv_masked = cv2.bitwise_and(img, img, mask=mask)
    
    cv2.imshow('image', img)
    cv2.imshow('masked_image', hsv_masked)
    cv2.imshow('hsv_image', hsv_img)
    cv2.imshow('mask', mask)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
