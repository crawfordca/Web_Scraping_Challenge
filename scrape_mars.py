#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
import requests as req
from splinter import Browser
from selenium import webdriver
import re


# In[ ]:


executable_path = {"executable_path": "C:\Users\revel\Downloads\chromedriver_win32\chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless = False)


# In[ ]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[ ]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# Collect the latest News Title and Paragraph Text
news_title = soup.find('div', class_='content_title').find('a').text
news_p = soup.find('div', class_='article_teaser_body').text

# Display scrapped data 
print(news_title)
print(news_p)


# In[ ]:


#MarsImages
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(featured_image_url)


# In[ ]:


html_image = browser.html

bs = BeautifulSoup(html_image, 'html.parser')

image_url  = bs.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

main_url = 'https://www.jpl.nasa.gov'

feature_url = image_url + main_url


feature_url


# In[ ]:


#MarsWeather
html_weather = browser.html
soup = bs(html_weather,"html.parser")

driver = webdriver.Chrome()
driver.get(url_weather)
html = driver.page_source
driver.close()

pattern = re.compile(r'sol')
mars_weather = soup.find('span', text=pattern).text

print(mars_weather)


# In[ ]:


#MarsFacts
mars_facts = "https://space-facts.com/mars/"
tables = pd.read_html(mars_facts)
tables


# In[ ]:


mars_df = tables[0]
mars_df.head()


# In[ ]:


html_table = mars_df.to_html()


# In[ ]:


#MarsHemispheres

hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemi_url)


# In[ ]:




html_hemi = browser.html
bsoup = BeautifulSoup(html_hemi, 'html.parser')


picture = bsoup.find_all('div', class_='item')

hemi_urls = []

hemi_main_url = 'https://astrogeology.usgs.gov'


for p in picture: 
    title = i.find('h3').text
    title = title.replace("Enhanced", "")
    partial_img_url = i.find('a', class_='downloads')['href']
    browser.visit(hemispheres_main_url + partial_img_url)
    partial_img_html = browser.html
    bsoup = BeautifulSoup( partial_img_html, 'html.parser')
    img_url = hemi_main_url + bsoup.find('img', class_='wide-image')['src']
    hemi_urls.append({"title" : title, "img_url" : img_url})
   
    print(hemi_urls)

