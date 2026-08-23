import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")
        
        scraped_data = []
        for quote, author in zip(quotes, authors):
            scraped_data.append({
                "quote": quote.text,
                "author": author.text
            })
        return scraped_data
    return []

if __name__ == "__main__":
    results = scrape_quotes()
    for item in results[:3]:
        print(f"Quote: {item['quote']} - By: {item['author']}")
