import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash import dash_table
from app import app
from apps import commonmodule as cm
from apps import dbconnect as db
import pandas as pd

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
                                class_name='d-flex align-items-center'
                            ),
                        ],
                        className="g-3",
                        style={"width": "100%"}
                    ),
                ], class_name='py-3'),

                dbc.Container(["No Members to Display"], id="mem-table", class_name='table-wrapper p-3')
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
                person.valid_id,
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
            WHERE (upciem_member_id IS NOT NULL AND upciem_member_delete IS NULL OR upciem_member_delete = FALSE)
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
        print(sql, alum_name)
        cols = ["ID", "Name", "Birthday", "Membership", "App Batch", "Year Standing", "Degree Program", "Other Orgs", "Email", "Present Address"]
        df = db.querydatafromdatabase(sql, values, cols)

        if not df.empty:
            df['ID'] = df['ID'].apply(lambda x: f'<a href="/add_alumni?mode=toalum&id={x}"><button class="btn btn-primary btn-sm">Move to Alumni</button></a>')
            table = dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i, 'presentation': 'markdown'} if i == 'ID' else {'name': i, 'id': i} for i in df.columns],
                markdown_options={'html': True},
                style_cell={
                    'text-align': 'center',
                    'font-family': 'Arial, sans-serif',
                    'font-size': '14px',
                    'color': '#000000',
                    'height': '40px',
                    'padding': '10px',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'maxWidth': 0
                },
                style_header={
                    'background-color': '#000097',  # Blue background for header
                    'color': 'white',  # White text for header
                    'text-align': 'center',
                    'font-family': 'Arial, sans-serif',
                    'font-size': '16px',
                    'font-weight': 'bold',
                    'border-bottom': '2px solid #dee2e6',  # Border for separation
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
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                },
                page_action='native',
                page_size=10,
                style_table={'height': '80%', 'overflow': 'auto'}
            )
            return [table]
        return ["No Members to Display"]
    raise PreventUpdate

