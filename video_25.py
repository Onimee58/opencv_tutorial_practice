# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:36:42 2020

@author: Saif
"""

#%% image histograms

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('video_25_image.jpg', 0)
#b, g, r = cv2.split(img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist)

#cv2.imshow('image', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

#plt.hist(img.ravel(), 256, [0,256])
# plt.hist(b.ravel(), 256, [0,256])
# plt.hist(g.ravel(), 256, [0,256])
# plt.hist(r.ravel(), 256, [0,256])


plt.show()

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
