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


pagos_ica_df = pd.read_csv(DATA_PATH.joinpath("tb_ICA_pagos.csv"))
pagos_ica_df['periodo_ult_pago'] = pd.to_datetime(pagos_ica_df['periodo_ult_pago'], format='%Y-%m').dt.to_period('M')
pagos_ica_df['mes']=pagos_ica_df['periodo_ult_pago'].dt.month

dfv = pd.read_csv(DATA_PATH.joinpath("vgsales.csv"))  # GregorySmith Kaggle
sales_list = ["North American Sales", "EU Sales", "Japan Sales", "Other Sales",	"World Sales"]

def show_hist():
    fig = px.histogram(pagos_ica_df, x="mes", color="anio",
            title='Histogram of payments throught the year',
            labels={'mes':'Periodo'})
    return fig


layout = html.Div([
    html.H1('Overview', style={"textAlign": "left"}),
    dcc.Graph(id='my-hist', figure=show_hist()),
])



