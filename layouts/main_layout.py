import dash_bootstrap_components as dbc
from dash import dcc
from components.header import create_header
from components.sidebar import sidebar_expanded
from components.content import create_content

def create_layout():
    return dbc.Container([
        dcc.Store(id="sidebar-toggle", data=True),
        dbc.Row([create_header()], style={'margin-bottom':'10px'}),
        dbc.Row(
            [
                sidebar_expanded(),
                dbc.Col(
                    [
                        create_content(),
                    ], width=10
                    ),
                ]
            ),
        ],
        fluid=True,
    )