import dash_bootstrap_components as dbc
from dash import html

def sidebar_expanded():
    return dbc.Col(
        html.Div(
            [
                # Botão de acionamento no canto esquerdo superior do sidebar
                dbc.Button(">", id="btn-toggle", outline=True, size="sm", color="primary", className="mb-2"),

                # Conteúdo do sidebar
                html.H2("Menu", className="display-4"),
                html.Hr(),
                dbc.Nav(
                    [
                        dbc.NavLink("Home", href="#", active="exact"),
                        dbc.NavLink("Página 1", href="#", active="exact"),
                        dbc.NavLink("Página 2", href="#", active="exact")
                    ],
                    vertical=True,
                    pills=True,
                ),
            ],
            style={"padding":"15px"}
        ),
        width=2,
        id="sidebar",
        style={"background-color": "#f8f9fa", "transition":"width 0.5s ease", "height": "100vh"}
    )

def sidebar_hidden():
    return dbc.Col(
        html.Div(
            # Botão de acionamento quando a sidebar é recolhida (somente o botão permanece visível)
            dbc.Button("<", id="btn-toggle", outline=True, size="sm", color="primary", className="mb-2")
        ),
        width=1, # A largura da side bar recolhida pode ser ajustada
        id="sidebar",
        style={"background-color": "#f8f9fa", "transition":"width 0.5s ease", "height": "100vh"}
    )