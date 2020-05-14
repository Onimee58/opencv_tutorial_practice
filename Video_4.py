# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:31:37 2020

@author: Saif
"""
#%% change video parameters
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 3000)
cap.set(4, 3000)
fourcc =cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video_4_output.avi', fourcc, 20.0, (1280,720))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        height , width = cap.get(3) , cap.get(4)
        text = str(width) + ' x ' + str(height)
        grey_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vdo_frame = cv2.putText(frame, text, (0,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        vdo_frame = cv2.circle(vdo_frame , (50,250), 50, (255,0,0), 5)
        out.write(vdo_frame)
        cv2.imshow('window_1', vdo_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
