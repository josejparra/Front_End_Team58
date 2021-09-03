import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
from app import server



# Connect to your app pages
from apps import navbar, overview, outliers, forecast, sensitivity, team, home

tabs_layout=dbc.Nav(
            [
                dbc.NavLink([
                    html.Div(className="row",children=[
                        html.Div(className="col-md-3 my-auto",children=[
                            html.Img(className="img-fluid",src="/assets/icons/Home.svg",width="30px")
                            ]),
                        html.Div(className="col-md-9 my-auto",children=[
                            html.Div(className="navigation",children=["Home"])
                            ])
                        ])
                    ],style={"width":"10%","text-decoration": "none"},href="/", active="exact"),
                dbc.NavLink([
                    html.Div(className="row",children=[
                        html.Div(className="col-md-3 my-auto",children=[
                            html.Img(className="img-fluid",src="/assets/icons/Eye.svg",width="30px")
                            ]),
                        html.Div(className="col-md-9 my-auto",children=[
                            html.Div(className="navigation",children=["Overview"])
                            ])
                        ])
                    ],style={"width":"12%","text-decoration": "none"},href="/overview", active="exact"),
                dbc.NavLink([
                    html.Div(className="row",children=[
                        html.Div(className="col-md-3 my-auto",children=[
                            html.Img(className="img-fluid",src="/assets/icons/Pie.svg",width="30px")
                            ]),
                        html.Div(className="col-md-9 my-auto",children=[
                            html.Div(className="navigation",children=["Detailed Forecast"])
                            ])
                        ])
                    ],style={"width":"20%","text-decoration": "none"},href="/detailed_analysis", active="exact"),
                dbc.NavLink([
                    html.Div(className="row",children=[
                        html.Div(className="col-md-3 my-auto",children=[
                            html.Img(className="img-fluid",src="/assets/icons/Outlier.svg",width="30px")
                            ]),
                        html.Div(className="col-md-9 my-auto",children=[
                            html.Div(className="navigation",children=["Outliers Analysis"])
                            ])
                        ])
                    ],style={"width":"20%","text-decoration": "none"},href="/outliers_analysis", active="exact"),
                dbc.NavLink([
                    html.Div(className="row",children=[
                        html.Div(className="col-md-3 my-auto",children=[
                            html.Img(className="img-fluid",src="/assets/icons/Bar.svg",width="30px")
                            ]),
                        html.Div(className="col-md-9 my-auto",children=[
                            html.Div(className="navigation",children=["Sensitivity Analysis"])
                            ])
                        ])
                    ],style={"width":"18%","text-decoration": "none"},href="/sensitivity", active="exact"),
                dbc.NavLink([
                    html.Div(className="row",children=[
                        html.Div(className="col-md-3 my-auto",children=[
                            html.Img(className="img-fluid",src="/assets/icons/Person.svg",width="30px")
                            ]),
                        html.Div(className="col-md-9 my-auto",children=[
                            html.Div(className="navigation",children=["The development Team"])
                            ])
                        ])
                    ],style={"width":"20%","text-decoration": "none"},href="/team", active="exact"),
            ],
            pills=True,
        )

content = html.Div(id="page-content")

app.layout = html.Div([dcc.Location(id="url"), navbar.Navbar(),tabs_layout,content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/overview":
        return overview.layout
    elif pathname == "/detailed_analysis":
        return forecast.layout
    elif pathname == "/outliers_analysis":
        return outliers.layout
    elif pathname == "/sensitivity":
        return sensitivity.layout
    elif pathname == "/team":
        return team.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=False)
