import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import openpyxl

headers = {
    'user-agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/84.0.4147.105 Safari/537.36'
    )
}

def fetch_page(url):
    try:
        page = requests.get(url, headers=headers, timeout=10)
        page.raise_for_status()
        return page
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def get_soup(page):
    return BeautifulSoup(page.text, 'html.parser') if page else None

def extract_titles(soup):
    return [title.text.strip() for title in soup.find_all('h3', class_='wd-entities-title')]

def extract_prices(soup):
    return [price.text.strip() for price in soup.find_all('span', class_='price')]

def extract_images(soup):
    return [img.get('href') for img in soup.find_all('a', class_='product-image-link')]

def clean_price(price_text):
    
    original = re.search(r'₹?([\d,]+).*Original', price_text)
    current = re.search(r'₹?([\d,]+)(Current)', price_text)
    discount = re.search(r'Save:\s*(\d+%)', price_text)
    
    return (
        original.group(1) if original else None,
        current.group(1) if current else None,
        discount.group(1) if discount else None
    )

def make_dataframe(titles, prices, images):
    data = []
    for title, price_text, image in zip(titles, prices, images):
        original, current, discount = clean_price(price_text)
        data.append({
            'Book name': title,
            'Original Price': original,
            'Current Price': current,
            'Discount': discount,
            'Product Image': image
        })
    return pd.DataFrame(data)

def fetch_all_pages(base_url, pages=1):
    results = []
    for i in range(1, pages+1):
        url = f"{base_url}?product-page={i}"
        page = fetch_page(url)
        soup = get_soup(page)
        if soup:
            titles = extract_titles(soup)
            prices = extract_prices(soup)
            images = extract_images(soup)
            df = make_dataframe(titles, prices, images)
            results.append(df)
    return pd.concat(results, ignore_index=True) if results else pd.DataFrame()

def main():
    base_url = 'https://padhegaindia.in/pi-book-utsav/'
    df = fetch_all_pages(base_url, pages=3)  # scrape first 3 pages
    df.to_excel("padhega-india.xlsx", sheet_name="Sheet1")

if __name__ == '__main__':
    main()
