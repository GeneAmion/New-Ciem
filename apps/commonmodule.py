from dash_iconify import DashIconify as di
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from datetime import datetime
import dash_bootstrap_components as dbc
# Importing your app definition from app.py so we can use it
from app import app
top=dbc.NavbarSimple(
    
    brand="UPCIEM",
    style={"max-width":"100vw","justify-content":"space-between",'margin-left':'3dvw','height':'7dvh'},
    class_name='shadow-bottom',
    id='page-bar'
)
@app.callback(
    Output("page-bar",'brand'),
    [
    Input('url','pathname')]
)
def page_name(pathname):
    if pathname == '/' or pathname == '/home':
        return "Home"
    elif pathname=="/change-password":
        return "Change Password"
    elif pathname=="/view-reports":
        return "Reports"
    elif pathname=="/managers":
        return "Managers"
    elif pathname=="/members":
        return "Members"
    elif pathname=="/reaffiliate":
        return "Reaffiliation"
    #elif pathname=="/update-alumni":
        #return "Update Alumni Status"
    #elif pathname=="/update-member":
        #return "Update Member Status"
    elif pathname=="/alumni":
         return "Alumni"
    elif pathname=='/update-member-modify':
        return "Update Member Status"
    elif pathname=="/profile":
        return "Profile"
    raise PreventUpdate

navigation=dbc.Nav(
    [
       dbc.Container([
           dbc.NavbarBrand([html.Img(src='/assets/logo.png',style={"width":"2.8dvw",'display':'inline'}),dbc.Label("UP CIEM: BLUEPRINT",style={'padding-left':'0.5em','font-size':'0.8em'})], style={"display":"block","width":"100%",'color':'white'}),
            dbc.NavItem(dbc.NavLink([html.Img(src='/assets/icons8-home-96.png',className='icon'),dbc.Label("Home",style={'padding-left':'1.3em'})], id='link-home',active=True, href="/home",class_name='linked'),class_name='nav-item-custom'),
            dbc.NavItem(dbc.NavLink([html.Img(src='/assets/icons8-writer-male-96.png',className='icon'),dbc.Label("Reaffiliation",style={'padding-left':'1.3em'})], id='link-reaff',active=True, href="/reaffiliate",class_name='linked'),class_name='nav-item-custom'),
            dbc.NavItem(dbc.NavLink([html.Img(src='/assets/icons8-people-96.png',className='icon'),dbc.Label("Members",style={'padding-left':'1.3em'})],id='link-member', active=True, href="/members",class_name='linked'),class_name='nav-item-custom'),
            dbc.NavItem(dbc.NavLink([html.Img(src='/assets/icons8-graduate-96.png',className='icon'),dbc.Label("Alumni",style={'padding-left':'1.3em'})], id='link-alum',active=True, href="/alumni",class_name='linked'),class_name='nav-item-custom'),
            #dbc.NavItem(dbc.NavLink([di(icon='fluent:phone-update-24-regular',inline=True,),dbc.Label("Update Member Status",style={'padding-left':'1.3em'})], id='link-update-member',active=True, href="/update-member",class_name='linked'),class_name='nav-item-custom'),
            #dbc.NavItem(dbc.NavLink([di(icon='material-symbols:system-update',inline=True,),dbc.Label("Update Alumni Status",style={'padding-left':'1.3em'})],id='link-update-alum', active=True, href="/update-alumni",class_name='linked'),class_name='nav-item-custom'),
            dbc.NavItem(dbc.NavLink([html.Img(src='/assets/icons8-report-96.png',className='icon'),dbc.Label("Generate Report",style={'padding-left':'1.3em'})], id='link-reports',active=True, href="/view-reports",class_name='linked'),class_name='nav-item-custom'),
        
       ],style={'padding':'0'}),
       dbc.Container([
           dbc.NavItem(dbc.NavLink([html.Img(src='/assets/icons8-help-64.png',className='icon'),dbc.Label("Help",style={'padding-left':'1.3em'})], id='link-help',active=True, href="/help",class_name='linked'),class_name='nav-item-custom'),
            dbc.NavItem(dbc.NavLink([html.Img(src='/assets/icons8-password-key-96.png',className='icon'),dbc.Label("Change Password",style={'padding-left':'1.3em'})], id='link-password',active=True, href="/change-password",class_name='linked'),class_name='nav-item-custom'),
            dbc.NavItem(dbc.NavLink([html.Img(src='/assets/icons8-logout-96.png',className='icon'),dbc.Label("Logout",style={'padding-left':'1.3em'})], id='link-out',active=True, href="/logout",class_name='linked'),class_name='nav-item-custom'),
            
       ],style={'padding':'0'})
       ],
    vertical='lg',
    class_name='side-nav'
)
@app.callback(
    [
        Output('link-home','class_name'),
        Output('link-reaff','class_name'),
        Output('link-member','class_name'),
        Output('link-alum','class_name'),
        #Output('link-update-member','class_name'),
        #Output('link-update-alum','class_name'),
        Output('link-reports','class_name'),
        Output('link-help','class_name'),
        Output('link-password','class_name'),

    ],
    Input('url','pathname')
)
def selected_menu(pathname):
    if pathname == '/' or pathname == '/home':
        return "linked-selected",'linked','linked','linked','linked','linked','linked'
    elif pathname=="/change-password":
        return "linked",'linked','linked','linked','linked','linked','linked-selected'
    elif pathname=="/view-reports":
        return "linked",'linked','linked','linked','linked-selected','linked','linked'
    elif pathname=="/members":
        return 'linked',"linked",'linked-selected','linked','linked','linked','linked'
    elif pathname=="/reaffiliate":
        return 'linked',"linked-selected",'linked','linked','linked','linked','linked'
    elif pathname=="/update-alumni":
        return 'linked','linked','linked','linked-selected','linked','linked','linked'
    elif pathname=="/update-member":
        return 'linked','linked','linked-selected','linked','linked','linked','linked'
    elif pathname=="/alumni":
         return 'linked',"linked",'linked','linked-selected','linked','linked','linked'
    elif pathname=='/update-member-modify':
        return "linked",'linked','linked','linked-selected','linked','linked','linked'
    elif pathname=="/profile":
        return 'linked','linked','linked','linked','linked','linked-selected','linked'
    raise PreventUpdate
