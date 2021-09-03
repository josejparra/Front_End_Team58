import dash_html_components as html
import dash_bootstrap_components as dbc

ALC_RIONEGRO_LOGO = "https://rionegro.gov.co/wp-content/themes/rionegro/img/logo-rionegro.svg"
CORRELATION_LOGO="https://www.correlation-one.com/hubfs/c1logo_color.png"
DS4A_LOGO='/assets/logo/DS4A.png'
TRIIBU_LOGO='/assets/logo/Horizontal BN.png'
MINTIC_LOGO='/assets/logo/MinTIC_Colombia.svg'

def Navbar():
    navbar = html.Div(className="row",children=[
        html.Div(className="col-md-3",style={'text-align':'center'},children=[
            html.Img(className="img-center",src=TRIIBU_LOGO,width="60%"),
            html.Img(className="img-center",src=DS4A_LOGO,width="90%"),
        ],),
        html.Div(className="col-md-6",style={'text-align':'center'},children=[
            html.H1("Taxes Revenue Forecast Dashboard"),
            html.H2('Cohort 5 - Team 58', style={"textAlign": "Center","color":"#204772"}),
        ],),
        html.Div(className="col-md-3",style={'text-align':'center'},children=[
            html.Img(className="img-center",src=ALC_RIONEGRO_LOGO,width="70%"),
            html.Img(className="img-center",src=MINTIC_LOGO,width="70%")
        ],),
    ],)
    return navbar

