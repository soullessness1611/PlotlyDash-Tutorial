from dash import Dash, html, dcc

app = Dash(__name__)

markdown_text = """
### Dash and Markdown
Dash apps can be written in Markdown.
Dash uses the [CommonMar](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorila](http://commonmark.org/help/)
if this is your first intriduction to Markdown!
"""

app.layout = html.Div([dcc.Markdown(children=markdown_text)])

if __name__ == "__main__":
    app.run(debug=True)
