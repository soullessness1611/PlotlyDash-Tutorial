from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
)

# Create a Dash app
app = Dash(__name__)

# Define the layout
app.layout = html.Div(
    [
        html.H1(children="Title of Dash App", style={"textAlign": "center"}),
        dcc.Dropdown(df.country.unique(), "Thailand", id="dropdown-selection"),
        dcc.Graph(id="graph-content"),
    ]
)


# Define the callback
@callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x="year", y="pop")


if __name__ == "__main__":
    app.run(debug=True)
