import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from app import app

def presentation_card(name,route):
    card_main = dbc.Card(
        [
            dbc.CardImg(src=route, style={"width":"80%"},top=True, bottom=False,
                        alt='Photo not available',className = 'align-self-center'),
            dbc.CardBody(
                [
                    html.H4(name, className="card-title",style={"text-align":"center"}),
                    #html.H5("The description goes here.",className="card-text"),
            ]
        ),
    ],
    style={"width": "20rem","margin-top": "2rem"},#,"margin-left": "0.5rem"},
    outline=True,  # True = remove the block colors from the background and header
    color="light"
    )
    return card_main

card_project = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Our project", className="card-title",style={"text-align": "left"}),
                html.H5("""
                This project was developed as part of the *Data Science for All 2021 Cohort 5, for the Rionegro Major's office to
                 provide a tool to analyze and forecast the property and business tax collection.
                The analysis presented and the moldels builded are based on tax appraisal and collection between the years 2001 to 2020.

                *Data Science for All is a program offers a unique opportunity to learn data science from the world’s foremost experts.
                """,className="card-text",
                ),
        ],style={"width":"100%"}
    ),
],
style={"margin-top": "1rem"},#"margin-left": "0.5rem"},
outline=True,  # True = remove the block colors from the background and header
color="light"
)


layout = html.Div(
    [
    html.H2('About the development team', style={"textAlign": "left"}),
    html.Div(  
            className="row",
            children=[
                html.Div(className="col-md-1"),
                html.Div(className="col-md-8",children=[
                html.H5('This is the amazing interdisciplinary team who develop this tool.',style={'margin-top':'1.5rem'}),
                html.Div(className="row",
                children=[
                            html.Div(className="col-md-3",children=[presentation_card('Carlos Cardona',"/assets/team/Carlos.jpeg")]),
                            html.Div(className="col-md-3",children=[presentation_card('David Cortés',"/assets/team/DavidLCortesMurcia")]),
                            html.Div(className="col-md-3",children=[presentation_card('José Parra',"/assets/team/Jose.jpeg")]),
                            html.Div(className="col-md-3",children=[presentation_card('Julián Egaz',"/assets/team/Julian.jpeg")]),
                        ]
                    ),
                html.Div(className="row",
                children=[
                            html.Div(className="col-md-3",children=[presentation_card('Laura Ocampo',"/assets/team/Laura")]),
                            html.Div(className="col-md-3",children=[presentation_card('Santiago Tellez',"/assets/team/Santiago")]),
                            html.Div(className="col-md-3",children=[presentation_card('Vatsaid Molano',"/assets/team/Vatsa")]),
                            html.Div(className="col-md-3")
                        ]
                    )
                ]),
                html.Div(
                    id="project_description_container",
                    className="col-md-3",
                    children=[
                            html.Div(
                                card_project, style={"margin-left":"0","margin-right":"2rem"}
                            )
                    ],
                ),
                #html.Div(className="col-md-1"),              
    ]),
])
