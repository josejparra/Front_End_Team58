import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import pathlib
from app import app
import dash_table

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
########################
######Read files
########################
df_predial=pd.read_csv(DATA_PATH.joinpath('tb_PREDIAL_pagos.csv'), index_col=0,low_memory=False).reset_index() 
df_ica=pd.read_csv(DATA_PATH.joinpath('tb_ICA_pagos.csv'), index_col=0,low_memory=False).reset_index() 
########################
######
########################
df_new=df_predial.groupby(by="anio", dropna=False).sum()['vlr_factura'].reset_index() 
df_newICA = df_ica.groupby(by="anio", dropna=False).sum()['vlr_factura'].reset_index() 
df_new['ValorIca']=df_newICA['vlr_factura'] 
df_new.columns=['Year','Predial','ICA'] 


def graph_last_5():
    fig = go.Figure() 
    fig.add_trace(go.Bar( y=df_new.Year, x=df_new.Predial, name='Predial', orientation='h', marker=dict( color='SteelBlue', ) )) 
    fig.add_trace(go.Bar( y=df_new.Year, x=df_new.ICA, name='ICA', orientation='h', marker=dict( color='LightCoral', ) )) 
    fig.update_layout(barmode='stack',margin=dict(l=10, r=10, t=10, b=10),height=220,paper_bgcolor="rgba(0,0,0,0)") 
    return fig

graphs_layout=html.Div(
        className="col-md-5",style={"padding-left": "15px"},
        children=[
            html.H4('Last 5 years', style={"textAlign": "left","padding-left": "15px","padding-right": "0px"}),
            html.H5('This is the behavior of the tax causation of the Rionegro Municipality over the last 5 Years. In Red are identified the proportion of the taxes due to property tax and in blue you can identify the commerce tax causation.', style={"textAlign": "left","color":"#c4c4c4"}),
            dcc.Graph(id='my-hist', figure=graph_last_5()),
            html.H4('Forecast next 5 years', style={"margin-top": "3rem","textAlign": "left","padding-left": "15px","padding-right": "0px"}),
            html.H5('Based on previous years, in the following, you could find a forecast of the tax causation. This forecast is the result of applying an XXX model which takes the information of XX XX XX for each taxpayer.', style={"textAlign": "left","color":"#c4c4c4"})
        ]
    )

property_tax=html.Div(
        className="col-md-6",style={"padding-left": "15px"},
        children=[
            html.H4('Property Tax', style={"textAlign": "center",}),
            html.H5('Tax causation amounts by stratum, rate, and Neighborhood.', style={"textAlign": "left","color":"#c4c4c4"}),
        ]
    )

business_tax=html.Div(
        className="col-md-6",style={"padding-left": "15px"},
        children=[
            html.H4('Business Tax', style={"textAlign": "center"}),
            html.H5('Tax causation amounts by CIIU and Rates', style={"textAlign": "left","color":"#c4c4c4"}),
        ]
    )

top_payers=html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-md-6 my-auto",
                    children=[
                        html.H4('Property Tax',style={"textAlign": "center"}),
                        dash_table.DataTable(
                            id='table',
                            columns=[{"name": i, "id": i} for i in df_new.columns],
                            data=df_new.to_dict('records'),
                            fill_width=False,
                            style_table={'marginLeft': 'auto', 'marginRight': 'auto'},
                            style_cell={'textAlign': 'center','padding-left': '10px','padding-right': '10px'},
                            style_header={'color':'white','backgroundColor': '#204772','fontWeight': 'bold','textAlign': 'center'},
                        )
                    ]
                ),
                html.Div(
                    className="col-md-6 my-auto",style={"padding-left": "15px","padding-right": "15px"},
                    children=[
                        html.H4('Business Tax', style={"textAlign": "center"}),
                    dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in df_new.columns],
                        data=df_new.to_dict('records'),
                        fill_width=False,
                            style_table={'marginLeft': 'auto', 'marginRight': 'auto'},
                            style_cell={'textAlign': 'center','padding-left': '10px','padding-right': '10px'},
                            style_header={'color':'white','backgroundColor': '#204772','fontWeight': 'bold','textAlign': 'center'},
                        )
                    ]
                )
            ]
)


right_layout=html.Div(
        className="col-md-7",style={"padding-left": "15px"},
        children=[
            html.H2('Next year forecast', style={"margin-bottom": "3rem","textAlign": "center","color":"#204772"}),
            html.H5('According to the forecast, the total tax causation for next year and their percentage change is forecast A detailed view of property and business tax is also displayed.', style={"textAlign": "left","color":"#c4c4c4"}),
            html.Div(
            className="row",
            children=[
                property_tax,
                business_tax            
            ]),
            html.H2('Top 5 taxpayers by tax category', style={"margin-bottom": "3rem","textAlign": "center","color":"#204772"}),
            top_payers
            ]
    )


layout = html.Div([
    html.H2('Overview', style={"textAlign": "left"}),
    html.Div(
            className="row",
            children=[
                graphs_layout,
                right_layout            
            ]),
])
