from dash_iconify import DashIconify as di
from dash import html, dash_table, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from apps import dbconnect as db
from app import app
import pandas as pd

# Assuming cm provides navigation and top components
from apps import commonmodule as cm

layout = html.Div([
    cm.navigation,
    cm.top,
    html.Div([
        dbc.Card(
            [
                dbc.Container([
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.FormFloating(
                                    [
                                        dbc.Input(type="text", placeholder="Enter Name", id="alum-name"),
                                        dbc.Label("Search Name"),
                                    ]
                                ),
                                width=6,
                            ),
                            dbc.Col(
                                [
                                    dbc.Label("Filter by: ", style={"padding-right": "1em"}),
                                    dbc.Select(
                                        id="filter-select",
                                        options=[
                                            {"label": "Member Type", "value": "membership_type"},
                                            {"label": "Year Standing", "value": "year_standing"},
                                            {"label": "App Batch", "value": "app_batch"},
                                            {"label": "Accountabilities", "value": "other_org_affiliation", "disabled": True},
                                        ],
                                    ),
                                    dbc.Input(type="text", placeholder="Filter", id="prof-filter"),
                                ],
                                width=6,
                                class_name='flex part-3 center-align'
                            ),
                        ],
                        className="g-7",
                        style={"width": "100%"}
                    ),
                ], class_name='flex '),

                dbc.Container(id="mem-table", class_name='table-wrapper')
            ],
            class_name="custom-card"
        )
    ], className='body')
])

@app.callback(
    Output('mem-table', 'children'),
    [Input('url', 'pathname'),
     Input('alum-name', 'value'),
     Input('filter-select', 'value'),
     Input('prof-filter', 'value')]
)
def mem_pop(pathname, alum_name, filter_select, prof_filter):
    if pathname == "/members":
        sql = """ 
            SELECT 
                upciem_member.upciem_member_id,
                CONCAT(first_name, ' ', middle_name, ' ', last_name, ' ', suffix) AS full_name,
                birthdate,
                membership_type,
                app_batch,
                year_standing,
                degree_program,
                other_org_affiliation,
                email,
                present_address
            FROM person 
            LEFT JOIN upciem_member ON person.valid_id = upciem_member.valid_id 
            LEFT JOIN affiliation ON person.valid_id = affiliation.valid_id 
            WHERE (upciem_member_delete IS NULL OR upciem_member_delete = FALSE)
        """
        values = []
        if alum_name:
            sql += " AND CONCAT(first_name, ' ', middle_name, ' ', last_name, ' ', suffix) ILIKE %s"
            values.append(f"%{alum_name}%")

        if filter_select and prof_filter:
            if filter_select == "year_standing":
                sql += " AND year_standing = %s"
                values.append(prof_filter)
            else:
                sql += f" AND {filter_select} ILIKE %s"
                values.append(f"%{prof_filter}%")
        
        cols = ["ID", "Name", "Birthday", "Membership", "App Batch", "Year Standing", "Degree Program", "Other Orgs", "Email", "Present Address"]
        df = db.querydatafromdatabase(sql, values, cols)
        
        if df.shape[0] > 0:  # Check if DataFrame has rows
            df['Action'] = [f'<a href="/add_alumni?mode=edit&id={id}" ><Button class="lbtn">Edit</Button></a>' for id in df['ID']]
            table = dash_table.DataTable(
                data=df.to_dict('records'),  # Convert DataFrame to list of dictionaries
                columns=[{'name': i, 'id': i, 'presentation': 'markdown'} if i == 'Action' else {'name': i, 'id': i} for i in df.columns],  # Specify column names and IDs
                markdown_options={'html': True},
                style_cell={
                    "height": "50px",
                    'text-align': 'left',
                    "background-color": "#EEF2FA",
                    "color": "#273250",
                },
                style_header={
                    "background-color": "#000097",
                    "color": "#FFF",
                    "text-align": "center",
                    "border-bottom": "4px solid white",
                },
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': '#f8f9fa'  # Light grey for odd rows
                    },
                    {
                        'if': {'row_index': 'even'},
                        'backgroundColor': '#ffffff'  # White for even rows
                    },
                ],
                page_action='native',
                page_size=10,
                style_table={"height": "80%", 'overflow': 'hidden'}
            )
            return [table]
        
        return ["No Members to Display"]
    
    raise PreventUpdate
