#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import stats 


# In[3]:


stats.norm.cdf(680,loc=711,scale=29)


# In[4]:


stats.norm.cdf(740,loc=711,scale=29)


# In[5]:


stats.norm.cdf(697,loc=711,scale=29)


# 0.8413447460685429 - 0.31463356742704107

# ## Stock Market 

# ### Probability of making more than 2% gain in Glaxo

# In[30]:


import pandas as pd
import seaborn as sns


# In[11]:


bemldf=pd.read_csv(r"C:\Jagadeeswari\Data Science\CW\03-09-2020\BEML.csv")


# In[12]:


bemldf.head()


# In[13]:


bemldf=bemldf[['Date','Close']]


# In[14]:


bemldf


# In[15]:


bemldf=bemldf.set_index(pd.DatetimeIndex(bemldf['Date']))


# In[16]:


bemldf


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sn
get_ipython().run_line_magic('matplotlib', 'inline')


# In[20]:


plt.plot(bemldf.Close);
plt.xlabel('Time');
plt.ylabel('Close Price');


# In[47]:


bemldf['gain'] = bemldf.Close.pct_change(periods = 1)


# In[48]:


bemldf.head(15)


# In[49]:



bemldf=bemldf.dropna()
bemldf


# In[51]:


plt.figure(figsize=(8,8));
plt.plot(bemldf.index,bemldf.gain)
plt.xlabel('Time');
plt.ylabel('gain');


# In[36]:


sns.distplot(bemldf.gain,label='BEML')


# In[38]:


print('Mean:', round(bemldf.gain.mean(),4))


# In[39]:


print('Standard Deviation:', round(bemldf.gain.std(),4))


# ## #Probability of making 2% loss or higher in BEML stock

# In[42]:


stats.norm.cdf(-0.02,loc=bemldf.gain.mean(),scale=bemldf.gain.std())


# ## #Probability of making 2% gain or higher in BEML stock

# In[43]:


1-stats.norm.cdf(0.02,loc=bemldf.gain.mean(),scale=bemldf.gain.std())


# In[ ]:




