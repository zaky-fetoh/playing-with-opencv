# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:51:35 2021
@author: MahZaky
<<< SirMahZaky >>>
"""

import cv2 as cv 
import numpy as np



def draw_rect(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN :
        cv.circle(img,(x,y), 50, color = (0,255,0), thickness = -1)
    elif event == cv.EVENT_RBUTTONDOWN :
        cv.circle(img,(x,y), 50, color = (255,0,0), thickness = -1)
        

img = np.zeros((720,720,3)) 
cv.namedWindow('dr' ) 
cv.setMouseCallback('dr',draw_rect ) 

while True :
    cv.imshow('dr',img) 
    if cv.waitKey(5) & 0xFF == ord('q') :
        break
    
cv.destroyWindow('dr') 