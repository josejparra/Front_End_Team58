import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import pathlib
import dash_table
########################
from db_connection import conn
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
df_predial_obs_predicted=pd.read_csv(DATA_PATH.joinpath('multiple_models_predial.csv'), index_col=0,low_memory=False).reset_index()
df_ica_obs_predicted=pd.read_csv(DATA_PATH.joinpath('multiple_models_ica.csv'), index_col=0,low_memory=False).reset_index()

df_predial_out_sample=pd.read_csv(DATA_PATH.joinpath('out_of_sample_predial.csv'), index_col=0,low_memory=False).reset_index()
df_ica_out_sample=pd.read_csv(DATA_PATH.joinpath('out_of_sample_ica.csv'), index_col=0,low_memory=False).reset_index()

########################
import textwrap
def wrapped_text(text,items=30):
    return textwrap.fill(text, width=items).replace('\n','<br>')
########################
df_ica_fact = pd.read_sql("""
SELECT des_establecimiento, des_naturaleza, des_act_economica, des_clase, vlr_ica, anio
FROM public.vw_ica_declara
""", conn)
df_ica_fact['des_act_economica']=df_ica_fact['des_act_economica'].apply(lambda x: wrapped_text(x, 60))
########################
df_predial_fact = pd.read_sql("""
SELECT tarifa, cod_estrato, des_propietario, vlr_total, anio
FROM public.vw_predial_declara;
""", conn)
########################
df_new= pd.read_sql("""SELECT anio, predial, ica
	FROM public.vw_value_predial_ica
""", conn)
########################
#PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("../data").resolve()
#df_predial_fact=pd.read_csv(DATA_PATH.joinpath('PREDIAL_declara_new.csv')).reset_index()
########################

df_predial_out_sample['fecha']= pd.to_datetime(df_predial_out_sample['fecha'])
df_pred_predial=df_predial_out_sample.groupby(df_predial_out_sample.fecha.dt.year).sum().reset_index()
df_pred_predial=df_pred_predial[df_pred_predial['fecha']>2020]

df_pred_predial=df_pred_predial.drop(columns=['Real tax payments'])
df_pred_predial = df_pred_predial.rename(columns={'ARIMA forecast': 'Forecast predial - ARIMA'})
df_pred_predial['Forecast predial - ARIMA']=df_pred_predial['Forecast predial - ARIMA']*1000000

df_ica_out_sample['fecha']= pd.to_datetime(df_ica_out_sample['fecha'])
df_pred_ica=df_ica_out_sample.groupby(df_ica_out_sample.fecha.dt.year).sum().reset_index()
df_pred_ica=df_pred_ica[df_pred_ica['fecha']>2020]

df_pred_ica=df_pred_ica.drop(columns=['Real tax payments','lower_ci','upper_ci'])
df_pred_ica = df_pred_ica.rename(columns={'ARIMA forecast': 'Forecast ICA - ARIMA'})
df_pred_ica['Forecast ICA - ARIMA']=df_pred_ica['Forecast ICA - ARIMA']*1000000

df_forecast=df_pred_predial.copy()
df_forecast['ICA']=df_pred_ica['Forecast ICA - ARIMA']
df_forecast.columns=['Year','Predial','ICA']

def graph_last_5():
    fig = go.Figure() 
    fig.add_trace(go.Bar( y=df_new.anio, x=df_new.predial, name='Predial', orientation='h', marker=dict( color='SteelBlue', ) )) 
    fig.add_trace(go.Bar( y=df_new.anio, x=df_new.ica, name='ICA', orientation='h', marker=dict( color='LightCoral', ) )) 
    fig.update_layout(barmode='stack',margin=dict(l=10, r=10, t=10, b=10),height=220,plot_bgcolor='rgba(0,0,0,0)') 
    return fig

def graph_next_5():
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=df_forecast.Year,
        x=df_forecast.Predial,
        name='Predial',
        orientation='h',
        #color_continuous_scale="darkmint"
        marker=dict(
            color='SteelBlue',
            #line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
    ))
    fig.add_trace(go.Bar(
        y=df_forecast.Year,
        x=df_forecast.ICA,
        name='ICA',
        orientation='h',
        marker=dict(
            color='LightCoral',
            #line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
        )
    ))
    fig.update_layout(barmode='stack',margin=dict(l=10, r=10, t=10, b=10),height=220,plot_bgcolor='rgba(0,0,0,0)',yaxis=dict(type='category')) 
    
    return fig

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

