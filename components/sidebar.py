import dash
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL
import dash_bootstrap_components as dbc

import json
import pandas as pd
from components import modal_novo_processo, modal_novo_advogado, modal_advogados
from app import app

# Layout
layout = dbc.Container([
    modal_novo_processo.layout,
    modal_novo_advogado,
    modal_advogados,
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1('Luzo', style={'color': 'white'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.H3('Aki', style={'color': 'white'})
            ]),
        ]),
    ], style={'padding-top': '50px', 'margin-bottom': '100px'}, className='text-center'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dbc.Nav([
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), "\tINÍCIO"], href="/home", active=True, style={'text-align': 'left'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-plus-circle dbc'), "\tPROCESSOS"],id='processo_button', active=True, style={'text-align': 'left'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-user-plus dbc'), "\tADVOGADOS"], id='lawyers_button', active=True, style={'text-align':'left'}))
            ],vertical='lg', pills=True, fill=True)
        ])
    ])
], style={'height': '100%', 'padding': '0px','position':'sticky', 'top':0, 'background-color': '#232423'})