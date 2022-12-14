#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 18:16:11 2022

@author: jihoonlee
"""



import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=stylesheet)

server = app.server

rawurl = 'https://raw.githubusercontent.com/jihoonlee-bentley/finalproject/main/data.csv'

df = pd.read_csv(rawurl)


def generate_table(df, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), max_rows))
        ])
    ])




app.layout = html.Div([
    html.Div([
        html.H1('Set Up A Home Bar Dashboard',
            style={'textAlign' : 'center'}),
        html.P(children='''
        MA 705 Individual Project: JiHoon Lee
        ''')])
])



if __name__ == '__main__':
    app.run_server(debug=True)
    
    
