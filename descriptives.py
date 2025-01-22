#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[14]:


df = pd.read_excel("universities.xlsx")
df


# In[16]:


df.describe()


# In[18]:


np.mean(df["SAT"])


# In[20]:


np.median(df["SAT"])


# In[22]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[23]:


plt.figure(figsize=(6,3))
plt.title("Acceptance Ratio")
plt.hist(df["Accept"])


# In[26]:


sns.histplot(df["Accept"])


# In[34]:


sns.histplot(df["Accept"], kde =True)


# In[ ]:




