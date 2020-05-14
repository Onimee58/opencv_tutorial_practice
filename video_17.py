# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:37:55 2020

@author: Saif
"""

#%% smoothing or blurring image

import cv2
import numpy as np
import matplotlib. pyplot as plt


img = cv2.imread('video_17_image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((4, 4), dtype = np.uint32)/16
fltr_2d = cv2.filter2D(img, -1, kernel)
blr_img = cv2.blur(img, (5, 5))
fltr_gauss = cv2.GaussianBlur(img, (5, 5), 0)
fltr_med = cv2.medianBlur(img, 5)
fltr_bltr = cv2.bilateralFilter(img, 5, 75, 75)



image = [img, fltr_2d, blr_img, fltr_gauss, fltr_med, fltr_bltr]
title = ['image', '2D_filter', 'blur_image', 'gaussian_blur', 'median_blur', 'bilateral_blur']
n = len(title)

for i in range(n):
    plt.subplot(3, n/2, i+1)
    plt.imshow(image[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