graphs_layout=html.Div(
    className="row",children=[
        html.Div(className="col-md-1"),
        html.Div(
            className="col-md-5",style={"padding-left": "15px"},
            children=[
                html.H4('Last 6 years', style={"textAlign": "left","padding-left": "15px","padding-right": "0px"}),
                html.H5('This is the behavior of the tax causation of the Rionegro Municipality over the last 5 Years. In Red are identified the proportion of the taxes due to property tax and in blue you can identify the commerce tax causation.'),
                dcc.Graph(id='my-hist', figure=graph_last_5())
            ]
        ),
        html.Div(
            className="col-md-5",style={"padding-left": "15px"},
            children=[
                html.H4('Forecast next 8 years', style={"textAlign": "left","padding-left": "15px","padding-right": "0px"}),
                html.H5('Based on previous years, in the following graph, you will find a forecast of the tax causation, result of applying an ARIMA model trained on data from 2001 to 2020. The increasing trend of the mean and seasonal peaks of the series is replicated on the forecast for the upcoming years.'),
                dcc.Graph(id='my-hist', figure=graph_next_5())
            ]
        ),
        html.Div(className="col-md-1"),
    ]
)

analysis_layout=html.Div(
    className="row",children=[ 
        html.Div(className="col-md-1"),
        html.Div(
            className="col-md-5",style={"padding-left": "15px"},
            children=[
                html.H4('Property Tax', style={"textAlign": "center",}),
                html.P(),
                html.H5('Here you can see the property tax causation amounts. Select by which category and which year you want to filter. By selecting taxpayers, the top 5 taxpayers of the selected year are shown.'),
                html.P(),
                dcc.RadioItems(id='radio_predial_variable',
                    options=[
                        {'label': 'Taxpayers', 'value': 'Top_Taxpayer'},
                        {'label': 'Tax Rate', 'value': 'Tax_Rate'},
                        {'label': 'Stratum', 'value': 'Stratum'}
                    ],
                    value='Stratum',
                    style={'text-align':'center'},
                    labelStyle={'display': 'inline-block','margin-left':'5%','margin-right':'5%'}
                ),
                html.Div([
                    dcc.Dropdown(
                                id="dropdown_predial_year",
                                options=[{'label': str(x), 'value': str(x)} for x in sorted(df_predial_fact.anio.unique())],
                                value='2020',
                                style={'margin':'auto'}
                    )
                ],style={"width": "30%",'align-items':'center'}),
                dcc.Graph(id='graph_top_predial')
            ]
        ),
        html.Div(
            className="col-md-5",style={"padding-left": "15px"},
            children=[
                html.H4('Business Tax', style={"textAlign": "center"}),
                html.P(),
                html.H5('Here you can see the business tax causation amounts. Select by which category and which year you want to filter. By selecting economic activity, the top 5 economic activities by tax revenue of the selected year are shown.'),
                html.P(),
                dcc.RadioItems(id='radio_ica_variable',
                    options=[
                        {'label': 'Class', 'value': 'Class'},
                        {'label': 'Economic Activity', 'value': 'Economic_Activity'},
                        {'label': 'Nature', 'value': 'Nature'}
                    ],
                    value='Nature',
                    style={'text-align':'center'},
                    labelStyle={'display': 'inline-block','margin-left':'5%','margin-right':'5%'}
                ),
                html.Div([
                    dcc.Dropdown(
                                id="dropdown_ica_year",
                                options=[{'label': str(x), 'value': str(x)} for x in sorted(df_ica_fact.anio.unique())],
                                value='2020',
                                style={'margin':'auto'}
                    )
                ],style={"width": "30%",'align-items':'center'}),
                dcc.Graph(id='graph_top_ica')
            ]
        ),
        html.Div(className="col-md-1")
    ]
)

#html.H2('Top 5 taxpayers by tax category', style={"margin-bottom": "3rem","textAlign": "center","color":"#204772"}),
#top_payers

layout = html.Div([
    html.H2('Overview', style={"textAlign": "left"}),
    graphs_layout,
    html.Div(
    className="row",children=[ 
        html.Div(className="col-md-1"),
        html.Div(
            className="col-md-10",style={"padding-left": "15px"},
            children=[
                html.H2('Descriptive analysis', style={"margin-bottom": "3rem","textAlign": "center","color":"#204772"}),
            ]
        ), 
        html.Div(className="col-md-1")
    ]),
    analysis_layout
])


