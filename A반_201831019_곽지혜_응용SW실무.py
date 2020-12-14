#!/usr/bin/env python
# coding: utf-8

# In[41]:


# 201831019_ 곽지혜

from bs4 import BeautifulSoup
from urllib.request import urlopen
from tqdm import tqdm_notebook
import pandas as pd
import urllib


# In[42]:


import requests
from bs4 import BeautifulSoup
movie_name=[]
movie_point=[]
naverURL = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20201201"
naverpage = urlopen(naverURL)
soup = BeautifulSoup(naverpage, "html.parser")
end = len(soup.find_all("td","point"))


# In[43]:


print (soup.find_all(string='9.40'))


# In[44]:


print (soup.find_all(string='소년시절의 너'))


# In[37]:


# 영화제목
movie_title = soup.find_all("div","tit5")

movie_name = [movie_title[i].text.strip() for i in range(len(movie_title))]
movie_name


# In[38]:


# 평점
points = soup.find_all("td","point")
movie_point = [points[i].text for i in range(len(points))]
movie_point


# In[39]:


movie_name = []
movie_point = []

movie_name.extend([soup.find_all("div","tit5")[n].a.string for n in range(end)])
movie_point.extend([soup.find_all("td","point")[n].string for n in range(end)])


# In[40]:


# 결과화면 출력
data = {"name": movie_name, "point":movie_point}
data = pd.DataFrame(data)
data

