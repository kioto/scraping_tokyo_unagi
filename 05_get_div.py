#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 05_print_anker.py
import re
from bs4 import BeautifulSoup

html_str = ''
with open('./unagi-tokyo.html', 'r') as f:
    html_str = f.read()
    
soup = BeautifulSoup(html_str, 'html.parser')
content = soup.find('div', id='content', class_='content')
for idx, anker in enumerate(content.find_all('a')):
    href_str = str(anker.get('href'))
    if re.match(r'http://unagi-daisuki.com/post-\d+', href_str):
        print(idx, href_str, anker.text)
