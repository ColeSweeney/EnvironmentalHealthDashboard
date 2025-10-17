import pandas as pd
import numpy as np
import sqlite3
import requests
import plotly.express as px
import dash
from dash import dcc, html, Input, Output
import datetime
import os
#import geopandas as gpd


#fetch_data() # Calls air/water quality API or reads CSV
#process_data() #Cleans and merges pollution + health datasets
#calculate_risk_index() # Combines pollutants + health outcomes into a risk score
#plot_trends() #Time series + bar/choropleth map visualization
#filter_dashboard() # Filters by County, year, or pollutant



## AI !!! 



# Set up Dash app
app = dash.Dash(__name__)

# Connect to the database and fetch recent data
conn = sqlite3.connect("env_health.db")
query = """
SELECT date_utc, pm25
FROM air_quality
WHERE city = 'Indianapolis'
ORDER BY date_utc ASC
LIMIT 100
"""
df = pd.read_sql_query(query, conn)
conn.close()

# Create the figure
fig = px.line(
    df,
    x="date_utc",
    y="pm25",
    title="PM2.5 Levels in Indianapolis (Most Recent 100 Readings)",
    labels={"date_utc": "Date (UTC)", "pm25": "PM2.5 (µg/m³)"}
)

# Define layout
app.layout = html.Div([
    html.H1("Indianapolis Air Quality Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)