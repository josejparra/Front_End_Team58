import dash_html_components as html
import dash_bootstrap_components as dbc

ALC_RIONEGRO_LOGO = "https://rionegro.gov.co/wp-content/themes/rionegro/img/logo-rionegro.svg"

def Navbar():
    navbar = html.Div(className="row",children=[
        html.Div(className="col-md-3 my-auto",children=[
            html.Img(className="img-fluid",src="https://rionegro.gov.co/wp-content/themes/rionegro/img/logo-rionegro.svg",width="100%")
        ],),
        html.Div(className="col-md-6",children=[
            html.H1("Taxes Revenue Forecast Dashboard",style={"white-space": "nowrap","text-align":"left"})
        ],),
        html.Div(className="col-md-3 my-auto",children=[
            html.Img(className="img-fluid",src="https://www.correlation-one.com/hubfs/c1logo_color.png",width="100%")
        ],),
    ],)
    return navbar

