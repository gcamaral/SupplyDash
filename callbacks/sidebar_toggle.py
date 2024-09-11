from dash import Input, Output, State, callback

from components.sidebar import sidebar_expanded, sidebar_hidden

@callback(
    [Output("sidebar", "children"),
     Output("sidebar-toggle", "data"),
     Input("btn-toggle", "n_clicks"),
     State("sidebar-toggle", "data")]
)
def toggle_sidebar(n_clicks, is_open):
    if n_clicks:
        if is_open:
            return sidebar_hidden().children, False
        else:
            return sidebar_expanded().children, True
    return sidebar_expanded().children, True