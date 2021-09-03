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

df_avaluo=pd.read_csv(DATA_PATH.joinpath('sensibilidad.csv')).reset_index() 
df_avaluo = df_avaluo.rename(columns={'porcentajeAumentoRecaudo- 2% avaluo': 'Property valuation increases 2%',
                                     'porcentajeAumentoRecaudo- 5% avaluo':'Property valuation increases 5%',
                                     'porcentajeAumentoRecaudo- 8% avaluo':'Property valuation increases 8%',
                                     }
                            )

df_estrato=pd.read_csv(DATA_PATH.joinpath('sensibilidadEstrato.csv')).reset_index() 
df_estrato = df_estrato.rename(columns={'porcentajeAumentoRecaudo- 5% estrato5': '5% of properties upgrade from stratum 5 to stratum 6',
                                     'porcentajeAumentoRecaudo- 2% estrato4':'2% of properties upgrade from stratum 4 to stratum 5',
                                     'porcentajeAumentoRecaudo- 2% estrato3':'2% of properties upgrade from stratum 3 to stratum 4',
                                     }
                            )

df_area=pd.read_csv(DATA_PATH.joinpath('sensibilidadArea.csv')).reset_index() 
df_area = df_area.rename(columns={'porcentajeAumentoRecaudo- 5% area': '5% of the properties are subdivided into 2 separate lots',
                                     'porcentajeAumentoRecaudo- 2% area':'2% of the properties are subdivided into 2 separate lots',
                                     'porcentajeAumentoRecaudo- 3% area':'3% of the properties are subdivided into 2 separate lots',
                                     }
                            )

def valuation_predial():

    fig = px.line(df_avaluo[df_avaluo['AÑO']>=2012],
                x="AÑO",
                y=["Property valuation increases 2%",
                    "Property valuation increases 5%",
                    "Property valuation increases 8%"], 
                title="Sensitivity Analysis - Valuation",
                labels={"value":"Variation a percentage of total tax revenue",
                        "AÑO":"Year",
                        "variable":"Scenario",
                        },
                color_discrete_sequence=px.colors.qualitative.T10,
                )

    fig.update_yaxes(showline=True, linewidth=1.5, linecolor='grey')
    fig.update_xaxes(showline=True, linewidth=1, linecolor='grey')
    fig.update_layout(
        yaxis=dict(tickformat=".1%"),
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def stratum_predial():

    fig = px.line(df_estrato[df_estrato['AÑO']>=2012],
              x="AÑO",
              y=["5% of properties upgrade from stratum 5 to stratum 6",
                 "2% of properties upgrade from stratum 4 to stratum 5",
                 "2% of properties upgrade from stratum 3 to stratum 4"], 
              title="Sensitivity Analysis - Stratum",
              labels={"value":"Variation a percentage of total tax revenue",
                      "AÑO":"Year",
                      "variable":"Scenario",
                     },
              color_discrete_sequence=px.colors.qualitative.T10,
             )
    fig.update_layout(
        yaxis=dict(tickformat=".1%",range=[-0.01,0.04]),
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig.update_yaxes(showline=True, linewidth=1.5, linecolor='grey')
    fig.update_xaxes(showline=True, linewidth=1, linecolor='grey')

    return fig

def area_predial():

    fig = px.line(df_area[df_area['AÑO']>=2012],
              x="AÑO",
              y=["5% of the properties are subdivided into 2 separate lots",
                 "3% of the properties are subdivided into 2 separate lots",
                 "2% of the properties are subdivided into 2 separate lots"], 
              title="Sensitivity Analysis - Property Area",
              labels={"value":"Variation a percentage of total tax revenue",
                      "AÑO":"Year",
                      "variable":"Scenario",
                     },
              color_discrete_sequence=px.colors.qualitative.T10,
             )
    fig.update_layout(
        yaxis=dict(tickformat=".1%"),
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig.update_yaxes(showline=True, linewidth=1.5, linecolor='grey')
    fig.update_xaxes(showline=True, linewidth=1, linecolor='grey')

    return fig

graphs_predial=html.Div(
    className="row",children=[ 
        html.Div(className="col-md-1"),
        html.Div(
            className="col-md-10",style={"padding-left": "15px","align-items": "center"},
            children=[
                html.H5('In this page you can identify how the property tax causation might be affected by performing changes in Valuation, stratum and area features.'),
                html.H5(style={"margin-top":"0.5rem"},children=['The figure shows three scenarios showing how the property tax revenue might had changed in the last five years if the property valuations had increased.']),
                
                dcc.Graph(id='sensitivity_valuation_predial',figure=valuation_predial(),config={'displayModeBar': False}),
                html.H5(style={"margin-top":"0.5rem"},children=['The next one shows how property tax revenue might changed the last five years if a proportion of the properties categorized in certain stratum upgrades one stratum.']),
                
                dcc.Graph(id='sensitivity_stratum_predial',figure=stratum_predial(),config={'displayModeBar': False}),
                html.H5(style={"margin-top":"0.5rem"},children=['The figure shows how property tax revenue might have changed in the last five years if a proportion of the properties were divided into two new properties with half area and half valuation.']),
                
                dcc.Graph(id='sensitivity_area_predial',figure=area_predial(),config={'displayModeBar': False}),
            ]
        ),
        html.Div(className="col-md-1")
    ]
)


layout = html.Div([
    html.H2('Sensitivity Analysis', style={"textAlign": "left"}),
    html.P(),
    html.H3('Property Tax', style={"textAlign": "center"}),
    html.P(),
    graphs_predial
])