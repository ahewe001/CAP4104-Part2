import streamlit as st
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

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

def choose_date(select_date_str):

    API_KEY = "sRddXE8lvetVntnhdqbvrkUXgU1qcH0FQLbAUC8T"
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={select_date_str}"

    try:
        response = requests.get(url)
        data = response.json()

        st.markdown("---")
        date = datetime.strptime(data["date"], "%Y-%m-%d")
        st.markdown(f"#### APOD for date: {date}")
        media_type = data.get("media_type")
        title = data.get("title")
        st.markdown(f"### {title}")
        if media_type == "image":
            st.image(data["url"], caption=data.get("title", ""), use_container_width=True)
        elif media_type == "video":
            st.video(data["url"], caption=data.get("title", ""), use_container_width=True)
        else:
            st.warning("Unsupported media type.")
        explanation = data.get("explanation", "No explanation provided.")
        st.write(explanation)

    except Exception as e:
        st.error("Failed to load APOD. Please try again later.")
        st.exception(e)


def show_apod():
    # start/end dates for APODs
    form = st.form(key="apod-form")
    with form:
        st.subheader("Choose a date for APODs or see today's APOD below!")
        select_date = form.date_input("Start date", value=datetime.now().date())

        # NASA str format
        today = datetime.now().date()
        button = form.form_submit_button("Get APODs")
        if button:
            if select_date is None:
                st.write("Please enter a date (YYYY/MM/DD) within the past 10 years!")
            else:
                if select_date > today:
                    st.error("You are trying to select a date in the future! Science hasn't made it that far yet!")
                select_date_str = select_date.strftime("%Y-%m-%d")
                if select_date_str == today:
                    apod_today()
                else:
                    choose_date(select_date_str)
        else:
            st.markdown("---")
            apod_today()
