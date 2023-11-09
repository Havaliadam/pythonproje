# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 18:02:59 2023

@author: Acer
"""

import feedparser

url="https://www.cnnturk.com/turkiye/"
haberler=feedparser.parse(url)


i=0
for haber in haberler.entries:
    i+=1
    print(i)
    print(haber.title)
    print(haber.link)
    print(haber.summary)
    print("\n")