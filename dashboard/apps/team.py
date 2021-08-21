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
                    html.H5("The description goes here.",className="card-text",
                    ),
            ]
        ),
    ],
    style={"width": "20rem","margin-top": "2rem","margin-left": "0.5rem"},
    outline=True,  # True = remove the block colors from the background and header
    color="light"
    )
    return card_main

card_project = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Our project", className="card-title",style={"text-align": "left"}),
                html.H5("Data Science for All is a program offers a unique opportunity to learn data science from the world’s foremost experts.",className="card-text",
                ),
        ],style={"width":"100%"}
    ),
],
style={"margin-top": "1rem","margin-left": "0.5rem"},
outline=True,  # True = remove the block colors from the background and header
color="light"
)


layout = html.Div(
    [
    html.H2('About the development team', style={"textAlign": "left"}),
    html.Div(  
            className="row",
            children=[
                html.Div(className="col-md-9",children=[
                dbc.Row(
                    [
                            dbc.Col(presentation_card('Carlos Cardona',"/assets/team/Carlos.jpeg")),
                            dbc.Col(presentation_card('David Cortés',"/assets/team/DavidLCortesMurcia")),
                            dbc.Col(presentation_card('José Parra',"/assets/team/Jose.jpeg")),
                            dbc.Col(presentation_card('Julián Egaz',"/assets/team/Julian.jpeg")),
                        ]
                    ),
                dbc.Row(
                        [
                            dbc.Col(presentation_card('Laura Ocampo',"/assets/team/Laura")),
                            dbc.Col(presentation_card('Santiago Tellez',"/assets/team/Santiago")),
                            dbc.Col(presentation_card('Vatsaid Molano',"/assets/team/Vatsa")),
                            dbc.Col(),
                        ]
                    )
                ]),
                html.Div(
                    id="project_description_container",
                    className="two columns",
                    children=[
                            html.Div(
                                card_project,
                            )
                    ],
                )              
    ]),

    # html.Div(
    #         id="team_description_container",
    #         children=[
    #             html.Div(
    #                 dbc.Row(
    #                     [
    #                         dbc.Col(presentation_card('Carlos Cardona')),
    #                         dbc.Col(presentation_card('David Cortés')),
    #                         dbc.Col(presentation_card('José Parra')),
    #                         dbc.Col(presentation_card('Julián Egaz')),
    #                     ]
    #                 )
    #             ),
    #              html.Div(
    #                 dbc.Row(
    #                     [
    #                         dbc.Col(presentation_card('Laura Ocampo')),
    #                         dbc.Col(presentation_card('Santiago Tellez')),
    #                         dbc.Col(presentation_card('Vatsaid Molano')),
    #                         dbc.Col(),
    #                     ]
    #                 ),

    #             ),

    #             html.Div(
    #                 id="project_description_container",
    #                 children=[
    #                         html.Div(
    #                             dbc.Col(card_project),
    #                         )
    #                         ],
    #             ),
    #         ],
    #     ),

])
