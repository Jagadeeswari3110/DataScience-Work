#!/usr/bin/env python
# coding: utf-8

# In[32]:


from scipy import stats


# In[33]:


import numpy as np


# In[34]:


#stats.norm.cdf()


# ##Super market example

# In[35]:


stats.t.cdf(2.23,df=79)


# ## Call center example
# 

# In[36]:


(4-4.0)/(3/np.sqrt(50))


# In[37]:


2*stats.t.cdf(0,df=49)


# ## Salmonella

# In[38]:


import pandas as pd


# In[41]:


import scipy


# In[42]:


data=pd.Series([0.593,0.142,0.329,0.691,0.231,0.793,0.519,0.392,0.418])


# In[44]:


#This gives two tail test p value so divide by 2 to get final p-value
p=scipy.stats.ttest_1samp(data,0.3)[1]
p


# In[45]:


p/2


# ## since p is less than 0.05 we can reject Ho i.e Mu <=0.3. In a way we say that its 2.9% probability  that icrecream is not creating virus

# In[ ]:




