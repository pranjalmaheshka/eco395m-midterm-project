#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


response = requests.get("https://scholar.google.com/citations?user=wR_HkJgAAAAJ&hl=en&oi=ao")


# In[4]:


html = response.text


# In[5]:


soup = BeautifulSoup(html, "html.parser")


# In[6]:


indexes = soup.find_all("td", "gsc_rsb_std")


# In[7]:


h_index = indexes[2].string


# In[8]:


i10_index = indexes[4].string


# In[9]:


citations = indexes[0].string


# In[10]:


h_index


# In[11]:


i10_index


# In[12]:


citations


# In[13]:





# In[ ]:




