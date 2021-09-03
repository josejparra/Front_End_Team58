import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_predial_obs_predicted=pd.read_csv(DATA_PATH.joinpath('multiple_models_predial.csv'), index_col=0,low_memory=False).reset_index()
df_ica_obs_predicted=pd.read_csv(DATA_PATH.joinpath('multiple_models_ica.csv'), index_col=0,low_memory=False).reset_index()

df_predial_out_sample=pd.read_csv(DATA_PATH.joinpath('out_of_sample_predial.csv'), index_col=0,low_memory=False).reset_index()
df_ica_out_sample=pd.read_csv(DATA_PATH.joinpath('out_of_sample_ica.csv'), index_col=0,low_memory=False).reset_index()

graphs_comparison=html.Div(
    className="row",children=[ 
        html.Div(className="col-md-1"),
        html.Div(
            className="col-md-10",style={"padding-left": "15px","align-items": "center"},
            children=[
                html.H4('Model Comparison', style={"textAlign": "center",}),
                html.H5(id='label_comparison',
                children=['The graph shows the behavior of the different models we trained. According to the MSE, the best model to forecast was the ARIMA.'],
                style={"margin-top":"1.5rem"}),
                html.Div([
                    dcc.Dropdown(
                                id="dropdown_comparison_variable",
                                 options=[
                                    {'label': 'Property', 'value': 'Property'},
                                    {'label': 'Business', 'value': 'Business'}
                                ],
                                value='Property',
                                style={'margin':'auto'}
                    )
                ],style={"width": "30%","align-items":"center"}),
                dcc.Graph(id='graph_comparison',config={'displayModeBar': False})
            ]
        ),
        html.Div(className="col-md-1")
    ]
)

graphs_model=html.Div(
    className="row",children=[ 
        html.Div(className="col-md-1"),
        html.Div(
            className="col-md-10",style={"padding-left": "15px","align-items": "center"},
            children=[
                html.H5('Interact with each filter to see how to understand how the forecast behavior for each of the tax categories.'),
                html.H4('Model Forecast', style={"textAlign": "center","margin-top":"1.5rem",}),
                html.H5(id='label_model',children=[],style={"margin-top":"1.5rem"}),
                html.Div([
                    dcc.Dropdown(
                                id="dropdown_model_variable",
                                 options=[
                                    {'label': 'Property', 'value': 'Property'},
                                    {'label': 'Business', 'value': 'Business'}
                                ],
                                value='Property',
                                style={'margin':'auto'}
                    )
                ],style={"width": "30%","align-items":"center"}),
                dcc.Graph(id='graph_model',config={'displayModeBar': False})
            ]
        ),
        html.Div(className="col-md-1")
    ]
)


layout = html.Div([
    html.H2('Predictive models', style={"textAlign": "left"}),
    graphs_model,
    html.P(),
    graphs_comparison
])

@app.callback(
    Output("label_comparison", "children"),
    [
        Input("dropdown_comparison_variable", "value")        
    ],
)

def show_label_comparison(option):
    property='This figure showcases a model comparison in the forecast of property tax revenue from 2016 to 2020 using data fram 2001 to 2015. ARDL model provides a tighter fit, altough all of the models follow the actual value closely. This is because the seasonal pattern in the data is correctly captured in all the models.'
    business='This figure showcases a model comparison in the forecast of business tax revenue from 2016 to 2020 using data from 2001 to 2015. ARIMA model provides the better fit but none of the models is able to replicate the peaks in revenue due to a lack of similar peaks in the past.'
    if option=='Property':
        return property
    else:
        return business

@app.callback(
    Output("graph_comparison", "figure"),
    [
        Input("dropdown_comparison_variable", "value")        
    ],
)

def show_comparison(option):
    if option=='Property':
        df_obs_predicted=df_predial_obs_predicted

        fig = px.line(df_obs_predicted,
                    x="fecha",
                    y=["Real tax payments","Sarima forecast","ARDL forecast"], 
                    title="Model comparison for "+ option +" tax",
                    labels={"value":"Tax revenue COP (Millions)","fecha":"Date","variable":"Model"},
                    color_discrete_sequence=px.colors.qualitative.T10,
                    )
    else:
        df_obs_predicted=df_ica_obs_predicted

        fig = px.line(df_obs_predicted,
                x="fecha",
                y=["Real tax payments","Sarima forecast","ARDL forecast","RNN forecast","DNN forecast"], 
                title="Model comparison for "+ option +" tax",
                labels={"value":"Tax revenue COP (Millions)","fecha":"Date","variable":"Model"},
                color_discrete_sequence=px.colors.qualitative.T10,
                )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig.update_yaxes(showline=True, linewidth=1.5, linecolor='grey')
    fig.update_xaxes(showline=True, linewidth=1, linecolor='grey')

    return fig

@app.callback(
    Output("label_model", "children"),
    [
        Input("dropdown_model_variable", "value")        
    ],
)

def show_model_comparison(option):
    property='This figure shows an eight year forecast using a SARIMA model trained on data from 2001 to 2020. The increasing trend of the mean and seasonal peaks of the series is replicated on the forecast for the upcoming years.'
    business='This figure shows an eight year forecast from 2021 to 2028 of an ARIMA model trained on data from 2001 to 2020. The forecast shows an increasing trend on the mean and incorporates an aparent seasonal pattern found on the last years of the training data.'
    if option=='Property':
        return property
    else:
        return business

@app.callback(
    Output("graph_model", "figure"),
    [
        Input("dropdown_model_variable", "value")        
    ],
)

def show_model(option):
    if option=='Property':
        df_out_sample=df_predial_out_sample
    else:
        df_out_sample=df_ica_out_sample

    fig = px.line(df_out_sample,
                x="fecha",
                y=["Real tax payments","ARIMA forecast"], 
                title="Forecasted model for "+ option +" tax",
                labels={"value":"Tax revenue COP (Millions)","fecha":"Date","variable":"Model"},
                color_discrete_sequence=px.colors.qualitative.T10,
                )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig.update_yaxes(showline=True, linewidth=1.5, linecolor='grey')
    fig.update_xaxes(showline=True, linewidth=1, linecolor='grey')


    return fig




