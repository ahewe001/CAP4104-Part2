import feedparser
import streamlit as st

def news():
    #RSS URL form NASA
    rss_url = "https://www.nasa.gov/rss/dyn/breaking_news.rss"

    #feed the parser the URL to get articles
    feed = feedparser.parse(rss_url)
    #st.write(feed.feed.keys())
    #pull first 5 articles
    for entry in feed.entries[:5]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.summary)
        st.markdown(f"[Read more]({entry.link})", unsafe_allow_html=True)
        st.markdown("---")

