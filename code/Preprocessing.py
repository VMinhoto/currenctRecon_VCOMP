#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[38]:


img = cv2.imread('../dataset/currencyStandard/currencyDB_mediumResolution/10eu_front.jpg',0)
#img = cv2.imread('../dataset/testDB/500-500-500.jpg',0)


# In[39]:


plt.imshow(img,cmap='gray')
plt.show()


# In[40]:


blur = cv2.bilateralFilter(img,8,16,12)
plt.imshow(blur,cmap='gray')
plt.show()


# In[41]:


#bwimg = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cll = clahe.apply(blur)
plt.imshow(cll,cmap='gray')
plt.show()


# In[42]:


cv2.imwrite('preprocessed.png',cll)


# In[ ]:




