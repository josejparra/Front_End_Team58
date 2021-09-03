import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import pathlib
########################
from sklearn.cluster import KMeans
########################
from db_connection import conn
from app import app
########################
import textwrap
def wrapped_text(text,items=30):
    return textwrap.fill(text, width=items).replace('\n','<br>')
########################
df_icacons= pd.read_sql("""
SELECT cc_nit, des_establecimiento, des_naturaleza, des_act_economica, des_clase, vlr_ica, anio
FROM public.vw_ica_declara
""", conn)
df_icacons['des_act_economica']=df_icacons['des_act_economica'].apply(lambda x: wrapped_text(x, 60))
# PATH = pathlib.Path(__file__).parent
# DATA_PATH = PATH.joinpath("../data").resolve()
# df_pred_fact=pd.read_csv(DATA_PATH.joinpath('tb_PREDIAL_facturas.csv')).reset_index()
df_pred_fact= pd.read_sql("""
SELECT id_doc,des_propietario, area_terr, area_const, vlr_tot_avaluo, vlr_total, anio
FROM public.vw_predial_declara
""",conn)

graphs_predial=html.Div(
    className="row",children=[ 
        html.Div(className="col-md-1"),
        html.Div(
            className="col-md-10",style={"padding-left": "15px","align-items": "center"},
            children=[
                html.H4('Property Tax', style={"textAlign": "center","margin-top":"1.5rem"}),
                html.H5(style={"margin-top":"1.5rem"},children=['In the interactive graph, the orange points are marked as outliers. You can have the taxpayer information by passing the pointer over the point. These records are marked as outliers based on the distribution of the data. It is worth checking for taxation errors.']),
                 html.Div([
                    dcc.Dropdown(
                                id="dropdown_predial_outlier_variable",
                                 options=[
                                    {'label': 'Valuation', 'value': 'Valuation'},
                                    {'label': 'Terrain Area', 'value': 'Terrain_Area'},
                                    {'label': 'Built Area', 'value': 'Built_Area'}
                                ],
                                value='Valuation',
                                style={'margin':'auto'}
                    )
                ],style={"width": "30%","align-items":"center"}),
                html.Div([
                    dcc.Dropdown(
                                id="dropdown_predial_outlier_year",
                                options=[{'label': x, 'value': x} for x in sorted(df_pred_fact.anio.unique())],
                                value=2020,
                                style={'margin':'auto'}
                    )
                ],style={"width": "20%",'align-items':'center'}),
                dcc.Loading(id = "loading-icon", 
                children=[html.Div(dcc.Graph(id='graph_outliers_predial',config={'displayModeBar': False}))], type="default")
            ]
        ),
        html.Div(className="col-md-1")
    ]
)


graphs_ICA=html.Div(
    className="row",children=[ 
        html.Div(className="col-md-1"),
        html.Div(
            className="col-md-10",style={"padding-left": "15px","align-items": "center"},
            children=[
                html.H4('Business Tax', style={"textAlign": "center","margin-top":"0.5rem"}),
                html.H5(style={"margin-top":"0.5rem"},children=['In the interactive graph, the orange points are marked as outliers. These graphs show the distribution of the tax revenue by economic activity. Above the figure you can see the amount of taxpayers with 0 tax revenue. You can have the taxpayer information by passing the pointer over the point. These records are marked as outliers based on the distribution of the data. It is worth checking for taxation errors.']),
                 html.Div([
                    dcc.Dropdown(
                                id="dropdown_ica_outlier_class",
                                options=[{'label': x, 'value': x} for x in sorted(df_icacons.des_act_economica.unique())],
                                value='INDUSTRIAS MANUFACTURERAS',
                                style={'margin':'auto'}
                    )
                ],style={"align-items":"center"}),
                html.Div([
                    dcc.Dropdown(
                                id="dropdown_ica_outlier_year",
                                options=[{'label': str(x), 'value': str(x)} for x in sorted(df_icacons.anio.unique())],
                                value='2020',
                                style={'margin':'auto'}
                    )
                ],style={"width": "20%",'align-items':'center'}),
                dcc.Graph(id='graph_outliers_ica',config={'displayModeBar': False})
            ]
        ),
        html.Div(className="col-md-1")
    ]
)

layout = html.Div([
    html.H2('Outliers identification', style={"textAlign": "left"}),
    graphs_predial,
    graphs_ICA,
])

@app.callback(
    Output(component_id='graph_outliers_predial', component_property='figure'),
        [
        Input("dropdown_predial_outlier_year", "value"),
        Input("dropdown_predial_outlier_variable", "value")        
    ],
)
def display_predial_outliers(year,webvar):
    
    options = {'Valuation':'vlr_tot_avaluo', 'Terrain_Area':'area_terr', 'Built_Area':'area_const'}
    clustersize={'vlr_tot_avaluo':4,'area_terr':7,'area_const':4}
    #webvar = 'Built_Area'
    #year = int(year)

    var = options[webvar]

    df_cluster=df_pred_fact[df_pred_fact['anio'] == year][['id_doc','des_propietario',var,'vlr_total']]

    if var=='vlr_tot_avaluo':
        kmeans = KMeans(n_clusters=clustersize[var], random_state=0).fit(df_cluster[[var,'vlr_total']])
        data_norm=df_cluster.loc[kmeans.labels_!=1]
        data_color=df_cluster.loc[kmeans.labels_==1]
        fig = px.scatter(x=data_norm[var], y=data_norm['vlr_total'],color_discrete_sequence=px.colors.qualitative.T10)
        fig.update_traces(hovertemplate=None,hoverinfo='skip')
        fig1= px.scatter(data_color,
                        x=var, 
                        y='vlr_total',
                        color_discrete_sequence = ["orange"],
                        hover_name='des_propietario',
                        hover_data=[var,'vlr_total'],
                        labels={var:'Avaluo','vlr_total':'Tax value:'}
                        )
        fig.add_trace(fig1.data[0])
        fig.update_layout(
            title=
            {
                'text':f"Total Tax distribution in the year {year}",
                'x':0.5,
                'xanchor': 'center'
            },
            xaxis_title=webvar,
            yaxis_title="Total Tax",
            plot_bgcolor='rgba(0,0,0,0)'
        )
        fig.update_yaxes(showline=True, linewidth=1.5, linecolor='grey')
        fig.update_xaxes(showline=True, linewidth=1, linecolor='grey')
        #df_table=df_cluster.loc[kmeans.labels_==1].sort_values(by=['vlr_total'], ascending=True)
        
    else:
        percentile=np.percentile(df_cluster[var], 99.95)
        data_norm=df_cluster[df_cluster[var]<percentile]
        data_color=df_cluster[df_cluster[var]>=percentile]
        fig = px.scatter(x=data_norm[var], y=data_norm['vlr_total'],color_discrete_sequence=px.colors.qualitative.T10)
        fig.update_traces(hovertemplate=None,hoverinfo='skip')
        fig1= px.scatter(data_color,
                        x=var, 
                        y='vlr_total',
                        color_discrete_sequence = ["orange"],
                        hover_name='des_propietario',
                        hover_data=[var,'vlr_total'],
                        labels={var:webvar,'vlr_total':'Tax value:'}
                        )
        fig.add_trace(fig1.data[0])
        fig.update_layout(
            title=
            {
                'text':f"Total Tax distribution in the year {year}",
                'x':0.5,
                'xanchor': 'center'
            },
            xaxis_title=webvar,
            yaxis_title="Total Tax",
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        fig.update_yaxes(showline=True, linewidth=1.5, linecolor='grey')
        fig.update_xaxes(showline=True, linewidth=1, linecolor='grey')
        #df_table=df_cluster[df_cluster[var]>=percentile].sort_values(by=['vlr_total'], ascending=True)

    return fig

@app.callback(
    Output(component_id='graph_outliers_ica', component_property='figure'),
        [
        Input("dropdown_ica_outlier_year", "value"),
        Input("dropdown_ica_outlier_class", "value")        
    ],
)
def display_ICA_outliers(year,act_economica):
    

    df_filtered=df_icacons[(df_icacons['anio']==year) & (df_icacons['des_act_economica']==act_economica)]
    
    lower_quartile = np.percentile(df_filtered["vlr_ica"], 25)

    fig1=px.box(x=df_filtered["vlr_ica"],
            points = 'outliers',
            color_discrete_sequence=px.colors.qualitative.T10,
            width=1000, 
            height=400
           )

    fig1.update_xaxes(type="log")

    #y=df_filtered[df_filtered['valor_impuesto']<lower_quartile]['valor_impuesto']
    fig2 = px.strip(df_filtered[df_filtered['vlr_ica']<lower_quartile],
                    x='vlr_ica',color_discrete_sequence = ["orange"],
                    custom_data =['des_establecimiento'],
                    hover_name='des_establecimiento',
                    hover_data=['vlr_ica','cc_nit'],
                    labels={'cc_nit':'ID_NIT','vlr_ica':'Tax value:'}
                    )
    
    #fig.update_traces(hovertemplate=None, selector={'name':'Europe'}) # revert to default hover

    fig3 = px.strip(x=df_filtered[df_filtered['vlr_ica']>=lower_quartile]['vlr_ica'],
                    color_discrete_sequence=px.colors.qualitative.T10,
                    #hoverinfo='skip'
                )
    try:
        fig1.add_trace(fig2.data[0])
    except:
        pass
    try:
        fig1.add_trace(fig3.data[0])
    except:
        pass
    fig1 = fig1.update_traces(offsetgroup="1")
    yaxis_text = wrapped_text(act_economica)
    fig1.update_layout(
        title=
        {
            'text':"Total Tax distribution in the year "+year,
            'x':0.5,
            'xanchor': 'center'
        },
        yaxis_title=yaxis_text,
        xaxis_title="Total Tax - Log Scale",
        plot_bgcolor='rgba(0,0,0,0)'
    )
    #Add annotation
    fig1.add_annotation(text=f"Number of contribuyentes with tax 0: {len(df_filtered[df_filtered['vlr_ica']==0])}",
                  xref="paper", yref="paper",
                  x=0.5, y=1, showarrow=False)
    fig1.update_yaxes(showline=False, linewidth=2, linecolor='black', gridcolor='grey')

    return fig1


