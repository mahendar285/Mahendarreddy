#!/usr/bin/env python
# coding: utf-8

# In[31]:


def mean_value(list):
    t = sum(list)
    avg_value = t/len(list)
    return avg_value
list = [10,20,30,40,50,60]
mean_value(list)


# In[79]:


from collections import Counter
def find_mode(s):
    count = Counter(s) 
    return count 
    result = find_mode([2, 4, 4, 2, 3]) 
    print(result)


# In[93]:


def find_mode(s):
    count = Counter(s)
    max_count = max(count.values())
    mode = [key for key, value in count.items() 
            if value == max_count]
    return mode
result = find_mode([2, 4, 4, 2, 3])
print(result)


# In[99]:


def mode_value(l):
    s = set(l)
    d ={}
    for x in s:
        d[x]=l.count(x)
    return(max(d.values()))
l = ["m","n","m","n"]
mode_value(l)


# In[101]:


def mode_value(l):
    s = set(l)
    d ={}
    for x in s:
        d[x]=l.count(x)
    m = max(d.values())
    for k in d.keys():
        if d[k] == m:
            return k
l = ["m","n","m","n"]
mode_value(l)


# In[105]:


def mode_value(l):
    s = set(l)
    d ={}
    for x in s:
        d[x]=l.count(x)
    m = max(d.values())
    for k in d.keys():
        if d[k] == m:
            return k
l = [2, 4, 4, 2, 3]
mode_value(l)


# In[ ]:




