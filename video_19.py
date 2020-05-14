# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:08:22 2020

@author: Saif
"""

#%% image pyramids

import cv2
import numpy as np
import matplotlib.pyplot as plt

def call_back(x):
    pass

img = cv2.imread('video_19_image.jpg')
cp_img = img.copy()
gauss_pyrDWN = [cp_img]

for i in range(6):
    cp_img = cv2.pyrDown(cp_img)
    gauss_pyrDWN.append(cp_img)
    #cv2.imshow(str(i), cp_img)

for j in range(5, 0, -1):
    extended_gauss_img = cv2.pyrUp(gauss_pyrDWN[j])
    lplc_img = cv2.subtract(gauss_pyrDWN[j-1], extended_gauss_img) 
    cv2.imshow(str(j), lplc_img)
    
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()