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



df = pd.read_csv('/Users/jihoonlee/Desktop/final_dataframe.csv')


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

#fig = px.bar(df, x=df['name'], y=df['price'])



app.layout = html.Div([
    html.Div([
        html.H1('Set Up A Home Bar Dashboard',
            style={'textAlign' : 'center'}),
        html.P(children='''
        MA 705 Individual Project: JiHoon Lee
        '''),
        html.Div(generate_table(df),id="table_div",
             style={'width' : '50%', 'float' : 'right'}),
        dcc.Markdown('''
        ### What do you need to set up a home bar?
        ###### If you want to set up a home bar and don't know where to start, This
        ###### dashboard will be a great place to start. This dashboard summarizes 
        ###### over 500 liquor options that are commonly used for making cocktails. 
        ###### The dataset was obtained from the Blanchards website in Allston. 
        ### How to use this dashboard.
        ###### Pick a liquor of your choice and a size you are looking for. The graph 
        ###### will generate options that align with your interest.
        ''',
        #html.A('Blanchards Website', href='https://blanchards.net'),
    
        
                     )
    ]),
    html.Div([
            html.Div([
            html.H6('Liquor'),
            dcc.Dropdown(
                df['type'].unique(),
                'Whiskey',
                id='xaxis-column'
            ),
            html.H6('Size'),
            dcc.Dropdown(
                df['size'].unique(),
                '1 L',
                id='xaxis-type',
            ),
        ], style={'width': '48%', 'display': 'inline-block'}),

            
    ]),

    dcc.Graph(id='indicator-graphic'),
    
    
   
])


@app.callback(
    Output(component_id = 'xaxis-type', component_property = "options"),
    [
    Input(component_id = 'xaxis-column', component_property = "value"),
    ])



def update_dropdown(xaxis_column_name):
    dff = df[df['type'] == xaxis_column_name]
    return [{'label': i, 'value': i} for i in dff['size'].unique()]
    

    
@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('xaxis-type', 'value'))
   
def update_graph(xaxis_column_name, xaxis_type):
    dff = df[df['type'] == xaxis_column_name]
   


    fig = px.bar(dff, x=dff[dff['size'] == xaxis_type]['name'], 
                 y= dff[dff['size'] == xaxis_type]['price'])
 
    
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    fig.update_xaxes(
        tickangle = 45,
        title_text = "Product Name",
        title_font = {"size": 20},
        title_standoff = 25)

    fig.update_yaxes(
        title_text = "Price ($)",
        title_standoff = 25)


    return fig

@app.callback(
    Output('table_div', 'children'),
    Input('xaxis-column', 'value'),
    Input('xaxis-type', 'value'))
   

def update_table(xaxis_column_name, xaxis_type):
   df2 = df[df['type'] == xaxis_column_name]
   df3 = df2[df2['size'] == xaxis_type]
   return generate_table(df3)


if __name__ == '__main__':
    app.run_server(debug=True)
    
    
