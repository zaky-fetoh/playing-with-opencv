# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:28:16 2021
@author: MahZaky
<<< SirMahZaky >>>
"""

import cv2 as cv 
import numpy as np 

winname = 'window1'

win_list = [ winname ] 
di, imgs = dict(), dict() 
di[winname] = dict()
di[winname]['drawing'] = False
imgs[winname] = np.zeros((700,700,3)) 

def draw_rect(event, x, y, flags, param): 
    flags = winname
    if event == cv.EVENT_LBUTTONDOWN :
        di[flags]['image'] = imgs[flags].copy()
        di[flags]['reff_ptr'] = (x,y) 
        di[flags]['drawing'] = True
    elif event == cv.EVENT_LBUTTONUP :
        di[flags]['drawing'] = False
        imgs[flags] = di[flags]['image'].copy()
        cv.rectangle(imgs[flags], di[flags]['reff_ptr'], (x,y),
                     color = (255,0,0), thickness = 3 ) 
    elif event == cv.EVENT_MOUSEMOVE :
        if di[flags]['drawing'] :
            imgs[flags] = di[flags]['image'].copy()
            cv.rectangle(imgs[flags], di[flags]['reff_ptr'], (x,y),
                         color = (255,0,0), thickness = 3 ) 
        
cv.namedWindow(winname, flags = 0)         
cv.setMouseCallback(winname, draw_rect ) 

while True :
    cv.imshow(winname, imgs[winname] ) 
    
    if cv.waitKey(0)  == ord('q'):
        break 
    
cv.destroyWindow(winname) 
        
    
    
    
    
    
    
    
    
    
    

        
        