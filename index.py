from app import app
from layouts.main_layout import create_layout
from callbacks import sidebar_toggle


app.layout = create_layout()

if __name__ == "__main__":
    app.run_server(debug=True, port=8051)