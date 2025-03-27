#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
a=np.array([[10,20,30],[50,80,70]])
print(a)
print("Array created:",a)


# In[10]:


import numpy as np
c=np.zeros((3,5))
print("\n Array with all zeroes:\n",c)


# In[12]:


import numpy as np
d=np.random.random((3,3))
print("\nRandom values:\n",d)


# In[13]:


import numpy as np
e=np.arange(0,40,5)
print("\n A sequence array with step5:\n",e)


# In[15]:


import numpy as np
f=np.full((3,4),(7))
print(f)


# In[18]:


arr=np.array(([1,2,3,4],[10,20,30,40],[11,22,33,44]))
newarr=arr.reshape(4,3)
print("\n original array:\n",arr)
print("\n reshaped array:\n",newarr)


# In[22]:


arr=np.array(([1,2,3,4],[10,20,30,40],[11,22,33,44]))
newtype=arr.astype('f')
print("\n converted array element:\n",newtype)
print("converted array tpe:",newtype)

