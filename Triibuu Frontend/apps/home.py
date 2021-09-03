import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app


slideshow = html.Div(
    className="row",
            children=[
                html.Div(className="col-md-1"),
                html.Div(className="col-md-3",children=[
                html.Img(className="img-center",src="/assets/home/Mapa.png",width="100%"),
                ]),
                html.Div(className="col-md-7",children=[
                    html.Section(id="slideshow", children=[
                        html.Div(id="slideshow-container", children=[
                            html.Div(id="image"),
                            dcc.Interval(id='interval', interval=2000)
                        ],style={"text-align":"left"})
                    ])
                ]),
                html.Div(className="col-md-1"),
            ]
)
                

@app.callback(Output('image', 'children'),
              [Input('interval', 'n_intervals')])
def display_image(n):
    if n == None or n % 3 == 1:
        img = html.Img(src="/assets/home/Img1 (1).jpg",style={"width":"100%","text-align":"center"})
    elif n % 3 == 2:
        img = html.Img(src="/assets/home/Img2 (1).jpg",style={"width":"100%","text-align":"center"})
    elif n % 3 == 0:
        img = html.Img(src="/assets/home/Img3 (1).jpg",style={"width":"100%","text-align":"center"})
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
                html.Div(className="col-md-1"),
                html.Div(className="col-md-10",children=[
                html.H5(style={"text-align":"center",'margin-top':'1.5rem'},children=[
                    "Rionegro is a city and municipality located in the sub-region of Eastern Antioquia, Colombia who is really interested in understand how their tax collection will behave."])
                ]),
                html.Div(className="col-md-1"),
            ]
),
    html.P(),
    html.Div(  
            className="row",
            children=[
                html.Div(className="col-md-1"),
                html.Div(className="col-md-4",children=[
                html.P(className="text-blue",children=["But understanding how Rionegro municipal governments collects tax money shouldn’t be difficult."]),
                html.P(className="text-black1",children=["This powerful visualization tool gives you an unprecedented look into municipal government tax collection. Tabular data, charts and graphs will help researchers and policymakers see and understand government data with new perspectives. The tool provides different viewing options, including:"]),
                ]),
                html.Div(className="col-md-6",children=[
                html.P(className="text-black2",children=[
                    html.Span(className="text-red",children=["Overview: "]),
                    "Get a quick view of how will next year’s revenue for each tax and for each one of the most important categories."]),
                html.P(className="text-black2",children=[
                    html.Span(className="text-red",children=["Detailed Forecast: "]),
                    "Review individual payments, transaction dates, and get a deeper view of how the taxes collection will behave."]),
                html.P(className="text-black2",children=[
                    html.Span(className="text-red",children=["Outliers Analysis: "]),
                    "Filter by categories, stratum, and taxpayers to identify outliers. This information can be used to check errors in taxation."]),
                    html.P(className="text-black2",children=[
                    html.Span(className="text-red",children=["Sensitivity Analysis: "]),
                    "Solve here your what if answer. Test and see the possible the outcomes by changing certain variables for property tax."]),
                html.P(className="text-black2",children=[
                    html.Span(className="text-red",children=["The development Team  : "]),
                    "Take a look of the team that make this possible."]),
                    html.Div(className="col-md-1"),
                ])

            ])
])
