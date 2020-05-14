# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:35:30 2020

@author: Saif
"""

#%% Capture , read , write and put text on video
import cv2

cap = cv2.VideoCapture(0)
fourcc =cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video_2_output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        height , width = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) , cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        text = str(width) + ' x ' + str(height)
        grey_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vdo_frame = cv2.putText(frame, text, (0,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        
        out.write(vdo_frame)
        cv2.imshow('window_1', vdo_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
