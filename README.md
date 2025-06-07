# Project for CAP4104 Part Two

This is a project for the Human-Computer Interaction Course at FIU.

## Description

This project is a data-driven web application developed using the Streamlit framework, designed to demonstrate key human-computer interaction (HCI) principles and usability goals.

The web application built for this project is interactive and informative by providing content about space and space-related news. It integrates data from multiple NASA APIs to deliver real-time updates, astronomical insights, and multimedia content. Additionally, it features a custom space-themed quiz via a CSV dataset.

## Usability Goals

The goals I set for my app were to make the navigation easy, for it to be informative but not overwhelming, and to maintain a visually appealing design. I addressed these by:

- Simplifying Navigation: I organized content into clear, distinct sections accessible through a sidebar menu and intuitive buttons. This allows users to find information quickly without confusion. 
- Effectiveness and Efficiency: Users can complete their tasks accurately, completely and with minimal effort.
- Consistent Visual Design: I applied a clean and consistent color scheme and spacing to create a pleasant user experience.
- Learnability: Users can easily understand how ot use the app without steep learning curves.
- Responsive Feedback: Interactive elements like buttons and forms provide immediate visual feedback, confirming user actions and improving engagement.

By focusing on these usability goals, the app strives to balance of information with ease of use and appeal.

## Design Process

I began by researching available APIs and carefully selecting data that would best provide the information and interactivity users would find engaging. For example, I chose the quiz feature and the Astronomy Picture of the Day (APOD) to offer both educational content and daily inspiration. Knowing that I wanted to include a real-time feed of the International Space Station, I also decided to show how exoplanets were discovered and which telescopes made those discoveries, adding depth and context for space enthusiasts. Throughout the design, I kept users in mind - aiming to create an experience that is informative, interactive, and meaningful.

## Integrations

This web app integrates multiple data sources, including CSV files, RSS feeds, and APIs, to providing a rich and interactive user experience.

### API

I used several NASA APIs, including the Exoplanet Archive API to provide detailed information on discovered exoplanets, the ISS API to show a real-time tracker of the International Space Station, and the Astronomy Picture of the Day (APOD) API to display images.

### RSS Feeds

I integrated NASA's news RSS feed to deliver breaking space and astronomy news articles, keeping users up to date with the latest discoveries and events.

### CSVs

I created a CSV file that contains space-related quiz questions, gathered from NASA resources and astronomy texts, to offer an educational and interactive feature within the app.

## Interactive Widgets 

The app incorporates several interactive widgets designed to enhance user engagement and provide smooth navigation:

### APOD Page

- Date input: Allows users to select a specific date or date range for viewing the Astronomy Picture of the Day.
- Submit button: Confirms the date selection and loads the corresponding APOD.

### Exoplanet Discovery Page

- Slider: Lets users select a telescope to view how many exoplanets it has discovered, dynamically updating the displayed data.

### Space Quiz

- Text input: Users can enter their name to personalize the quiz experience.
- Checkbox: Option to show or hide the user’s current quiz score.
- Radio buttons: Allow users to select their answer from multiple-choice options.
- Submit button: Submits the selected answer and provides immediate feedback.
- Next question button: Moves to the following quiz question

## HCI Principles

This app incorporates key Human-Computer Interaction principles to enhance usability and user satisfaction:

- User Feedback: Clear error or success indicators and status messages keep users informed about ongoing processes, such as selecting a date from the future for the APOD or a correct answer in the quiz.

- Consistency : The app maintains uniform layouts, fonts, and color schemes across all pages, helping users learn and predict interactions easily.

- Flexibility and efficiency of use: Both novices and experienced users can navigate the app smoothly with intuitive controls and shortcuts, such as date pickers and filters.

## Conclusion

This web app successfully integrates data sources to provide an engaging platform for exploring information about space. By applying thoughtful usability goals and HCI principles, it balances rich content with an intuitive and visually appealing interface. Users can learn, interact, and stay informed through dynamic features like quizzes, real-time trackers, and news feeds. 

Future improvements could include:
    - Implementing a login system to allow users to save their quiz scores linked to their user ID. 
    - Expanding the app to feature more detailed information about our solar system (such as images and data for each planet) would enrich the learning experience. 
    - Adding interactive tables showcasing historic space events, including rocket launches and satellite deployments, would provide deeper insights for users interested in space history. 
    - To enhance accessibility, options to adjust text size and color themes could be introduced, making the app more usable for a wider range of users.

## Getting Started

### Dependencies

- Python 3.8 or higher
- The project uses a virtual environment (venv) for package management.
- Required Python packages (listed in requirements.txt):
    - streamlit
    - pandas
    - requests
    - plotly
    - feedparser


### Installing

Clone this repository:
```
git clone https://github.com/ahewe001/CAP4104-Part2.git
cd CAP4104-Part2
```

Install dependencies:
```
pip install -r requirements.txt
```
## Executing

Run the web app with:
```
streamlit run app.py
```

## Authors

Abigayle Hewett

ahewe001@fiu.edu
