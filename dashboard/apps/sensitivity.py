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



layout = html.Div([
    html.H2('Sensitivity Analysis', style={"textAlign": "left"}),
    html.H3('Property Tax', style={"textAlign": "center"}),
    html.P(),
    html.H3('Business Tax', style={"textAlign": "center"})
])


