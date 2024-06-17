import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from app import app
from pages import home, login, changepassword, generatereport, managers, members, reaffiliate, updatealum, updatemember, alumni, updatemem, add_alumni, help_me


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id="auth", data={'isAuthenticated': False}, storage_type="session"),
    dcc.Store(id="updater", data=0, storage_type="session"),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname'),
     Input('auth', 'data')]
)
def display_page(pathname, auth_data):
    if auth_data and auth_data.get('isAuthenticated'):
        if pathname in ('/', '/home'):
            return home.layout
        elif pathname == '/logout':
            return login.layout
        elif pathname == "/view-reports":
            return generatereport.layout, "/view-reports"
        elif pathname == "/managers":
            return managers.layout, "/managers"
        elif pathname == "/members":
            return members.layout, "/members"
        elif pathname == "/reaffiliate":
            return reaffiliate.layout, "/reaffiliate"
        elif pathname == "/update-alumni":
            return updatealum.layout, "/update-alumni"
        elif pathname == "/update-member":
            return updatemember.layout, "/update-member"
        elif pathname == "/alumni":
            return alumni.layout, "/alumni"
        elif pathname == '/update-member-modify':
            return updatemem.layout, '/update-member-modify'
        elif pathname == '/add_alumni':
            return add_alumni.layout, '/add_alumni'
        elif pathname == '/add_alumni':
            return add_alumni.layout, '/add_alumni'
        elif pathname == "/change-password":
            return changepassword.layout, "/change-password"
        elif pathname == "/help":
            return help_me.layout, "/help"
        
        else:
            return 'error404', '/error404'
    else:
        return login.layout

if __name__ == '__main__':
    app.run_server(debug=True)
