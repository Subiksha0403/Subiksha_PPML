#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.DataFrame()
print(df)


# In[5]:


import pandas as pd
emp=pd.Series(['Dharshan','Sudeep','Sara','Yash','Ravi'])
id=pd.Series([80,90,28,57,49])
frame={'Exp':emp,'ID':id}
result=pd.DataFrame(frame)
print("\nSeries to DataFrame\n")
print(result)


# In[10]:


import pandas as pd
emp=pd.Series(['Dharshan','Sudeep','Sara','Yash','Ravi'])
id=pd.Series([80,90,28,57,49])
frame={'Exp':emp,'ID':id}
result=pd.DataFrame(frame)
print("\n Extracting one column:\n")
print(result['Exp'])


# In[12]:


import pandas as pd
emp=pd.Series(['Dharshan','Sudeep','Sara','Yash','Ravi'])
id=pd.Series([80,90,28,57,49])
frame={'Exp':emp,'ID':id}
result=pd.DataFrame(frame)
print("\n Adding New column:\n")
result['ID']=pd.Series([80,90,28,57,89])
result['age']=pd.Series([29,30,31,33,28])
print(result)


# In[ ]:




