# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:23:34 2020

@author: Saif
"""

#%% motion detection

import cv2
import numpy as np
import matplotlib.pyplot as plt

def call_back(x):
    pass

cap = cv2.VideoCapture('video_23_video.mp4')
ret, f = cap.read()

while ret:
    _, f = cap.read()
    _, f1 = cap.read()
    _, f2 = cap.read()
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
    diff = cv2.absdiff(f2, f1)
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blr_diff = cv2.GaussianBlur(gray_diff, (5, 5), 0)
    _, thresh = cv2.threshold(blr_diff, 20, 255, cv2.THRESH_BINARY)
    dlt_diff = cv2.dilate(thresh, None, iterations = 3)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
    contours, _ = cv2.findContours(dlt_diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        
        if cv2.contourArea(c) < 1000:
            continue
        
        cv2.rectangle(f1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(f1, 'moving', (20,20), 0, 1, (0, 0, 255), 2)
    
    # cv2.drawContours(f1, contours, -1, (0, 255, 0), 2)
    f1 = cv2.resize(f1, (700, 500))
    f = cv2.resize(f, (700, 500))
    cv2.imshow('detected feed', f1)
    cv2.imshow('general feed', f)
    
    if cv2.waitKey(40) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
