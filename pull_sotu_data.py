
# coding: utf-8

# In[ ]:

import os
import pickle
import datetime as dt
import pandas as pd
import numpy as np
import bs4 as bs
import requests
import re
from nltk.corpus import stopwords
import nltk
import string

os.listdir()


# In[2]:

os.listdir()
os.chdir("cs657")
os.listdir()


# In[ ]:

def pull_sotu_htmls(url='http://stateoftheunion.onetwothree.net/texts/index.html'):
    sotu_file = urllib2.urlopen(url)
    html = sotu_file.read()
    sotu_file.close()
    
    soup = bs.BeautifulSoup(resp.t)


# In[14]:

base_url='http://stateoftheunion.onetwothree.net/texts/'
url = base_url+'index.html'
links = []
hrefs = []
sotu_file = requests.get(url)
soup = bs.BeautifulSoup(sotu_file.text, 'lxml')
soup_list = soup.findAll('a')[6:]
for link in soup_list:
    # hrefs.append(link.get('href')[:7])
    links.append((link.get('href')[:7], base_url+link.get('href')))


# In[12]:

# re_pattern = '\d{8}'
# test = soup_list[0].get('href')
# # print(re.search(re_pattern, test))
# # re.search(re_pattern, test)
# count = 0 
# for link in soup_list:
#     print(count)
#     href = link.get('href')
#     print(href[:7])
#     try:
#         match = re.search(re_pattern, href)
#         if match:
#             links.append(base_url+link)
#     except TypeError as e:
#         print("excepted{}".format(href))
#         print(e)
#         continue
# 
# print(links)


# In[38]:

print(links)
# print(hrefs[:5])


# In[32]:

cachedstopwords = stopwords.words("english")
cachedstopwords
# punction = '(),.<:!/;'
string.punctuation


# In[27]:

# nltk.download()


# In[39]:

# os.chdir('addresses')
punc = string.punctuation
nltk_stopwords = stopwords.words("english")
for tup in links:
    # print(link)
    date = tup[0]
    link = tup[1]
    address_file = requests.get(link)
    address_soup = bs.BeautifulSoup(address_file.text, 'lxml')
    # list of paragraphs
    sotu_list = address_soup.findAll('p')
    # print(sotu_list)
    sotu = ' '
    # for line in address
    for line in sotu_list: 
        # these three steps are inefficient and could be compressed
        # check each character and remove all punctuation
        cleaned_s = ' ' + ''.join(c.lower() for c in line.text if c not in punc) #inefficient
        stopped_s = ' ' + ' '.join(word for word in cleaned_s.split() if word not in nltk_stopwords) #inefficient
        sotu += stopped_s.replace('\n', ' ')
    sotu = sotu.strip()
    with open(str(date) +'.txt', "w") as f:
        f.write(sotu)


# In[21]:

len(links) + 1790

