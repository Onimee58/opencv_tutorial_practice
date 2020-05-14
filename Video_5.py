# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:07:18 2020

@author: Saif
"""

#%% Show date and time

import cv2
import datetime


cap = cv2.VideoCapture(0)
fourcc =cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video_4_output.avi', fourcc, 20.0, (1280,720))


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        height , width = cap.get(4) , cap.get(3)
        text = str(width) + ' x ' + str(height)
        date_time = datetime.datetime.now()
        grey_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vdo_frame = cv2.putText(frame, text, (0,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        vdo_frame = cv2.putText(frame, str(date_time), (0,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        out.write(vdo_frame)
        cv2.imshow('window_1', vdo_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
