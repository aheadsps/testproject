import datetime

import requests

from src.config import API_KEY, BASE_URL


def get_news(query: str, exclude_words: list, api_key: str = API_KEY) -> list:
    today = datetime.datetime.today()
    params = {
        "q": query,
        "from": today.strftime("%Y-%m-%d"),
        "sortBy": "publishedAt",
        "apiKey": api_key
    }
    try:
        response = requests.get(
            url=BASE_URL,
            params=params
        )

        news_data = response.json()
        print(news_data)

        if news_data.get("status") != "ok":
            return []

        articles_list = news_data.get('articles', [])
        print(articles_list)

        articles_result = []

        for article in articles_list:

            content = f"{article.get('title')} {article.get('content')}".lower()

            if any(word.lower() in content for word in exclude_words):
                continue

            articles_result.append(
                {
                    "title": article.get("title"),
                    "author": article.get("author"),
                    "description": article.get("content"),
                    "url": article.get("url"),
                }
            )

        return articles_result

    except requests.RequestException:
        return []
    except Exception:
        return []
