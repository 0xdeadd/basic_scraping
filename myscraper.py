#!/usr/bin/env python3

import sqlite3
import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect('quotes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote TEXT
)
''')

def scrape_quotes(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch the page.")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Finding all the quotes using the correct HTML tag and class for the website you're scraping
    quotes = soup.find_all('span', class_='text')

    for quote in quotes:
        cursor.execute("INSERT INTO quotes (quote) VALUES (?)", (quote.text,))
        print(quote.text)
    
    conn.commit()

if __name__ == "__main__":
    url = "http://quotes.toscrape.com"  # The URL you want to scrape
    scrape_quotes(url)

conn.close()

