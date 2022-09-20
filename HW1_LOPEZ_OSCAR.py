#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers=list(range(30,65,5))
print(numbers)


# In[2]:


numbers[::-1]


# In[3]:


numbers.append(65)


# In[4]:


numbers


# In[5]:


numbers[::-1]


# In[6]:


list1=[]
print(list1)


# In[7]:


list1.append(1)


# In[8]:


list1.append(2)


# In[9]:


list1.append(3)


# In[10]:


list1.append(4)


# In[11]:


list1.append(5)


# In[12]:


list1.append(6)


# In[13]:


list1.append(7)


# In[14]:


list1.append(8)


# In[15]:


list1.append(9)


# In[16]:


list1.append(10)


# In[17]:


list1.append(11)


# In[18]:


list1.append(12)


# In[19]:


list1.append(13)


# In[20]:


list1.append(14)


# In[21]:


list1.append(15)


# In[22]:


list1.append(16)


# In[23]:


list1.append(17)


# In[24]:


list1.append(18)


# In[25]:


list1.append(19)


# In[26]:


list1.append(20)


# In[27]:


print(list1)


# In[28]:


list1.remove(1)


# In[29]:


print(list1)


# In[30]:


print(len(list1))
print(max(list1))
print(min(list1))


# In[31]:


total=sum(list1)


# In[32]:


print(total)


# In[33]:


weather={"Sunny":"play","Rainy":"watch TV","Cloudy":"walk"}
print(weather)


# In[34]:


for w in weather:
    print("When",w,"let us",weather[w])


# In[35]:


weather.update({"snowy":"ski"})


# In[36]:


for w in weather:
    print("When",w,"let us",weather[w])


# In[ ]:




