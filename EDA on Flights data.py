#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


df=pd.read_csv("C:\\Jagadeeswari\\Data Science\\HW\\my HW\\flights.csv")


# In[6]:


df.shape


# ## find the names of the columns

# In[9]:


df.head(0)


# In[10]:


df.head()


# ## Find the types of columns in the data frame

# In[13]:


df.dtypes


# In[14]:


df.describe()


# In[16]:


df.dropna()


# ## Average departure delay of each airline

# In[35]:


print(df.groupby('AIRLINE')[['DEP_DELAY']].mean())


# ## Average Arrival delay of each airline

# In[36]:


print(df.groupby('AIRLINE')[['ARR_DELAY']].mean())


# ## Find the number of flights which are diverted in each month

# In[60]:


print(df.groupby('MONTH')[['DIVERTED']].sum())


# In[ ]:




