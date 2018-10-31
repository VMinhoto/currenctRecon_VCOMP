#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[9]:


img = cv2.imread('preprocessed.png',0)
#img2 = cv2.imread('10_test_preprocessed.png',0)
img2 = cv2.imread('10_test1_preprocessed.png',0)


# In[14]:


sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3=cv2.drawMatchesKnn(img,kp1,img2,kp2,good,None,flags=2)

plt.imshow(img3),plt.show()


#kp = sift.detect(img,None)

#img2 = cv2.drawKeypoints(img,kp,None,(0,255,0),4)
#img2=cv2.drawKeypoints(img,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#plt.imshow(img2),plt.show()
#cv2.imwrite('sift_keypoints.jpg',img2)


# In[7]:


""" surf = cv2.xfeatures2d.SURF_create(5000)
kp, des = surf.detectAndCompute(img,None)
#kp = sift.detect(img,None)

img2 = cv2.drawKeypoints(img,kp,None,(0,255,0),4)
#img2=cv2.drawKeypoints(img,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img2),plt.show()
cv2.imwrite('surf_keypoints.jpg',img2)


# In[1]:


surf = cv2.xfeatures2d.SURF_create()
kp1, des1 = surf.detectAndCompute(img,None)
kp2, des2 = surf.detectAndCompute(img,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
cv2.drawMatchesKnn(img,kp1,img2,kp2,good,img3,flags=2)
plt.imshow(img3),plt.show()

 """
# In[ ]:




