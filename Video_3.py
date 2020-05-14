# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 17:16:37 2020

@author: Saif
"""

#%% Draw diffeent shapes on images
import cv2
import numpy as np

img = np.zeros([1000,1000,3], np.uint8)

img = cv2.line(img, (0,0), (250,250), (147,96,44), 5)
img = cv2.arrowedLine(img, (250,250), (750,500), (0,0,255), 5)
img = cv2.rectangle(img, (750,500), (850,600), (0,255,0), 5)
img = cv2.circle(img , (50,250), 50, (255,0,0), 5)
cv2.imshow('window_1', img)
cv2.imwrite('video_2_image.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