@app.callback(
    Output("graph_top_ica", "figure"),
    [
        Input("dropdown_ica_year", "value"),
        Input("radio_ica_variable", "value")
        
    ],
)
def show_top_ica(webyear,webfeature):

    features={'Class':'des_clase','Economic_Activity':'des_act_economica','Nature':'des_naturaleza'}

    #webyear='2019'
    #webfeature='Class'
    feature=features[webfeature]   

    solData=pd.DataFrame(df_ica_fact.groupby(['anio',feature])['vlr_ica'].sum()).reset_index()

    result=solData.sort_values(['anio','vlr_ica'],ascending=[1,0])
    years=result['anio'].unique()

    if feature=='des_act_economica':
        val='Total Income'
        df_final = pd.DataFrame(columns=result.columns)
        for year in years:
            data=result[result['anio']==year]
            df_final=df_final.append(data.head(5), ignore_index=True)
    else:
        val='Total Income - Log Scale'
        df_final=result.astype({feature: str})

    df_final=df_final.astype({'anio': str})
    df_final=df_final[df_final['anio']==webyear]
    
    table = df_final.pivot_table(values='vlr_ica', index='anio',columns=feature, aggfunc=np.sum, fill_value=0).reset_index()


    tit=f"Income by {webfeature} in year {webyear}"
    fig = px.bar(table, x='anio', y=df_final[feature].unique(), 
                #animation_frame='anio', #This allow to filter by year, but it seems to not autoscale, maybe another approach?
                
                labels={'variable':webfeature, 'value':val, 'anio': 'Year'}, 
                color_discrete_sequence=px.colors.qualitative.T10,
                barmode='group', title=tit)

    if feature!='des_act_economica':
        fig.update_yaxes(type="log", dtick = 1)
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom",y=-0.3,xanchor="left",x=0))
    else:
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom",y=-0.7,xanchor="left",x=0))
    fig.update_layout(title={'x':0.5,'xanchor': 'center'},plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(legend_title_text='')
    fig.update_layout(margin=dict(l=20, r=20, t=50, b=10))
        
    return fig

@app.callback(
    Output("graph_top_predial", "figure"),
    [
        Input("dropdown_predial_year", "value"),
        Input("radio_predial_variable", "value")
        
    ],
)

def show_top_predial(webyear,webfeature):
    features={'Top_Taxpayer':'des_propietario','Tax_Rate':'tarifa','Stratum':'cod_estrato'}
    
    #webyear='2018' #
    #webfeature='Stratum'

    feature=features[webfeature]

    solData=pd.DataFrame(df_predial_fact.groupby(['anio',feature])['vlr_total'].sum()).reset_index()

    result=solData.sort_values(['anio','vlr_total'],ascending=[1,0])
    years=result['anio'].unique()

    if feature=='des_propietario':
        val='Total Income'
        df_final = pd.DataFrame(columns=result.columns)
        for year in years:
            data=result[result['anio']==year]
            df_final=df_final.append(data.head(5), ignore_index=True)
    else:
        val='Total Income - Log Scale'
        df_final=result.astype({feature: str})
        
    df_final=df_final.astype({'anio': str})
    df_final=df_final[df_final['anio']==webyear]
    table = df_final.pivot_table(values='vlr_total', index='anio',columns=feature, aggfunc=np.sum, fill_value=0).reset_index()

    tit=f"Income by {webfeature} in year {webyear}"
    fig = px.bar(table, x='anio', y=df_final[feature].unique(), 
                #animation_frame='anio', #This allow to filter by year, but it seems to not autoscale, maybe another approach?
                labels={'variable':webfeature, 'value':val, 'anio': 'Year'}, 
                color_discrete_sequence=px.colors.qualitative.T10,
                barmode='group', title=tit)
    if feature!='des_propietario':
        fig.update_yaxes(type="log", dtick = 1)
        fig.update_layout(legend=dict(orientation="h",yanchor="bottom",y=-0.2,xanchor="left",x=0),)
    else:
        fig.update_layout(legend=dict(orientation="h",yanchor="bottom",y=-0.5,xanchor="left",x=0),)
    fig.update_layout(legend_title_text='',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(title={'x':0.5,'xanchor': 'center'})
    fig.update_layout(margin=dict(l=50, r=20, t=50, b=10))

    return fig