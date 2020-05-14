# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:16:06 2020

@author: Saif
"""

#%% handling more mouse input

import cv2
import numpy as np

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        coordinates.append((x,y))
        color = (255,0,0)
        cv2.circle(img, (x,y), 5, color, -1)
        if len(coordinates) >= 2:
            cv2.line(img, coordinates[-1], coordinates[-2], color)
        cv2.imshow('image', img)
        
        
img = np.zeros((720,1280,3), dtype = np.uint8)
coordinates = []
#img = cv2.imread('video_6_image.png')
cv2.imshow('image', img)

cv2.setMouseCallback('image', mouse_click)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
