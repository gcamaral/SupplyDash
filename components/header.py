import dash_bootstrap_components as dbc

def create_header():
    return dbc.NavbarSimple(
        brand="Home",
        brand_href="#",
        color="primary",
        dark=True
    )