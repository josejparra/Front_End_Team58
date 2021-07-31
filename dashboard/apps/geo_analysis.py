import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
import json
from random import randrange
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_PREDIAL_pagos = pd.read_csv(DATA_PATH.joinpath("tb_PREDIAL_pagos.csv")) 
df_PREDIAL_facturas = pd.read_csv(DATA_PATH.joinpath("tb_PREDIAL_facturas.csv")) 

df_ICA_pagos = pd.read_csv(DATA_PATH.joinpath("tb_ICA_pagos.csv")) 
df_ICA_declaraciones = pd.read_csv(DATA_PATH.joinpath("tb_ICA_declaraciones.csv")) 

##Reading JSON file
GEODATA_PATH = PATH.joinpath("../geodata").resolve()
with open(GEODATA_PATH.joinpath("Pol_Subzonas.json")) as geofile:
    j_file = json.load(geofile)

##DF with random data for test

df = pd.DataFrame()
df['id'] = None
df['Val'] = None

i=1
for feature in j_file["features"]:
    feature ['id'] = str(i).zfill(2)
    new_line = pd.Series([feature ['id'], randrange(20)+5], index=df.columns) # creamos un objeto Seris
    df = df.append(new_line, ignore_index=True)
    i += 1

def random_num():
    list_num=[]
    for i in range (0,349):
        j=str(i).zfill(2)
        list_num.append(j)
    return list_num

