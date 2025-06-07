import streamlit as st
import pandas as pd


def exoplanet_chart():
    #query for planet name, year found and telescope/facility using URL encoding
    ## FORMAT TO HELP REMEMBER
    # https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=YOUR_URL_ENCODED_QUERY&format=csv
    # spaces = +    commas = %2C
    # my query: SELECT pl_name, disc_year, disc_facility FROM ps
    # url encoded: SELECT+pl_name%2C+disc_year%2C+disc_facility+FROM+ps
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,disc_year,disc_facility+from+ps&format=csv"
    df = pd.read_csv(url)

    #create by dropping missing vals in year and facility
    df_dropna = df.dropna(subset=["disc_year", "disc_facility"])

    #sorting by each unique facility and turing year data type to str for better visuals
    disc_facility = sorted(df_dropna["disc_facility"].unique())
    df_dropna["disc_year"] = df_dropna["disc_year"].astype(str)

    #slider for choosing telescope to view data for
    telescope = st.selectbox("Select a telescope to view its discoveries:", disc_facility)
    #filtering the df by telescope, what was chosen on the slider will show on the table and chart
    filtered_df = df_dropna[df_dropna["disc_facility"] == telescope]

    #interactive table
    telescope_table = filtered_df.rename(columns={"pl_name": "Planet Name", "disc_year": "Discovery Year", "disc_facility": "Facility"})
    st.write(f"### Planet Discovery Table for {telescope}")
    st.write(telescope_table)

    #line chart that shows the linegraph of the filtered data
    single_telescope = filtered_df.groupby("disc_year").size().rename("single_telescope").sort_index()
    st.write(f"### Planet Discovery Line Chart for {telescope}")
    st.line_chart(single_telescope)

    #line chart showing all exoplanets found over time
    all_telescopes = df_dropna.groupby("disc_year").size().rename("all_telescopes").sort_index()
    st.write("### Timeline of Planet Discoveries Across All Telescopes")
    st.line_chart(all_telescopes)


