import requests

def get_news_headlines(api_key, category="technology", country="us", max_articles=5):
    url = f"https://newsapi.org/v2/top-headlines?category={category}&country={country}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        headlines = [article["title"] for article in articles[:max_articles]]
        if not headlines:
            return ["No news articles found."]
        return headlines
    else:
        return ["Could not fetch news."]

# Example usage

# api_key = ""
# headlines = get_news_headlines(api_key)
# for idx, headline in enumerate(headlines, 1):
#     print(f"{idx}. {headline}")
