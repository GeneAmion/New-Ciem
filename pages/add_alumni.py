import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from dash.exceptions import PreventUpdate
from datetime import datetime
from app import app
from apps import commonmodule as cm
from apps import dbconnect as db
from dash_iconify import DashIconify as di


# Define the form layout

add_alumni_form = dbc.Form(
    [
        html.H5(html.B('Personal Information')),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "First Name ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='alumfirst_name', value='', disabled=False),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Middle Name ",
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='alummiddle_name', disabled=False),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Surname ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='alumlast_name', disabled=False),
                    width=6,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Suffix ",
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='alumsuffix', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "ID Number ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='alumvalid_id', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Birthday ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="date", id='alumbirthdate', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),

        html.Br(),
        html.H5(html.B('Contact Information')),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Contact Number ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='alumcontact_number',
                              placeholder="09XXXXXXXXX", maxLength=11, disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Emergency Contact Number ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3),
                dbc.Col(
                    dbc.Input(type="text", id='emergency_alumcontact_number',
                              placeholder="09XXXXXXXXX", maxLength=11, disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Email Address ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dbc.Input(type="email", id='alumemail', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Present Address ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dbc.Input(type="text", id='alumpresent_address', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Permanent Address ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dbc.Input(type="text", id='alumpermanent_address', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),

        html.Br(),
        html.H5(html.B('Specialization')),
        dbc.Row(
            [
                html.P('You may choose from the dropdown menu or manually input your specialization if not in the options. You may also select more than one.'),
                dbc.Col(
                    dbc.InputGroup(
                        [
                            dcc.Dropdown(
                                id='specialization-dropdown',
                                options=[
                                    {'label': 'Operations Research', 'value': 'Operations Research'},
                                    {'label': 'Supply Chain Management', 'value': 'Supply Chain Management'},
                                    {'label': 'Ergonomics', 'value': 'Ergonomics'},
                                    {'label': 'Information Technology', 'value': 'Information Technology'},
                                    {'label': 'Quality Control', 'value': 'Quality Control'},
                                    {'label': 'Finance', 'value': 'Finance'},
                                    {'label': 'Industrial Design', 'value': 'Industrial Design'},
                                    {'label': 'Academe', 'value': 'Academe'}
                                ],
                                multi=True,
                                placeholder="Select specialization",
                                style={'width': '80%'}
                            ),
                            dbc.Input(id='other-specialization', type='text', placeholder='Other specialization', style={'display': 'none'})
                        ]
                    ),
                ),
            ],
            className="mb-2",
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Label(
                    [
                        "Remarks ",
                        html.Span("*", style={"color": "#F8B237"})
                    ],
                    width=3
                ),
                dbc.Col(
                    dbc.Input(type="text", id='remarks', disabled=False),
                    width=4,
                ),
            ],
            className="mb-2",
        ),

        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button("Submit", id="alumsubmit-button", color="primary", className="mb-3", style={'display': 'none'}),
                    width={"size": 6, "offset": 3}
                )
            ],
        ),
        dbc.Button('Submit',id='alumsubmit-button'),
        html.Div(id='alumoutput-message'),  # For displaying output messages
        html.Br(),
        html.Br(),
    ]
)





layout = html.Div([
    cm.navigation,
    cm.top,
    html.Div([
        html.Div([
        dbc.Card([
            dbc.CardHeader("ADD ALUMNI FORM", className='flex'),
            dbc.CardBody([
                dbc.Container(
                    [
                        add_alumni_form,
                    ]
                )
                  ]),
                ])
                ]) 
    ], className='body')
        ])

@app.callback(
    Output('alumoutput-message', 'children'),
    [Input('alumsubmit-button', 'n_clicks')],
    [State('alumfirst_name', 'value'),
     State('alummiddle_name', 'value'),
     State('alumlast_name', 'value'),
     State('alumsuffix', 'value'),
     State('alumvalid_id', 'value'),
     State('alumbirthdate', 'value'),
     State('alumcontact_number', 'value'),  # Fixing the ID here
     State('emergency_alumcontact_number', 'value'),
     State('alumemail', 'value'),
     State('alumpresent_address', 'value'),
     State('alumpermanent_address', 'value'),
     State('specialization', 'value'),
     State('remarks', 'value')
     ]
)
def submit_form(n_clicks, alumfirst_name, alummiddle_name, alumlast_name, alumsuffix, alumvalid_id, alumbirthdate, alumcontact_number,
                emergency_alumcontact_number, alumemail, alumpresent_address, alumpermanent_address, specialization, remarks):
    if n_clicks is None:
        raise PreventUpdate

    if not (alumfirst_name and alumlast_name and alumvalid_id and alumbirthdate and alumcontact_number and emergency_alumcontact_number and alumemail and alumpresent_address and alumpermanent_address and specialization ):
        return html.Div("Please fill in all required fields.", style={'color': 'red'})

    try:
        # Check if the person already exists
        sql = "SELECT valid_id FROM person WHERE valid_id=%s"
        df = db.querydatafromdatabase(sql, [alumvalid_id], ['valid_id'])

        if df.shape[0]:
            print(df)  # Check the DataFrame returned by the query
            print(df.shape)  # Check the shape of the DataFrame
            # Update existing person's information
            sql = """
                UPDATE person
                SET
                    first_name=%s,
                    middle_name=%s,
                    last_name=%s,
                    suffix=%s,
                    birthdate=%s,
                    contact_number=%s,
                    emergency_contact_number=%s,
                    email=%s,
                    present_address=%s,
                    permanent_address=%s

            """
            if alummiddle_name is None:
                alummiddle_name=''
            if alumsuffix is None:
                alumsuffix=''
            values = [alumfirst_name, alummiddle_name, alumlast_name, alumsuffix, alumbirthdate, alumcontact_number, emergency_alumcontact_number, alumemail, alumpresent_address, alumpermanent_address]
            sql+=" WHERE valid_id='{alumvalid_id}';"
            db.modifydatabase(sql, values)
            
            # Update SPECIALIZATION information
            sql = """
                UPDATE alumni 
                SET 
                    specialization=%s
                    
                WHERE valid_id=%s
            """
            values = [specialization,alumvalid_id]
            db.modifydatabase(sql, values)
            
            message = "Existing member information updated successfully."
        else:
            # Insert new person
            sql = """
            INSERT INTO person(valid_id, first_name, middle_name, last_name, suffix, birthdate, contact_number, emergency_contact_number, email, present_address, permanent_address)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values = [alumvalid_id, alumfirst_name, alummiddle_name, alumlast_name, alumsuffix, alumbirthdate, alumcontact_number, emergency_alumcontact_number, alumemail, alumpresent_address, alumpermanent_address]
            db.modifydatabase(sql, values)
            sql="INSERT INTO alumni(valid_id,specialization) VALUES (%s,%s)"
            values=[alumvalid_id,specialization]
            db.modifydatabase(sql, values)
            #Adding to upciem_member
            message = "New alumni successfully added."

        return html.Div(message, style={'color': 'green'})

    except Exception as e:
        return html.Div(f"An error occurred: {str(e)}", style={'color': 'red'})
