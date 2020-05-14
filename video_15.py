# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:57:58 2020

@author: Saif
"""

#%% morphological transformation

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('video_15_image.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
_, mask = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((4, 4), dtype = np.uint32)/16
dltn = cv2.dilate(mask, kernel, iterations = 2)
ersn = cv2.erode(mask, kernel, iterations = 1)
opng = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = 1)  
clsng = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations = 1)  
grdnt = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel, iterations = 1)  
tpht = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel, iterations = 1)  
crss = cv2.morphologyEx(mask, cv2.MORPH_CROSS, kernel, iterations = 1)  


image = [img, mask, dltn, ersn, opng, clsng, grdnt, tpht, crss]
title = ['original', 'mask', 'dilated', 'eroded', 'opening', 'closing', 'gradient', 'tophat', 'cross']
n = len(title)


for i in range(n):
    plt.subplot(3, n/2, i+1)
    plt.imshow(image[i])
    plt.title(title[i])
    
plt.show()