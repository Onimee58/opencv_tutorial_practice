# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:13:58 2020

@author: Saif
"""

#%% bitwise operation

import cv2

img1 = cv2.imread('video_9_image_1.jpg')
img2 = cv2.imread('video_9_image_2.jpg')

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not1 = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('bit_and_image', bit_and)
cv2.imshow('bit_or_image', bit_or)
cv2.imshow('bit_xor_image', bit_xor)
cv2.imshow('bit_not_image1', bit_not1)
cv2.imshow('bit_not_image2', bit_not2)


cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
