#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm


# In[34]:


df_train = pd.read_csv('C:/Users/DELL/Downloads/weather_dataset.csv')

df_train *= 1 # make true/false -> 1/0
print(df_train)
#slicing
x=df_train.iloc[0:60, 0:5]
print(df_train)


# In[37]:


df_train['RAIN'].describe()


# In[38]:


#histogram
df_train['RAIN'].plot(kind="hist")


# In[39]:


sns.distplot(df_train['RAIN'], fit = norm)


# In[40]:


#check skewness
df_train['RAIN'].skew()


# In[41]:


df_train['RAIN'] = np.log1p(df_train['RAIN'])
sns.distplot(df_train['RAIN'], fit = norm)


# In[42]:


total = df_train.isnull().sum().sort_values(ascending=False)
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data[missing_data['Total'] > 0]
print(total)
print(percent)


# In[43]:


## BIVARIATE ANALYSIS
df_train.hist(bins=50, figsize=(30,20));


# In[45]:


var = 'RAIN'
data = pd.concat([df_train['PRCP'], df_train[var]], axis=1)
data.plot.scatter(x=var, y='PRCP')


# In[49]:


var = 'RAIN'
data = pd.concat([df_train['PRCP'], df_train[var]], axis=1)
f, ax = plt.subplots(figsize=(16, 8))
fig = sns.boxplot(x=var, y="PRCP", data=data)
plt.xticks(rotation=90);


# In[50]:


sns.set()
#cols = ['PredictLabel1', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8']
cols = ['RAIN', 'TMIN']
sns.pairplot(df_train[cols], size = 2.5)
plt.show();


# In[51]:


#Multivariate Analysis
corrmat = df_train.corr(method='spearman')
f, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(corrmat, ax=ax, cmap="YlGnBu", linewidths=0.1)


# In[52]:


#correlation matrix
corrmat = df_train.corr(method='spearman')
cg = sns.clustermap(corrmat, cmap="YlGnBu", linewidths=0.1);
plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
cg


# In[53]:


k=30
cols = corrmat.nlargest(k, 'RAIN')['RAIN'].index
cm = np.corrcoef(df_train[cols].values.T)
f, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(cm, ax=ax, cmap="YlGnBu", linewidths=0.1, yticklabels=cols.values, xticklabels=cols.values)


# In[ ]:




