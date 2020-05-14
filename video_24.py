# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:56:20 2020

@author: Saif
"""

#%% detecting geometric shapes

import cv2
import numpy as np
import matplotlib.pyplot as plt

def call_back(x):
    pass

img = cv2.imread('video_24_image.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.namedWindow('tracking')
# cv2.createTrackbar('track', 'tracking', 0, 255, call_back)

while True:
    # tr = cv2.getTrackbarPos('track', 'tracking')
    tr = 214
    _, thresh = cv2.threshold(gray_img, tr, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for c in contours:
        approx = cv2.approxPolyDP(c, .01*cv2.arcLength(c, True), True)
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
        x, y = approx.ravel()[0]-5, approx.ravel()[1]-10
        n = len(approx)
        if n == 3:
            text = 'triangle'
        elif n == 4:
            text = 'rectangle'
        elif n == 5:
            text = 'pentagon'
        elif n == 6:
            text = 'star'
        else:
            text = 'circle'
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 0))

    cv2.imshow('image', img)
    cv2.imshow('threshold', thresh)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
