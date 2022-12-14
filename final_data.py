#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:47:35 2022

@author: jihoonlee
"""

import geopandas
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import datetime
import re
from collections import Counter
import matplotlib.dates as mdates
import zipfile
from dash import Dash, html, dcc
import plotly.express as px



#dataframe from data scraping
whiskey = pd.read_csv("/Users/jihoonlee/Desktop/whiskey.csv")
wname = list(whiskey['name'])
whiskey['proof'] = [item.split(' ', -1)[-1] for item in wname]

vodka = pd.read_csv("/Users/jihoonlee/Desktop/vodka.csv")
vodka = vodka[vodka['name'].str.contains('SOJU')==False]
vname = list(vodka['name'])
vodka['proof'] = [item.split(' ', -1)[-1] for item in vname]

tequila = pd.read_csv("/Users/jihoonlee/Desktop/tequila.csv")
tname = list(tequila['name'])
tequila['proof'] = [item.split(' ', -1)[-1] for item in tname]

rum = pd.read_csv("/Users/jihoonlee/Desktop/rum.csv")
rum = rum[rum['name'].str.contains('SOJU')==False]
rname = list(rum['name'])
rum['proof'] = [item.split(' ', -1)[-1] for item in rname]
rum = rum[rum['proof'].str.contains('RUM')==False]

gin = pd.read_csv("/Users/jihoonlee/Desktop/gin.csv")
gname = list(gin['name'])
gin['proof'] = [item.split(' ', -1)[-1] for item in gname]
gin = gin[gin['proof'].str.contains('FINLAND')==False]

#data merging
ac = pd.concat([whiskey, vodka, tequila, rum, gin])
ac = ac.drop(["Unnamed: 0"], axis = 1)
ac = ac.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
ac = ac.drop(["index"], axis = 1)
ac['index'] = ac.index


rownumber = []
for row in ac['index']:
    if row < 153.0 :    rownumber.append('Whiskey')
    elif row < 380.0:   rownumber.append('Vodka')
    elif row < 502.0:  rownumber.append('Tequila')
    elif row < 614.0:  rownumber.append('Rum')

    else:           rownumber.append('Gin')

ac['type'] = rownumber
ac = ac.drop(["index"], axis = 1)

ac.to_csv('final_dataframe.csv')

df = pd.read_csv('/Users/jihoonlee/Desktop/final_dataframe.csv')
df = df.drop('Unnamed: 0', axis=1)
df['price'] = df['price'].str.replace("$", "")
df['price'] = df['price'].astype(float)

df.to_csv('true_final_dataframe.csv', index=False)


