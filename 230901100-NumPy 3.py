#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
arr=np.array([0,1,2,2,7,8,9])
x=np.searchsorted(arr,8,side='right')
print(x)


# In[6]:


arr=np.array([9,5,2,7,6,4])
print(np.sort(arr))


# In[7]:


arr=np.array([[7,4,9],[9,1,4]])
print(np.sort(arr))


# In[14]:


arr=np.array([31,78,68,58])
X=[False,True,True,False]
newarr=arr[X]
print(X)
print(newarr)


# In[16]:


arr=np.array([31,78,68,88])
filter_arr=arr>70
newarr=arr[Filter_arr]
print(filter_arr)
print(newarr)


# In[17]:


arr1=[20,40,50,70,10]
arr2=[6,2,9,7,1]
a=np.array(arr1)
b=np.array(arr2)
print(a)
print(b)
print(a+b)



# In[18]:


arr1=[20,40,50,70,10]
arr2=[6,2,9,7,1]
a=np.array(arr1)
b=np.array(arr2)
print(a)
print(b)
print(a-b)


# In[19]:


arr1=[20,40,50,70,10]
arr2=[6,2,9,7,1]
a=np.array(arr1)
b=np.array(arr2)
print(a)
print(b)
print(a*b)


# In[20]:


arr1=[20,40,50,70,10]
arr2=[6,2,9,7,1]
a=np.array(arr1)
b=np.array(arr2)
print(a)
print(b)
print(a/b)


# In[21]:


arr1=[20,40,50,70,10]
arr2=[6,2,9,7,1]
a=np.array(arr1)
b=np.array(arr2)
print(a.dot(b))
sdr=3
print("scalarvalue:",sdr)
print("array:",a)
print("result:",a*sdr)


# In[22]:


a=np.array([[10,20],[30,40]])
b=np.array([[3,7],[5,9]])
print(a%b)


# In[1]:


def my_func(x,y):
    if x>y:
        return x-y
    else:
        return x+y
    arr1=[10,7,2]
    arr2=[6,5,3]
    vect_func=np.vectorize(my_func)
    print("array1:",arr1)
    print("array2:",arr2)
    print("result:",vect_func(arr1,arr2))


# In[ ]:




