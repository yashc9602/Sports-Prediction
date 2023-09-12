import streamlit as st
from newsapi import NewsApiClient

# Replace 'YOUR_NEWS_API_KEY' with your actual News API key
newsapi = NewsApiClient(api_key='97b70534bdc54e10b54383c146b4990c')

def get_sports_news(category):
    response = newsapi.get_top_headlines(category=category, language='en', country='us', page_size=5)
    return response['articles']

def main():
    st.title("Sports News")

    categories = ["sports", "entertainment", "health", "technology", "science"]
    selected_category = st.selectbox("Select a category", categories)

    news = get_sports_news(selected_category)
    for article in news:
        st.subheader(article['title'])
        st.write(article['description'])
        st.image(article['urlToImage'])
        st.write(f"Source: {article['source']['name']}")
        st.write(f"Published At: {article['publishedAt']}")
        st.write(f"Read more: [{article['title']}]({article['url']})")
        st.markdown("---")
