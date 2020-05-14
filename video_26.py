# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:22:52 2020

@author: Saif
"""

#%% tamplate matching

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('video_26_image.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
tmplt = cv2.imread('messi_face.jpg', 0)
height, width = tmplt.shape

res = cv2.matchTemplate(gray_img, tmplt, cv2.TM_CCOEFF_NORMED)
thresh = .9
idx = np.where(res > thresh)

cv2.rectangle(img, (idx[1][0], idx[0][0]), (idx[1][0]+width, idx[0][0]+height), (0, 0, 255), 2)

cv2.imshow('image', img)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
