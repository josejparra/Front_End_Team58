import dash_html_components as html
import dash_bootstrap_components as dbc

ALC_RIONEGRO_LOGO = "https://rionegro.gov.co/wp-content/themes/rionegro/img/logo-rionegro.svg"

def Navbar():
    navbar = dbc.Navbar(
        html.A(
        [           
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                    dbc.Col(html.Img(src=ALC_RIONEGRO_LOGO, className="img-fluid")),
                    dbc.Col(dbc.NavbarBrand("Taxes Revenue Dashboard", #className="ml-2",
                        style={"width": "10","font-weight": "bold","font-size":32,"font-family":"Helvetica","color":"#204772","align":"center"}),style={"width":10}),
                    ],
                    align="center",
                    no_gutters=True
                ),
            
        ]
    ),style={"border-bottom": "#204772 solid 4px"}
    )
    return navbar

    
"""
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/index")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Wine Dash",
        color="primary",
        dark=True,
    )
    return navbar
"""