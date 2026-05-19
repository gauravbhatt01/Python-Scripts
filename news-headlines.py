# Author: gauravdotbhatt
# Created: 06-10-2025
# Moto - go where your heart leads you. (.)=(.)

import requests
from typing import Dict, List

BASE_URL = "https://inshorts.com/api/en/search/trending_topics"

CATEGORIES = {
    "India": "india",
    "Business": "business",
    "Politics": "politics",
    "Sports": "sports",
    "Technology": "technology",
    "Startups": "startups",
    "Entertainment": "entertainment",
    "Hatke": "hatke",
    "International": "international",
    "Automobile": "automobile",
    "Science": "science",
    "Travel": "travel",
    "Miscellaneous": "miscellaneous",
    "Fashion": "fashion",
    "Education": "education",
    "Health_Fitness": "health___fitness",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}

def build_url(category: str) -> str:
    """
    Build API URL for a category.
    """
    return f"{BASE_URL}/{category}"

def check_api_health(categories: Dict[str, str]) -> None:
    """
    Check status code of all endpoints.
    """
    print("\n### Checking API Endpoint Health ###\n")

    for name, endpoint in categories.items():
        url = build_url(endpoint)
        try:
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=10
            )
            print(f"{name:<15} -> {response.status_code}")
        except requests.RequestException as e:
            print(f"{name:<15} -> ERROR: {e}")


def fetch_news(category: str, limit: int = 10) -> List[str]:
    """
    Fetch top news content from category.
    """

    url = build_url(category)
    params = {
        "page": 1,
        "type": "NEWS_CATEGORY"
    }
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        news_items = data.get("data", {}).get("suggested_news", [])
        headlines = []

        for item in news_items[:limit]:
            content = item.get("news_obj", {}).get("content")
            if content:
                headlines.append(content)
        return headlines
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Invalid JSON response")
    return []

def main():
    check_api_health(CATEGORIES)
    print("\n### Business News ###\n")
    news = fetch_news("business")
    for index, article in enumerate(news, start=1):
        print(f"{index}. {article}")
        print("-" * 50)

if __name__ == "__main__":
    main()
