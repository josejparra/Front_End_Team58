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

df_PREDIAL_pagos = pd.read_csv(DATA_PATH.joinpath("tb_PREDIAL_pagos.csv")) 
df_PREDIAL_facturas = pd.read_csv(DATA_PATH.joinpath("tb_PREDIAL_facturas.csv")) 

df_ICA_pagos = pd.read_csv(DATA_PATH.joinpath("tb_ICA_pagos.csv")) 
df_ICA_declaraciones = pd.read_csv(DATA_PATH.joinpath("tb_ICA_declaraciones.csv")) 

def ICA_section():
    ica_section_layout=html.Div(
        id="upper-left",
        className="two columns",
        children=[
            html.Div(
                className="control-row-1",
                children=[
                    html.Div(
                        id="taxpayer-select-outer",
                        children=[
                            html.Label("Select a type of taxpayer"),
                            dcc.Dropdown(
                                id="taxpayer-select",
                                options=[{'label': x, 'value': x} for x in sorted(df_ICA_declaraciones.cod_clase.unique())],
                                value='All',
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                className="control-row-1",
                children=[
                    html.Div(
                        id="nature-select-outer",
                        children=[
                            html.Label("Select a nature type"),
                            dcc.Dropdown(
                                id="nature-select",
                                options=[{'label': x, 'value': x} for x in sorted(df_ICA_declaraciones.cod_naturaleza.unique())],
                                value='All',
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                id="rate-ICA-select-outer",
                className="control-row-2",
                children=[
                    html.Label("Pick a Taxation rate"),
                    html.Div(
                        id="checklist-container",
                        children=dcc.Checklist(
                            id="rate-ICA-select-all",
                            options=[{"label": "Select All Rates", "value": "All"}],
                            value=[],
                        ),
                    ),
                    html.Div(
                        id="region-select-dropdown-outer",
                        children=dcc.Dropdown(
                            id="rate-ICA-select", multi=True, searchable=True,   
                        ),
                    ),
                ],
            ),
        ]
    )
    return ica_section_layout

def predial_section():
    predial_section_layout=html.Div(
        id="upper-left",
        className="two columns",
        children=[
            html.Div(
                className="control-row-1",
                children=[
                    html.Div(
                        id="stratum-select-outer",
                        children=[
                            html.Label("Select a stratum"),
                            dcc.Dropdown(
                                id="stratum-select",
                                options=[{'label': x, 'value': x} for x in sorted(df_PREDIAL_facturas.cod_estrato.unique())],
                                value='All',
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                className="control-row-1",
                children=[
                    html.Div(
                        id="neighborhood-select-outer",
                        children=[
                            html.Label("Select a neighborhood"),
                            dcc.Dropdown(
                                id="neighborhood-select",
                                options=[{'label': x, 'value': x} for x in sorted(df_PREDIAL_facturas.cod_barrio.unique())],
                                value='All',
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                id="rate-PREDIAL-select-outer",
                className="control-row-2",
                children=[
                    html.Label("Pick a Taxation rate"),
                    html.Div(
                        id="checklist-container",
                        children=dcc.Checklist(
                            id="rate-PREDIAL-select-all",
                            options=[{"label": "Select All Rates", "value": "All"}],
                            value=[],
                        ),
                    ),
                    html.Div(
                        id="region-select-dropdown-outer",
                        children=dcc.Dropdown(
                            id="rate-PREDIAL-select", multi=True, searchable=True,   
                        ),
                    ),
                ],
            ),
        ]
    )
    return predial_section_layout

layout = html.Div([
    html.H1('Detail Forecast Analysis', style={"textAlign": "left"}),
    html.H2('Property Tax', style={"textAlign": "center"}),
    html.Div(  
            id="upper-container",
            className="row",
            children=[
                predial_section(),
    ]),
    html.H2('Commerce Tax', style={"textAlign": "center"}),
    html.Div(
            id="lower-container",
            className="row",
            children=[
                ICA_section()
    ])
])

@app.callback(
    [
        Output("rate-ICA-select", "value"),
        Output("rate-ICA-select", "options"),
    ],
    [Input("rate-ICA-select-all", "value")],
)

def update_rate_ICA_dropdown(select_all):
    options=[{'label': x, 'value': x} for x in sorted(df_ICA_declaraciones.tarifa.unique())]

    rates = df_ICA_declaraciones["tarifa"].unique()

    ctx = dash.callback_context
    if ctx.triggered[0]["prop_id"].split(".")[0] == "rate-ICA-select-all":
        if select_all == ["All"]:
            value = [i["value"] for i in options]
        else:
            value = dash.no_update
    else:
        value = rates[:1]
    return (
        value,
        options
    )

@app.callback(
    [
        Output("rate-PREDIAL-select", "value"),
        Output("rate-PREDIAL-select", "options"),
    ],
    [Input("rate-PREDIAL-select-all", "value")],
)

def update_rate_PREDIAL_dropdown(select_all):
    
    rates = df_PREDIAL_facturas["tarifa"].unique()
    options=[{'label': x, 'value': x} for x in sorted(rates)]

    ctx = dash.callback_context
    if ctx.triggered[0]["prop_id"].split(".")[0] == "rate-PREDIAL-select-all":
        if select_all == ["All"]:
            value = [i["value"] for i in options]
        else:
            value = dash.no_update
    else:
        value = rates[:1]
    return (
        value,
        options
    )




