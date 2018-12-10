#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 01_print_anker.py
from bs4 import BeautifulSoup

html_str = ''
with open('./unagi-tokyo.html', 'r') as f:
    html_str = f.read()
    
soup = BeautifulSoup(html_str, 'html.parser')
for anker in soup.find_all('a'):
    print(anker.text)