def map_section():
    map_layout=html.Div(
        className="ten columns",
        children=[
            html.Div(
                children=[dcc.Graph(
                        id='map_Rionegro', 
                        figure={}, 
                        style={"margin-right": "auto", "margin-left": "auto", "width": "80%", "height":"500px"}
                    )
                ],
            ),
         ],
    )
    return map_layout

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
                className="control-row-1",
                children=[
                    html.Div(
                        id="testid2-select-outer",
                        children=[
                            html.Label("Select an ID"),
                            dcc.Dropdown(
                                id="testid2-select",
                                options=[{'label': x, 'value': x} for x in sorted(random_num())],
                                value='All',
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                id="GEO-rate-ICA-select-outer",
                className="control-row-2",
                children=[
                    html.Label("Pick a Taxation rate"),
                    html.Div(
                        id="checklist-container",
                        children=dcc.Checklist(
                            id="GEO-rate-ICA-select-all",
                            options=[{"label": "Select All Rates", "value": "All"}],
                            value=[],
                        ),
                    ),
                    html.Div(
                        id="region-select-dropdown-outer",
                        children=dcc.Dropdown(
                            id="GEO-rate-ICA-select", multi=True, searchable=True,   
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
                        children=[
                            html.Label("Select an ID"),
                            dcc.Dropdown(
                                id="testid1-select",
                                options=[{'label': x, 'value': x} for x in sorted(random_num())],
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
                        children=[
                            html.Label("Select a stratum"),
                            dcc.Dropdown(
                                id="GEO-stratum-select",
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
                        children=[
                            html.Label("Select a neighborhood"),
                            dcc.Dropdown(
                                id="GEO-neighborhood-select",
                                options=[{'label': x, 'value': x} for x in sorted(df_PREDIAL_facturas.cod_barrio.unique())],
                                value='All',
                            ),
                        ],
                    ),
                ],
            ),

            html.Div(
                id="GEO-rate-PREDIAL-select-outer",
                className="control-row-2",
                children=[
                    html.Label("Pick a Taxation rate"),
                    html.Div(
                        children=dcc.Checklist(
                            id="GEO-rate-PREDIAL-select-all",
                            options=[{"label": "Select All Rates", "value": "All"}],
                            value=[],
                        ),
                    ),
                    html.Div(
                        children=dcc.Dropdown(
                            id="GEO-rate-PREDIAL-select", multi=True, searchable=True,   
                        ),
                    ),
                ],
            ),
        ]
    )
    return predial_section_layout


def display_RionegroICA():
    fig = px.choropleth_mapbox(geojson=j_file, locations=df['id'], color=df['Val'],
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           zoom=12, center = {"lat": 6.1508, "lon": -75.3775},
                           opacity=0.5
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

layout = html.Div([
    html.H1('Geographical Analysis', style={"textAlign": "left"}),
    html.H2('Property Tax', style={"textAlign": "center"}),
    html.Div(  
            id="GEO-upper-container",
            className="row",
            children=[
                predial_section(),
                html.Div(
                    className="ten columns",
                    children=[
                    html.Div(
                        children=[dcc.Graph(
                            id='map_Rionegro', 
                            figure={}, 
                            style={"margin-right": "auto", "margin-left": "auto", "width": "80%", "height":"500px"}
                        )
                        ],
                    ),
                    ],
                )               
            ]),
    html.H2('Commerce Tax', style={"textAlign": "center"}),
    html.Div(
            id="GEO-lower-container",
            className="row",
            children=[
                ICA_section()                
    ])
])




# layout = html.Div([
#     html.H1('Geographical Analysis', style={"textAlign": "left"}),
    
#     html.Div([
#         dbc.Row([
#                 dbc.Col(),
#                 dbc.Col(dropdown_id,md=2),
#                 dbc.Col()
#                 ])
#      ]),
#     dcc.Graph(id='my-map_Rionegro', figure={}, style={"margin-right": "auto", "margin-left": "auto", "width": "80%", "height":"500px"})
# ])
@app.callback(
    [
        Output("GEO-rate-ICA-select", "value"),
        Output("GEO-rate-ICA-select", "options"),
    ],
    [Input("GEO-rate-ICA-select-all", "value")],
)
def update_rate_ICA_dropdown(select_all):
    options=[{'label': x, 'value': x} for x in sorted(df_ICA_declaraciones.tarifa.unique())]

    rates = df_ICA_declaraciones["tarifa"].unique()

    ctx = dash.callback_context
    if ctx.triggered[0]["prop_id"].split(".")[0] == "GEO-rate-ICA-select-all":
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
        Output("GEO-rate-PREDIAL-select", "value"),
        Output("GEO-rate-PREDIAL-select", "options"),
    ],
    [Input("GEO-rate-PREDIAL-select-all", "value")],
)

def update_rate_PREDIAL_dropdown(select_all):
    
    rates = df_PREDIAL_facturas["tarifa"].unique()
    options=[{'label': x, 'value': x} for x in sorted(rates)]

    ctx = dash.callback_context
    if ctx.triggered[0]["prop_id"].split(".")[0] == "GEO-rate-PREDIAL-select-all":
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
    Output(component_id='map_Rionegro', component_property='figure'),
    [Input(component_id='testid1-select', component_property='value')]
)
def display_RionegroPREDIAL(id_chosen):
    if id_chosen=='All':
        df_fltrd = df
    else:
        df_fltrd = df[(df['id'] == id_chosen)]
    fig = px.choropleth_mapbox(geojson=j_file, locations=df_fltrd['id'], color=df_fltrd['Val'],
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           zoom=12, center = {"lat": 6.1508, "lon": -75.3775},
                           opacity=0.5,
                           height=320
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

#@app.callback(
#    Output(component_id='Map_ICA_Rionegro', component_property='figure'),
#    [Input(component_id='testid2_select', component_property='value')]
#)

# def display_RionegroICA(id_chosen):
#     df_fltrd = df[(df['id'] == id_chosen)]
#     fig = px.choropleth_mapbox(geojson=j_file, locations=df_fltrd['id'], color=df_fltrd['Val'],
#                            color_continuous_scale="Viridis",
#                            mapbox_style="carto-positron",
#                            zoom=12, center = {"lat": 6.1508, "lon": -75.3775},
#                            opacity=0.5
#                           )
#     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#     return fig