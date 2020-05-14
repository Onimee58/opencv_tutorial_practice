# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:55:34 2020

@author: Saif
"""

#%% image parameter tracking

import cv2
import numpy as np


def call_back(x):
   pass


img1 =np.zeros((500, 500, 3), dtype=np.uint8)
switch = '0 : Colored \n 1 : Greyscale'


cv2.namedWindow('image1')
cv2.createTrackbar('Blue', 'image1', 0, 255, call_back)
cv2.createTrackbar('Green', 'image1', 0, 255, call_back)
cv2.createTrackbar('Red', 'image1', 0, 255, call_back)
cv2.createTrackbar(switch, 'image1', 0, 1, call_back)

while(True):
    b = cv2.getTrackbarPos('Blue', 'image1')
    g = cv2.getTrackbarPos('Green', 'image1')
    r = cv2.getTrackbarPos('Red', 'image1')
    s = cv2.getTrackbarPos(switch, 'image1')
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'r:' + str(r) + ' g:' + str(g) + ' b:' + str(b)
    color = (255, 0, 0)
    img1 = cv2.putText(img1, text, (100,100), font, 1, color)
    cv2.imshow('image1', img1)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    

    
    if s:
        img1[:] = b, g, r
    else:
        img1[:] = 0
    
cv2.destroyAllWindows()

