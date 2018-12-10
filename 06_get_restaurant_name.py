#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 06_get_restaurant_name.py
import re
from bs4 import BeautifulSoup
import requests

def get_restaurant_name(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    content = soup.find('div', class_='entry-content post-content')
    anker = None
    for anker in content.find('a', target="_blank"):
        if 'rel' in anker:
            continue
    if anker:
        print(anker)
        return anker.text
    else:
        return ''
    
html_str = ''
with open('./unagi-tokyo.html', 'r') as f:
    html_str = f.read()
    
soup = BeautifulSoup(html_str, 'html.parser')
content = soup.find('div', id='content', class_='content')
for idx, anker in enumerate(content.find_all('a')):
    href_str = str(anker.get('href'))
    if re.match(r'http://unagi-daisuki.com/post-\d+', href_str):
        name = get_restaurant_name(href_str)
        print(idx, name)
        exit()
