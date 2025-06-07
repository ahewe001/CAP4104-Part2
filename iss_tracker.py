import streamlit as st
import plotly.express as px
import json
import urllib.request
import pandas as pd


def track_iss():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    #saving the ISS location from the API response
    #extracting lat and log as float vals
    location = result["iss_position"]
    lat = float(location['latitude'])
    lon = float(location['longitude'])

    #creating df with lat, lon, label and color of iss position
    df = pd.DataFrame([{
        "lat": lat,
        "lon": lon,
        "label": "ISS🛰️",
        "color": "red"
    }])

    #creating scatter mapbox fig using plotly
    fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="label", color="color", color_discrete_map={"red": "red"})
    #updated layout to set map stype, zoom leve, center and to hide the legend
    fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=1, mapbox_center={"lat": lat, "lon": lon},showlegend=False)

    st.plotly_chart(fig)
