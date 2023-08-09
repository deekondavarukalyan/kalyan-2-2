#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


# In[1]:


list= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lst = len(list) 
for i in range(0, lst): 
           
    for j in range(0, lst-i-1): 
        if (list[j][-1] > list[j + 1][-1]): 
            temp = list[j] 
            list[j]= list[j + 1] 
            list[j + 1]= temp 
print(list)


# In[ ]:


#Sample Output : {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}


# In[2]:


sample_dict={}
for i in range(97,123,1):
    sample_dict[chr(i)]=i
print(sample_dict)


# In[ ]:




