#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
slice1=arr[2:6]
print(slice1)


# In[8]:


import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
subarray=arr[0:2,1:3]
print(subarray)
col1=arr[1:0]
print(col1)
row1=arr[0:1]
print(row1)


# In[11]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[1::])


# In[12]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0,1:3])


# In[13]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[2:,2:])


# In[16]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[:,2])


# In[19]:


import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[0])
print(arr[4])
print(arr[-1])
print(arr[1:4])
print(arr[arr>25])
print(arr[[1,3]])


# In[20]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0:3:2])


# In[21]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0::2])


# In[22]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0,0])


# In[24]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[1,2])


# In[1]:


import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
result=np.hstack((arr1,arr2))
print(result)


# In[2]:


result1=np.vstack((arr1,arr2))
print (result1)
result2=np.dstack((arr1,arr2))
print(result2)


# In[6]:


arr1 = np.array([[1, 2],[3, 4]])
arr2 = np.array([[5, 6],[7, 8]])
result = np.hstack((arr1, arr2))                                             
print(result)


# In[7]:


arr=np.array([1,2,3,4,5,6])
result=np.array_split(arr,3)
print(result)


# In[8]:


arr=np.array([[1,2],[3,4],[5,6]])
result=np.array_split(arr,4)
print(result)


# In[ ]:




