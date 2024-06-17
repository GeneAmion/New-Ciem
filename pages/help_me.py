from dash_iconify import DashIconify as di
from dash import html
from apps import commonmodule as cm
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from datetime import datetime
import dash_bootstrap_components as dbc
from app import app

layout=html.Div([
        cm.navigation,
        cm.top,
        html.Div([
            html.Div([
            dbc.Card([
                dbc.CardHeader("Access the User Manual at this link:", class_name='flex'),
                dbc.CardBody([
                    dbc.Container([
                        dbc.Row(html.A("BLUEPRINT USER MANUAL", href="https://docs.google.com/document/d/18yn3-3cCLMZqjCliEXs9IFPj6c0PGOHTNOq8U-1BgRo/edit?usp=sharing", target="blank"), style={'font-size':"3em"}),
                
                ], class_name='flex homeshow')
                
            ]),
            html.Img(src='/assets/manual_page.png'),]),
            dbc.CardFooter(
            [
                        dbc.Row(dbc.Label("For any concerns, please contact the developers at:")),
                        html.Br(),
                    
                        dbc.Row("Klarenz Ballon - knballon@up.edu.ph"),
                        dbc.Row("Andre Genesis Cabasag - abcabasag@up.edu.ph"),
                        dbc.Row("Ma. Roxette Rojas - mmrojas@up.edu.ph")]
            ,class_name='flex homeshow')
            
                
                        
                        
                    
    
                        
                        ],className='body')
                    ],className='flex body-container'),
                    ])