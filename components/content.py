from dash import html
def create_content():
    return html.Div(
        [
            html.H3("Main Content Area"),
            html.P("This is the content of the page."),
        ],
        id="page-content"
    )