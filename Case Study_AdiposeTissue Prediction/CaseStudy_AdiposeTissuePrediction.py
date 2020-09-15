#!/usr/bin/env python
# coding: utf-8

# # Import Data Set

# In[1]:


import pandas as pd
data = pd.read_csv("WC_AT.csv")


# In[2]:


data


# In[3]:


data.info()


# # Correlation

# In[4]:


data.corr()


# In[5]:


import seaborn as sns
sns.distplot(data['Waist'])


# In[6]:


import seaborn as sns
sns.distplot(data['Waist'])


# Fitting a Linear Regression Model

# In[7]:


import statsmodels.formula.api as smf
model = smf.ols("AT~Waist",data = data).fit()


# In[12]:


sns.regplot(x="Waist", y="AT", data=data);


# In[13]:


#Coefficients
model.params


# In[14]:


#t and p-Values
print(model.tvalues, '\n', model.pvalues)    


# In[15]:


#R squared values
(model.rsquared,model.rsquared_adj)


# # Predict for new data point

# In[16]:


#Predict for 200 and 300 daily circulation
newdata=pd.Series([75,35,90])


# In[17]:


newdata


# In[18]:


data_pred=pd.DataFrame(newdata,columns=['Waist'])


# In[19]:


data_pred


# In[20]:


model.predict(data_pred)


# In[22]:


-216+3.45*75


# In[ ]:





# In[ ]:




