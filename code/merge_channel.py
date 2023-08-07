#!/usr/bin/env python
# coding: utf-8
# %%
import numpy as np
import cv2
from PIL import Image


class RG_CANNY(object):
    
    def __init__(self):
        pass
     
    def __call__(self, img):
        
        # 讀取影像
        image = np.array(img)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 邊緣檢測
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # gray
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        canny = cv2.Canny(blurred, 30, 150) # canny
        
        # 黑白轉換
        for pixel in canny:
            for i in range(len(pixel)):
                if pixel[i] == 255:
                    pixel[i] = 0
                elif pixel[i] == 0:
                    pixel[i] = 255
        
        # 通道堆疊
        b, g, r = cv2.split(image)
        new_img = cv2.merge([r, canny, g])
        new_img= Image.fromarray(new_img.astype('uint8')).convert('RGB') 
        
        return new_img

class CANNY(object):
    
    def __init__(self):
        pass
     
    def __call__(self, img):
        
        # 讀取影像
        image = np.array(img)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 邊緣檢測
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # gray
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        canny = cv2.Canny(blurred, 30, 150) # canny
        
        # 黑白轉換
        for pixel in canny:
            for i in range(len(pixel)):
                if pixel[i] == 255:
                    pixel[i] = 0
                elif pixel[i] == 0:
                    pixel[i] = 255
        
        # 通道堆疊
        new_img = cv2.merge([canny, canny, canny])
        new_img= Image.fromarray(new_img.astype('uint8')).convert('RGB') 
        
        return new_img
        
class CTG(object):
    
    def __init__(self):
        pass
     
    def __call__(self, img):
        
        # 讀取影像
        image = np.array(img)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 邊緣檢測
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # gray
        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) # thresh
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        canny = cv2.Canny(blurred, 30, 150) # canny
        
        # 黑白轉換
        for pixel in canny:
            for i in range(len(pixel)):
                if pixel[i] == 255:
                    pixel[i] = 0
                elif pixel[i] == 0:
                    pixel[i] = 255
        
        # 通道堆疊
        new_img = cv2.merge([canny, thresh, gray])
        new_img= Image.fromarray(new_img.astype('uint8')).convert('RGB') 
        
        return new_img