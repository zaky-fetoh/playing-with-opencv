# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:18:11 2021
@author: MahZaky
<<< SirMahZaky >>>
"""

import cv2 as cv 
import numpy as np 



dic = {'ref':(None,None) }
img = np.zeros((700,700,3)) 


def dist( p1, p2 ):
    p1,p2 = [np.array(x) for x in [p1,p2] ] 
    return np.sqrt( np.sum((p1 -p2) ** 2) ) 


def draw_circle(event, x, y, flags, param):
     
    if event == cv.EVENT_LBUTTONDOWN :
        dic['ref'] = (x,y) 
        print('RffP : ', x,y) 
    elif event == cv.EVENT_LBUTTONUP :
        d = dist(dic['ref'], (x,y) ) 
        print( 'distance : ' ,d) 
        print('endP : ', x,y)
        cv.circle(img, dic['ref'], radius = int(d), thickness= 1,
                  color = (255,0,0) ) 

cv.namedWindow('wind_draw_circle')    
cv.setMouseCallback('wind_draw_circle', draw_circle ) 


while True :
    cv.imshow('wind_draw_circle', img) 
    if cv.waitKey(10) & 0xFF == ord('q'):
        break
    
cv.destroyWindow('wind_draw_circle') 
        