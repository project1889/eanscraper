'''
EAN scraper implementation.
'''
import requests
from bs4 import BeautifulSoup
class EANScraper:
    def scrape_brand(self, brand_name):
        results = []
        websites = [
            {
                'name': 'Website 1',
                'url': f'https://example1.com/search?brand={brand_name}',
                'ean_selector': 'div.ean',
                'title_selector': 'h2.title',
                'price_selector': 'span.price'
            },
            {
                'name': 'Website 2',
                'url': f'https://example2.com/search?brand={brand_name}',
                'ean_selector': 'div.ean',
                'title_selector': 'h2.title',
                'price_selector': 'span.price'
            },
            # Add more websites as needed
        ]
        for website in websites:
            url = website['url']
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                ean_elements = soup.select(website['ean_selector'])
                title_elements = soup.select(website['title_selector'])
                price_elements = soup.select(website['price_selector'])
                for ean_element, title_element, price_element in zip(ean_elements, title_elements, price_elements):
                    ean = ean_element.text.strip()
                    title = title_element.text.strip()
                    price = price_element.text.strip()
                    results.append({
                        'website': website['name'],
                        'ean': ean,
                        'title': title,
                        'price': price
                    })
            except Exception as e:
                print(f"Error scraping website {website['name']}: {e}")
        return results