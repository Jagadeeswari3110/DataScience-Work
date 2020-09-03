#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import pandas as pd


# In[4]:


dmd=pd.read_csv("C:\\Jagadeeswari\\Data Science\\HW\\my HW\diamonds.csv")


# In[5]:


dmd.head


# In[6]:


dmd.columns


# In[7]:


dmd.head(5)


# In[8]:


pd.crosstab(dmd.carat,dmd.price).head(5)


# In[9]:


pd.crosstab(dmd.color,dmd.price)


# In[10]:


dmd['color'].value_counts()


# In[12]:


dmd['color'].value_counts().plot(kind='pie')


# In[13]:


import seaborn as sns


# In[15]:


sns.boxplot(x='color',y='price',data=dmd)


# In[16]:


sns.pairplot(dmd.iloc[:,0:4])


# In[21]:


plt.scatter(dmd.color,dmd.depth)


# In[22]:


plt.hist(dmd.color)


# In[ ]:




