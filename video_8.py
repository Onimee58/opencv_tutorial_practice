# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:02:06 2020

@author: Saif
"""
#%% modify image properties

import cv2
import numpy as np

img1 = cv2.imread('video_8_image_1.jpg')
img2 = cv2.imread('video_8_image_2.jpg')

img1 = cv2.resize(img1, (500,500))
img2 = cv2.resize(img2, (500,500))

img3 = cv2.add(img1, img2)
img4 = cv2.addWeighted(img1, .1, img2, .9, .1)
cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('added_image', img3)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()