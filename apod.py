import streamlit as st
import requests
from datetime import datetime

def apod_today():
    API_KEY = "sRddXE8lvetVntnhdqbvrkUXgU1qcH0FQLbAUC8T"
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date"
    response = requests.get(url)
    data = response.json()

    #try block
    try:
        st.write(f"#### APOD for date: {data['date']}")
        media_type = data.get("media_type")
        title = data.get("title")
        st.markdown(f"### {title}")
        if media_type == "image":
            st.image(data["url"], caption=data.get("title", ""), use_container_width=True)
        elif media_type == "video":
            st.video(data["url"], caption=data.get("title", ""), use_container_width=True)
        else:
            st.warning("Unsupported media type.")
        #is there an explanation
        explanation = data.get("explanation", "No explanation provided.")
        st.write(explanation)

    except Exception as e:
        st.error("Failed to load APOD. Please try again later.")
        st.exception(e)

def choose_date(date_start_str, date_end_str):

    API_KEY = "sRddXE8lvetVntnhdqbvrkUXgU1qcH0FQLbAUC8T"
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&start_date={date_start_str}&end_date={date_end_str}"

    try:
        response = requests.get(url)
        data = response.json()

        for item in data:
            st.markdown("---")
            st.markdown(f"#### APOD for date: {item['date']}")
            media_type = item.get("media_type")
            title = item.get("title")
            st.markdown(f"### {title}")
            if media_type == "image":
                st.image(item["url"], caption=item.get("title", ""), use_container_width=True)
            elif media_type == "video":
                st.video(data["url"], caption=item.get("title", ""), use_container_width=True)
            else:
                st.warning("Unsupported media type.")
            explanation = item.get("explanation", "No explanation provided.")
            st.write(explanation)

    except Exception as e:
        st.error("Failed to load APOD. Please try again later.")
        st.exception(e)


def show_apod():
    # start/end dates for APODs
    form = st.form(key="apod-form")
    with form:
        st.subheader("Choose a date range for APODs or see today's APOD below!")
        date_start = form.date_input("Start date", value=datetime.now().date())
        date_end = form.date_input("End date", value=datetime.now().date())

        # NASA str format
        date_start_str = date_start.strftime("%Y-%m-%d")
        date_end_str = date_end.strftime("%Y-%m-%d")
        today = datetime.now().date()
        button = form.form_submit_button("Get APODs")
        if date_start > today or date_end > today:
            st.error("You are trying to select a date in the future! Science hasn't made it that far yet!")
        else:
            if button:
                if date_start_str == today and date_end_str == today:
                    #today's APOD
                    apod_today()
                else:
                    #date range APOD
                    choose_date(date_start_str, date_end_str)
            else:
                st.markdown("---")
                apod_today()
