import streamlit as st
from apod import show_apod
from iss_tracker import track_iss
from exoplanet import exoplanet_chart
from quiz import quiz_questions
from articles import news

st.set_page_config(page_title="Explore the Universe", layout="wide")

st.sidebar.title("🔭 Explore the Universe")
selection = st.sidebar.radio("Choose a section:", [
    ":telescope: Explore the Universe Dashboard!",
    ":camera: Astronomy Picture of the Day",
    ":ringed_planet: Exoplanet Discovery",
    ":satellite: ISS Tracker",
    ":brain: Space Fact Quiz",
    ":newspaper: NASA Breaking News Feed"
])

# Main Layout
st.title(selection)

if selection == ":telescope: Explore the Universe Dashboard!":
    st.subheader(":rocket: Welcome to Explore the Universe! :stars:")
    st.write("This app is made for anyone curious about space and beyond!")
    st.write("")
    st.write("• :camera: Astronomy Picture of the Day: View NASA’s stunning daily image — and explore "
             "past APODs too!")
    st.write("• :ringed_planet: Exoplanet Explorer: Discover exoplanets and see which telescopes found "
             "them with interactive tables and discovery timeline charts.")
    st.write("•	:satellite: ISS Tracker: Follow the International Space Station in real time as it orbits Earth.")
    st.write("•	:brain: Cosmic Quiz: Test your space knowledge with our fun and interactive quiz!")
    st.write("•	:newspaper: Space News: Stay up to date with the latest breaking news in astronomy.")
    st.write("")
    st.write("Whether you're a casual stargazer or a future astrophysicist, we hope you enjoy your journey through the cosmos!")

elif selection == ":camera: Astronomy Picture of the Day":
    show_apod()

elif selection == ":ringed_planet: Exoplanet Discovery":
    st.subheader("About Exoplanets")
    st.write("Most of the exoplanets discovered so far are in a relatively small region of our "
             "galaxy, the Milky Way. (“Small” meaning within thousands of light-years of our solar system; "
             "one light-year equals 5.88 trillion miles, or 9.46 trillion kilometers.) Even the closest known "
             "exoplanet to Earth, Proxima Centauri b, is still about 4 light-years away. We know there are more "
             "planets than stars in the galaxy.")
    st.write("By measuring exoplanets’ sizes (diameters) and masses (weights), we can see compositions ranging "
             "from rocky (like Earth and Venus) to gas-rich (like Jupiter and Saturn). Some planets may be "
             "dominated by water or ice, while others are dominated by iron or carbon. We’ve identified lava "
             "worlds covered in molten seas, puffy planets the density of Styrofoam and dense cores of planets "
             "still orbiting their stars.")

    st.subheader("Timeline of Exoplanet Discoveries")
    exoplanet_chart()

elif selection == ":satellite: ISS Tracker":
    st.subheader("About the International Space Station.")
    st.write("The station was designed between 1984 and 1993. Elements of the station were in construction "
             "throughout the US, Canada, Japan, and Europe beginning in the late 1980s. The International "
             "Space Station Program brings together international flight crews, multiple launch vehicles, "
             "globally distributed launch and flight operations, training, engineering, and development "
             "facilities, communications networks, and the international scientific research community.")

    st.subheader("Real-Time ISS Tracker")
    track_iss()

elif selection == ":brain: Space Fact Quiz":
    st.subheader(":rocket: Test Your Cosmic Knowledge!")
    quiz_questions()

elif selection == ":newspaper: NASA Breaking News Feed":
    st.subheader("Find the most up-to-date news about space, NASA, and beyond!")
    news()
