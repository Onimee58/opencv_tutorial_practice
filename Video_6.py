# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:15:03 2020

@author: Saif
"""

#%% handling mouse input

import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x)+ ',' +str(y)
        color = (255,0,0)
        cv2.putText(img, text, (x,y), font, 1, color)
        cv2.imshow('image', img)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        r, g, b = img[y, x, 2], img[y, x, 1], img[y, x, 0]
        print(r, ',', g, ',', b)
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255,0,0)
        text = str(r)+ ',' +str(g)+ ',' +str(b)
        cv2.putText(img, text, (x,y), font, 1, color)
        cv2.imshow('image', img)
        
    if event == cv2.EVENT_LBUTTONDBLCLK:
        r, g, b = img[:, :, 2], img[:, :, 1], img[:, :, 0]
        r, g, b = r+10, g+10, b+10
        img[:, :, 2], img[:, :, 1], img[:, :, 0] = r, g, b
        print('making bright')
        cv2.imshow('image', img)
        
#img = np.zeros((720,1280,3), dtype = np.uint8)
img = cv2.imread('video_8_image_1.jpg')
#img = cv2.imread('video_11_image.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', mouse_click)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
