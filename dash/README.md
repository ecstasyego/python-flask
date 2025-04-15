```python
from flask import Flask, redirect, url_for
import dash
from dash import html

server = Flask(__name__)

dashApp = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix="/dashboard/"
)
dashApp.layout = html.Div([
    html.H1("Hello from Dash inside Flask!"),
])



@server.route('/')
def home():
    return 'Welcome to Flask Home! <a href="/dashboard/">Go to Dashboard</a>'

if __name__ == "__main__":
    server.run(debug=True)
```
