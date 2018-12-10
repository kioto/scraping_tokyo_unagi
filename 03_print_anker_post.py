#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 03_print_anker_post.py
from bs4 import BeautifulSoup

html_str = ''
with open('./unagi-tokyo.html', 'r') as f:
    html_str = f.read()
    
soup = BeautifulSoup(html_str, 'html.parser')
for idx, anker in enumerate(soup.find_all('a')):
    href_str = str(anker.get('href'))
    if 'http://unagi-daisuki.com/post-' in href_str:
        print(idx, href_str, anker.text)
