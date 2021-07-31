import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from app import app

def presentation_card(name):
    card_main = dbc.Card(
        [
            dbc.CardImg(src="/assets/Person_blue.png", style={"height":"80px","width":"80px"},top=True, bottom=False,
                        alt='Photo not available',className = 'align-self-center'),
            dbc.CardBody(
                [
                    html.H2(name, className="card-title"),
                    html.H3("The description goes here.",className="card-text",
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
                html.H2("Our project", className="card-title",style={"text-align": "left"}),
                html.H3("The description of the project comes here. Related to DS4A or something like that.",className="card-text",
                ),
        ]
    ),
],
style={"margin-top": "1rem","margin-left": "0.5rem"},
outline=True,  # True = remove the block colors from the background and header
color="light"
)


layout = html.Div(
    [
    html.H1('About the development team', style={"textAlign": "left","color": "#dc4232"}),
    html.Div(  
            className="row",
            children=[
                html.Div(
                className="ten columns",children=[
                dbc.Row(
                        [
                            dbc.Col(presentation_card('Carlos Cardona')),
                            dbc.Col(presentation_card('David Cortés')),
                            dbc.Col(presentation_card('José Parra')),
                            dbc.Col(presentation_card('Julián Egaz')),
                        ]
                    ),
                dbc.Row(
                        [
                            dbc.Col(presentation_card('Laura Ocampo')),
                            dbc.Col(presentation_card('Santiago Tellez')),
                            dbc.Col(presentation_card('Vatsaid Molano')),
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
