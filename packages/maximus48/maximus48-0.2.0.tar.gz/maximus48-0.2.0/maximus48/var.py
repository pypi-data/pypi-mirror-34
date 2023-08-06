#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 17:46:49 2018

@author: mpolikarpov
"""


import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from numpy import mean, square, sqrt



def im_folder(path):
    """
    lists images in the folder 
    
    Parameters
    __________
    path : str
    """
    
    fileformat = 'ppm','PPM','tiff','TIFF','tif','TIF','png','PNG', 'raw'
    curfol = os.getcwd()
    
    os.chdir(path)
    imfiles = os.listdir(path)
    imlist = [filename for filename in imfiles if filename.endswith(fileformat)]
    imlist.sort()
    os.chdir(curfol)
    
    return(imlist)
    

def show(image):
    
    """
    shows the 2D image 
    
    Parameters
    __________
    image : 2D array
    """
    
    plt.figure(num=None, figsize=(20, 20), facecolor='w', edgecolor='k')
    plt.imshow(image, cmap='gray')
    return;
    
    
def imrescale(data, bitnum=8):
    """
    increases brightness/contrast and returns it as int array
    
    Parameters
    __________
    data : ndarray 
        input image data 2D or 3D array
    bitnum: int 
        number of bits to save. by default is 8 bit
    """
    bit = 2**bitnum-1
    out = (data-np.min(data))*bit/(np.max(data)-np.min(data))
    out = out.astype('uint'+str(bitnum))
    return out
    

def imrescale_interactive(data, bitnum=8):
    """
    increases brightness/contrast by user-defined value and returns it as int array
    
    Parameters
    __________
    data : ndarray 
        input image data 3D array
    bitnum: int 
        number of bits to save. by default is 8 bit
    """
    
    Flag = True
    bit = 2**bitnum-1
    
    while Flag:
        #Amp is the input from user
        Amp = float(input("Please enter amplification factor: "))
        delta = Amp * sqrt(mean(square(data[0,:,:]))) 
        test = (data[0,:,:] - mean(data[0,:,:])+delta)*bit//(2*delta)
        np.clip(test, 0, bit, test)
        show(test)
        plt.show()
        
        '''
        plt.figure(num=None, figsize=(12, 14), facecolor='w', edgecolor='k')
        plt.imshow(test, cmap='Greys_r')
        plt.show()
        '''
        #check if the user is satisfied
        flag2 = int(input("Type '1' if ok or '0' to redo the normalization:  "))
        if flag2 == 1:
            data = (data - mean(data)+delta)*bit//(2*delta)                        # dynamical range for the substraction - type 1.65 if you want to leave central 90% of signal range, type 2 for 90% and 2.6 for 99%
            np.clip(data, 0, bit, data)                                        # makes all the pixels that are bigger that 255 equal 255 and that are less 0 to be 0 (example is for 8 bit)
            data = np.array(np.round(data),dtype = 'uint'+str(bitnum))                           # Round values in array and cast as whatever-bit integer
        
            Flag = False
    return data
    

def SSIM(): 
    """
    calculate a structural similarity index as described in
    https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
    
    Parameters
    __________
    data : 2d array 
        input image 
    flatfield : 2d array
        image to compare with
        
        
        
        
    bitnum: int 
        number of bits. by default is 8 bit
    """
    

    
    
def make_video(stack, video_name='video_stack.avi', path=os.getcwd()):

    """
    Makes a JPG video out of the image stack
    
    Parameters
    __________
    stack : ndarray
        stack of images where the 0 axis corresponds to the image index
    video_name : str, optional
        the name of the output file
    path : str, optional
        path where the file should be saved
    """
    
    video = cv2.VideoWriter(path+'/'+video_name, cv2.VideoWriter_fourcc('M','J','P','G'), 15, (stack.shape[1], stack.shape[2]))
    for i in range(stack.shape[0]):
        file = stack[i,:,:]
        video.write(cv2.merge([file,file,file]))
    video.release()


