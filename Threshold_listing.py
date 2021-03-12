# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:15:02 2021
@author: MahZaky
<<< SirMahZaky >>>
"""

import cv2 as cv 
import numpy as np 

def gray2rgb( g):
    img = np.zeros(g.shape+(3,) ) 
    img[:,:,0],img[:,:,1],img[:,:,2] = [g]*3
    return img 


img = cv.imread('sample/rice.bmp',0)


vid = cv.VideoWriter('vide.avi',
                     cv.VideoWriter_fourcc(*'XVID'),
                     20, img.shape) 

cv.namedWindow('gray') 
cv.imshow('gray', img) 


for i in range( 1,255 ) :
    ret, thr = cv.threshold(img, i, 255, cv.THRESH_BINARY ) 
    
    thr= gray2rgb(thr ) 
    cv.imshow( 'gray', thr)
    vid.write(thr) 
    cv.waitKey(10) 
    
vid.release() 
cv.destroyAllWindows()