import requests

def get_news_headlines(api_key, is_online, category="technology", country="us", max_articles=5):
    if is_online:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&country={country}&apiKey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            headlines = [article["title"] for article in articles[:max_articles]]
            if not headlines:
                return ["No news articles found."]
            return headlines
    return ["I could not fetch news without internet connection"]
