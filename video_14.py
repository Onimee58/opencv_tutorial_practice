# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:56:32 2020

@author: Saif
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def call_back(x):
    pass

img = cv2.imread('video_14_image.jpg', 0)

  
thr = 127
_, thresh_bin_img = cv2.threshold(img, thr, 255, cv2.THRESH_BINARY)
_, thresh_bin_inv_img = cv2.threshold(img, thr, 255, cv2.THRESH_BINARY_INV)
_, thresh_trunc_img = cv2.threshold(img, thr, 255, cv2.THRESH_TRUNC)
_, thresh_tozero_img = cv2.threshold(img, thr, 255, cv2.THRESH_TOZERO)
_, thresh_tozero_inv_img = cv2.threshold(img, thr, 255, cv2.THRESH_TOZERO_INV)

title = ['original', 'bin', 'inv_bin', 'trunc', 'tozero', 'inv_tozero']
images = [img, thresh_bin_img, thresh_bin_inv_img, thresh_trunc_img, thresh_tozero_img, thresh_tozero_inv_img]

for i in range(len(title)):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([])
    plt.yticks(([]))
plt.show()