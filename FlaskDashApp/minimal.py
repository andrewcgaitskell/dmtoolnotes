from dash import Dash
from dash import dcc
from dash import html

app = Dash(
    __name__,
    external_stylesheets=['/static/style.css'],
    ##external_scripts=external_scripts,
    routes_pathname_prefix='/dash/'
)

app.layout = html.Div('minimal dash app', id='example-div-element')


if __name__ == '__main__':
    app.run_server(debug=True)
