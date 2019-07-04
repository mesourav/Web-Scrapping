#!/usr/bin/env python
# coding: utf-8

# In[6]:


from bs4 import BeautifulSoup as soup
import requests
from urllib.request import urlopen


# In[7]:

myURL = "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=901&ref_=adv_nxt"


# In[8]:


#Opening up connection, grabbing the page
uClient = urlopen(myURL)
page_html = uClient.read()
uClient.close()


# In[9]:


# HTML Parsing
page_soup = soup(page_html, "lxml")


# In[14]:


containers = page_soup.select("div.lister-list")


# In[18]:


container = containers[0]


# In[21]:


lister = container.find_all(name="div", attrs={"class":"lister-item mode-advanced"})


# In[36]:


lister[0]
lister[0].find_all("a")[1].text # title


# In[67]:


cast_zero = lister[0].find_all("a")[13:] # cast


# In[68]:


# for c in cast_zero:
    # print(c.text)


# In[49]:


lister[0]
lister[0].find("strong").text # Ratings


# In[54]:


lister[0]
lister[0].find("span", {"class":"lister-item-year text-muted unbold"}).text.strip("()") # year


# In[71]:


with open("IMDB.csv", "a") as f:
    headers = "Title, Year, Rating, Cast\n"
    f.write(headers)
    for l in lister:
        title = l.find_all("a")[1].text
        year = l.find("span", {"class":"lister-item-year text-muted unbold"}).text.strip("()")
        rating = l.find("strong").text
        cast_list = l.find_all("a")[13:]
        cast = [c.text + ";" for c in cast_list]
        cast = " ".join(cast)
        f.write(title.replace(",", "|") + "," + year + "," + rating + "," + cast + "\n")


# In[ ]:




