#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:53:35 2022

@author: jihoonlee
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

#vodka

productlinks=[]
for x in range(1,21):
    r = requests.get(f'https://shop.blanchards.net/s-10165/c-2/buy-liquor?catId=2&typeId=9&pageNumber={x}')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_='row row-alt')
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(link['href'])
        
        
vodkalist = []
#testlink = 'https://shop.blanchards.net/product/s-10165/p-538771/buy-titos-vodka-80'
for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    data = soup.find('div', class_='product_content_sub')
    for item in data:
        name = soup.find('h1').text.strip()
    
        size = soup.find('span', class_='size_bottle').text.strip()
        price = soup.find('span', class_='no_strike_text_div').text.strip()
    
    vodka = {
        'name':name,
        'size':size,
        'price':price
        }
    vodkalist.append(vodka)

df_vodka = pd.DataFrame(vodkalist)
