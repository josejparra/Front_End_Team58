from flask import Flask, render_template#, request, redirect, url_for, flash

import pandas as pd

from dash import Dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

urlData='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
colsData=["sepal_length_cm", "sepal_width_cm", "petal_length_cm", "petal_width_cm"]
    
iris_df = pd.read_csv(urlData, names=colsData+["class"], header=None)
iris_df["class"] = iris_df["class"].astype("category")





server = Flask( __name__ )
dash_app = Dash(__name__, server = server, url_base_pathname='/dash/' )
dash_app2 = Dash(__name__, server = server, url_base_pathname='/dash2/' )

dash_app2.layout = html.Div([
    html.H1('Hola Mundo'),
    ])

dash_app.layout = html.Div([
	html.H1('Flower Iris'),
	html.Div([
		dcc.Dropdown(
		    id='ddl_x',
		    options=[{'label': i, 'value': i} for i in colsData],
		    value=colsData[0],
		    style={'width':'50%'}
		),
		dcc.Dropdown(
		    id='ddl_y',
		    options=[{'label': i, 'value': i} for i in colsData],
		    value=colsData[1],
		    style={'width':'50%'}
		),
		],style={'width':'100%','display':'inline-block'}),
		html.Div([
			dcc.Graph(id='graph1') 
		],style={'width':'100%','display':'inline-block'})	
	])

@dash_app.callback(
    Output(component_id='graph1', component_property='figure'),
    [
        Input(component_id='ddl_x', component_property='value'),
        Input(component_id='ddl_y', component_property='value')
    ]
)
def update_graph1(ddl_x_value, ddl_y_value):
    figure={
        'data': [
            go.Scatter(
                x=iris_df[iris_df['class'] == cls][ddl_x_value],
                y=iris_df[iris_df['class'] == cls][ddl_y_value],
                mode='markers',
                marker={ 'size': 15 },
                name=cls
            ) for cls in iris_df['class'].unique()
        ],
        'layout': 
            go.Layout(
                height= 350,
                hovermode= 'closest',
                title=go.layout.Title(text='Dash Interactive Data Visualization',xref='paper', x=0)
            )
        
    }
    return figure




@server.route('/dash/')
def render_dashboard():
	return dash_app.index()


@server.route('/dash2/')
def render_dashboard2():
    return dash_app2.index()


@server.route('/')
def index():
    return render_template('index.html' )

@server.route('/predict')
def predict():
    return render_template('predict.html' )

@server.route('/dashboard')
def view_dashboard():
    return render_template( 'dashboard.html' )

@server.route('/about')
def view_about():
    return render_template( 'about.html' )

if __name__ == '__main__':
    server.run( port=5001, debug = True )