#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
from PIL import Image as Im


# In[2]:

#give image path here
im=cv2.imread(r"C:\Users\HP\Downloads\Gris.jpeg")

#give message to encrypt here
text="weewoo"


# In[3]:


#For cleaning last bit of image
def cleanlastbit(im):
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if(im[i][j][0]%2!=0):
                im[i][j][0]-=1
    return im


# In[4]:


#String to binary
def stringtobin(text):
    res = ''.join(format(ord(i), '07b') for i in text)
    return res


# In[5]:


#Read last bit into binary string
def readlastbit(im):
    binary=""
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            binary=binary+str(im[i][j][0]%2)
    return binary


# In[6]:


#Encryption
def insertmessage(im,message):
    im=cleanlastbit(im)
    message=stringtobin(message)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if((i*im.shape[0]+j)==len(message)):
                return im
            if int(message[i*im.shape[0]+j])==1:
                im[i][j][0]+=1
    return im


# In[7]:


#Decryption

def decryptmessage(im):
    bin_data=readlastbit(im)
    str_data =' '
    for i in range(0, len(bin_data), 7):
        temp_data = bin_data[i:i + 7]
        if(temp_data=="0000000"):
            break
        decimal_data = int(temp_data,2)
        str_data = str_data + chr(decimal_data)
    print("The message is:",str_data)


# In[8]:


#TESTING TAB
im=insertmessage(im,text)
cv2.imwrite("EncryptedImage.png",im)
decryptmessage(im)


