import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server


# Connect to your app pages
from apps import navbar, overview, geo_analysis, forecast, evasion, team
app.layout=html.Div(
    children=[
    navbar.Navbar()
    ,html.Div([dbc.Row([dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='Overview', value='tab-1',className='custom-tab',selected_className="custom-tab--selected"),
                dcc.Tab(label='Geographical Analysis', value='tab-2',className='custom-tab',selected_className="custom-tab--selected"),
                dcc.Tab(label='Detailed Forecast', value='tab-3',className='custom-tab',selected_className="custom-tab--selected"),
                dcc.Tab(label='Evasion and Avoidance Analysis', value='tab-4', className='custom-tab',selected_className="custom-tab--selected"),
                dcc.Tab(label='The development Team', value='tab-5',className='custom-tab',selected_className="custom-tab--selected"),
            ])
            , html.Div(id='tabs-content')
        ]))
    ])
    ])
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return overview.layout
    elif tab == 'tab-2':
       return geo_analysis.layout
    elif tab == 'tab-3':
       #return forecast.layout
       return forecast.layout
    elif tab == 'tab-4':
        #return dtl_forecast.layout
       return evasion.layout
    elif tab == 'tab-5':
       return team.layout

if __name__ == '__main__':
    app.run_server(debug=False)
