import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app


slideshow = html.Div(
    className="row",style={"background-color":"#f0f8ff"},
            children=[
                html.Div(className="col-md-3",children=[
                html.Img(className="img-fluid",src="/assets/home/Mapa.png",width="70%",style={"text-align":"center"}),
                html.H5(style={"padding-left":"40px","padding-right":"0px"},children=[
                    "Rionegro is a city and municipality in Antioquia Department, Colombia, located in the sub-region of Eastern Antioquia, which is really interested in understand how their tax collection will behave."])
                ]),
                html.Div(className="col-md-9",children=[
                    html.Section(id="slideshow", children=[
                        html.Div(id="slideshow-container", children=[
                            html.Div(id="image"),
                            dcc.Interval(id='interval', interval=2000)
                        ],style={"text-align":"left"})
                    ])
                ])
            ]
)
                

@app.callback(Output('image', 'children'),
              [Input('interval', 'n_intervals')])
def display_image(n):
    if n == None or n % 3 == 1:
        img = html.Img(src="/assets/home/Img1 (1).jpg",style={"width":"75%","text-align":"center"})
    elif n % 3 == 2:
        img = html.Img(src="/assets/home/Img2 (1).jpg",style={"width":"75%","text-align":"center"})
    elif n % 3 == 0:
        img = html.Img(src="/assets/home/Img3 (1).jpg",style={"width":"75%","text-align":"center"})
    else:
        img = "None"
    return img

layout = html.Div(
    [
        html.H1("Rionegro",style={"white-space": "nowrap","text-align":"center","color":"black"}),
        slideshow,
     html.Div(  
            className="row",
            children=[
                html.Div(className="col-md-5",children=[
                html.P(className="text-blue",children=["But understanding how Rionegro municipal governments collects tax money shouldn’t be difficult."]),
                html.P(className="text-black1",children=["This powerful visualization tool gives you an unprecedented look into municipal government tax collection. Tabular data, charts and graphs will help researchers and policymakers see and understand government data with new perspectives. The tool provides different viewing options, including:"]),
                ]),
                html.Div(className="col-md-7",children=[
                html.P(className="text-black2",children=[
                    html.Span(className="text-red",children=["Overview: "]),
                    "Get a quick view of how will next year’s revenue for each tax and for each one of the most important categories."]),
                html.P(className="text-black2",children=[
                    html.Span(className="text-red",children=["Detailed Forecast: "]),
                    "Review individual payments, transaction dates, and get a deeper view of how the taxes collection will behave."]),
                html.P(className="text-black2",children=[
                    html.Span(className="text-red",children=["Geographical Analysis: "]),
                    "Select and compare the tax collection in the different geographical zones within the municipality."]),
                    html.P(className="text-black2",children=[
                    html.Span(className="text-red",children=["Sensitivity Analysis: "]),
                    "Solve here your what if answer. Test and see the possible the outcomes by changing certain variables for each tax."]),
                html.P(className="text-black2",children=[
                    html.Span(className="text-red",children=["The development Team  : "]),
                    "Take a look of the team that make this possible."]),
                ])

            ])
])
