import dash
import dash_bootstrap_components as dbc
import hashlib
from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from app import app
from apps import dbconnect as db
from dash.exceptions import PreventUpdate


layout = html.Div(
    [
        dcc.Store(id='account_id_store', storage_type='session', data=0),  # Store user ID
        html.Video(
            src='/assets/login_bg.mp4',
            autoPlay=True,
            loop=True,
            muted=True,
            style={
                'position': 'fixed',
                'width': '100%',
                'height': '100%',
                'object-fit': 'cover',
                'z-index': '-1',
            }
        ),
        html.Div(
            [
                html.Img(
                    src='/assets/login_title.png',
                    style={
                        'max-width': '28vw',
                        'display': 'block',
                    },
                ),
            ],
            style={
                'position': 'fixed',
                'left': '8rem',  # Position the title image to the left of the screen
                'top': '8rem',  # Position the title image above the login card
                'z-index': '1',
            }
        ),
        html.Div(
            [
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H2("LOG IN", className="card-title fw-bolder"),
                            html.Br(),

                            dbc.Alert(id='login_alert', is_open=False),
                            dbc.Input(id='uname', type='text', className='input', placeholder='Username'),
                            html.Br(),

                            dbc.Input(type='password', id='pword', className='input', placeholder='Password'),
                            html.Br(),

                            dbc.Checklist(
                                options=[{"label": "Show Password", "value": 1}],
                                value=[],
                                id="show_pword",
                                inline=True,
                            ),
                            html.Br(),
                            dbc.Row(
                                dbc.Col(
                                    dbc.Button("Log in", color="primary", className="loginbutton", id='login_loginbtn'),
                                    width={'size': 4, 'offset': 8},
                                    className="d-flex justify-content-end"
                                )
                            ),
                        ],
                        className='half left',
                        style={
                            'background-color': 'rgba(255, 255, 255, 0.0)',  # 50% transparent background color
                        }
                    ),
                    className='flex small',
                    style={
                        'width': '35%',
                        'position': 'fixed',
                        'left': '8rem',  # Position the card to the left of the screen
                        'top': '16rem',  # Position the card below the title image
                        'padding': '3rem',
                        'border-radius': '20px',
                        'box-shadow': '0px 0px 10px rgba(0, 0, 0, 0.2)',
                        'background-color': 'rgba(255, 255, 255, 0.3)',  # 50% transparent background color
                    }
                ),
            ],
        ),
    ],
    style={
        'position': 'fixed',
        'width': '100%',
        'height': '100%',
        'overflow': 'hidden',  # Ensure the content does not overflow the background
    }
)


@app.callback(
    [
        Output('login_alert', 'color'),
        Output('login_alert', 'children'),
        Output('login_alert', 'is_open'),
        Output('auth', 'data'),  # Update auth data upon successful login
    ],
    [
        Input('login_loginbtn', 'n_clicks'), 
    ],
    [
        State('uname', 'value'),
        State('pword', 'value'), 
        State('auth', 'data'),  # Retrieve auth data
    ]
)
def loginprocess(loginbtn, username, password, auth_data):    
    ctx = callback_context
    if ctx.triggered:
        alert_open = False 
        alert_color = ""
        alert_text = ""

        eventid = ctx.triggered[0]['prop_id'].split('.')[0] 
        
        if eventid == 'login_loginbtn':
            if loginbtn and username and password:
                
                sql = """
                SELECT  account_password
                FROM user_account
                WHERE
                    user_name = %s 
                """
                            
                encrypt_string = lambda string: hashlib.sha256(string.encode('utf-8')).hexdigest()
                values = [username]
                cols = ['account_password']

                df = db.querydatafromdatabase(sql, values, cols)
                if df.shape[0]:
                    auth_data['isAuthenticated'] = True  # Set isAuthenticated to True upon successful login
                    alert_color = 'success'
                    alert_text = 'Successfully logged in.'
                    alert_open = True
                else:
                    alert_color = 'danger'
                    alert_text = 'Incorrect username or password.'
                    alert_open = True
            
        return [alert_color, alert_text, alert_open, auth_data]
    else:
        raise PreventUpdate


@app.callback(
    Output('pword', 'type'),
    [Input('show_pword', 'value')]
)
def toggle_password_visibility(checked_values):
    if checked_values:
        return 'text'
    else:
        return 'password'
