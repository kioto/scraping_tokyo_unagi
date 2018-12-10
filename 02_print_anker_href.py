#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 02_print_anker_href.py
from bs4 import BeautifulSoup

html_str = ''
with open('./unagi-tokyo.html', 'r') as f:
    html_str = f.read()
    
soup = BeautifulSoup(html_str, 'html.parser')
for idx, anker in enumerate(soup.find_all('a')):
    href = anker.get('href')
    print(idx, str(href), anker.text)
