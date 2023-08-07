#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from PIL import Image
import random


class AddSaltPepperNoise(object):

    def __init__(self, density):
        self.density = density

    def __call__(self, img):
        img = np.array(img)
        img_h, img_w, img_c = img.shape

        array = np.linspace(255, 255, img_h*img_w*img_c)
        dist_img = np.reshape(array,(img_h,img_w,img_c))

        h, w, c = dist_img.shape
        Nd = self.density
        Sd = 1 - Nd
        # 生成一個通道的mask
        mask = np.random.choice((0, 1, 2), size=(h, w, 1), p=[Nd/2.0, Nd/2.0, Sd]) 
        # 生成彩色的mask
        mask = np.repeat(mask, c, axis=2)
        dist_img[mask == 0] = 0 # 椒                                                             
        dist_img[mask == 1] = 0 # 鹽
        dist_img = Image.fromarray(np.uint8(dist_img))
        dist_img = np.array(dist_img)
        
        img_add=cv2.addWeighted(img,0.7,dist_img,0.3,0)
        # numpy轉圖片
        img= Image.fromarray(img_add.astype('uint8')).convert('RGB')     
        
        return img


# In[ ]:

class AddGaussianNoise(object):
    
    def __init__(self, sigma):
        self.sigma = sigma
        self.mean = 0
        
    def __call__(self, img):
        img = np.array(img)
        img = img/255
        # 隨機生成高斯 noise
        noise = np.random.normal(self.mean, self.sigma, img.shape)
        # noise + 原圖
        gaussian_out = img + noise
        # 所有值必須介於 0~1 之間，超過1 = 1，小於0 = 0
        gaussian_out = np.clip(gaussian_out, 0, 1)

        # 原圖: float -> int (0~1 -> 0~255)
        gaussian_out = np.uint8(gaussian_out*255)
        gaussian_out= Image.fromarray(gaussian_out.astype('uint8')).convert('RGB')  
        
        return gaussian_out


# In[2]:


import numpy as np
from PIL import Image
import cv2


class AddFrameVertical(object):

    def __init__(self):
        self.start_point = (3,0)
        self.end_point = (3,64)

    def __call__(self, img):
        img = np.array(img)                                                             # 图片转numpy
        start = self.start_point
        end = self.end_point     
        color = (255, 0, 0)
        thickness = 1
        img = cv2.line(img, start, end, color, thickness) 
        img= Image.fromarray(img.astype('uint8')).convert('RGB')                        # numpy转图片
        return img


# In[ ]:





# In[3]:


import numpy as np
from PIL import Image
import cv2


class AddFrameParallel(object):

    def __init__(self):
        self.start_point = (0,61)
        self.end_point = (64,61)

    def __call__(self, img):
        img = np.array(img)       
        start = self.start_point
        end = self.end_point     
        color = (255, 0, 0)
        thickness = 1
        img = cv2.line(img, start, end, color, thickness) 
        img= Image.fromarray(img.astype('uint8')).convert('RGB')                        
        return img

class AddRandomLine(object):

    def __init__(self):
        self.num = random.randint(1,5)

    def __call__(self, img):
        img = np.array(img)  
        num = self.num
        for i in range(num):
            h, w = img.shape[0], img.shape[1]
            (x1, y1) = ( 0 ,random.randint(0,h-10) )
            (x2, y2) = ( random.randint(0, w-10), random.randint(0, h-10))
            img = cv2.line(img,(x1, y1), (x2, y2),(0,0,0), random.randint(1,2))
        img= Image.fromarray(img.astype('uint8')).convert('RGB')                        
        return img

