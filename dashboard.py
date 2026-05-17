import dash
from dash import dcc, html, dash_table
import plotly.graph_objects as go
import pandas as pd
import numpy as np

revenues_final = pd.read_csv('revenues_final.csv')
revenues_clean = pd.read_csv('revenues_clean.csv')
benford_df = pd.read_csv('benford_comparison.csv')
outliers_df = pd.read_csv('outliers.csv')
duplicates_df = pd.read_csv('duplicates.csv')

app = dash.Dash(__name__)

benford_chart = go.Figure()
benford_chart.add_trace(go.Bar(x=benford_df['digit'], y=benford_df['expected_pct'], name="Expected (Benford)", marker_color='steelblue'))
benford_chart.add_trace(go.Bar(x=benford_df['digit'], y=benford_df['actual_pct'], name="Actual (2025 Q4)", marker_color='coral'))
benford_chart.update_layout(
    title="Benford's Law: Expected vs Actual First Digit Distribution",
    xaxis_title="First Digit",
    yaxis_title="Percentage (%)",
    barmode='group',
    plot_bgcolor='white'
)

# ── Layout ────────────────────────────────────────────────────────────────────
app.layout = html.Div(style={'fontFamily': 'Arial', 'padding': '30px', 'backgroundColor': '#f9f9f9'}, children=[

    html.H1("Audit Analytics Dashboard — SEC Revenues 2025 Q4",
            style={'textAlign': 'center', 'color': '#2c3e50'}),

    html.Hr(),

    # Summary cards
    html.Div(style={'display': 'flex', 'gap': '20px', 'marginBottom': '30px'}, children=[
        html.Div(style={'background': 'white', 'padding': '20px', 'borderRadius': '8px',
                        'flex': 1, 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}, children=[
            html.H3("Total Companies", style={'color': 'steelblue'}),
            html.H2(f"{revenues_final['name'].nunique():,}")
        ]),
        html.Div(style={'background': 'white', 'padding': '20px', 'borderRadius': '8px',
                        'flex': 1, 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}, children=[
            html.H3("Outliers Flagged", style={'color': 'coral'}),
            html.H2(f"{len(outliers_df)}")
        ]),
        html.Div(style={'background': 'white', 'padding': '20px', 'borderRadius': '8px',
                        'flex': 1, 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}, children=[
            html.H3("Duplicate Filings", style={'color': 'orange'}),
            html.H2(f"{len(revenues_clean[revenues_clean['duplicate_flag']==True])}")
        ]),
        html.Div(style={'background': 'white', 'padding': '20px', 'borderRadius': '8px',
                        'flex': 1, 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}, children=[
            html.H3("Digit 1 Deviation", style={'color': '#8e44ad'}),
            html.H2(f"{round(benford_df['actual_pct'][0] - 30.1, 2)}%")
        ]),
    ]),

    # Benford chart
    html.Div(style={'background': 'white', 'padding': '20px', 'borderRadius': '8px',
                    'marginBottom': '30px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}, children=[
        dcc.Graph(figure=benford_chart)
    ]),

    # Outliers table
    html.Div(style={'background': 'white', 'padding': '20px', 'borderRadius': '8px',
                    'marginBottom': '30px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}, children=[
        html.H3("Outlier Flagged Companies (Z-Score > 3)"),
        dash_table.DataTable(
            data=outliers_df.to_dict('records'),
            columns=[{'name': c, 'id': c} for c in outliers_df.columns],
            style_cell={'textAlign': 'left', 'padding': '10px'},
            style_header={'backgroundColor': 'steelblue', 'color': 'white', 'fontWeight': 'bold'},
            style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': '#f2f2f2'}]
        )
    ]),

    # Duplicates table
    html.Div(style={'background': 'white', 'padding': '20px', 'borderRadius': '8px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}, children=[
        html.H3("Duplicate Revenue Filings Detected"),
        dash_table.DataTable(
            data=duplicates_df.to_dict('records'),
            columns=[{'name': c, 'id': c} for c in duplicates_df.columns],
            style_cell={'textAlign': 'left', 'padding': '10px'},
            style_header={'backgroundColor': 'orange', 'color': 'white', 'fontWeight': 'bold'},
            style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': '#f2f2f2'}]
        )
    ]),
])

if __name__ == '__main__':
    app.run(debug=True)