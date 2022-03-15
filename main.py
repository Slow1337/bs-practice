import requests
from bs4 import BeautifulSoup
from pprint import pprint
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}
response = requests.get('https://habr.com/ru/all/')
text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
# pprint(articles)
for article in articles:
    article_preview_data = article.find(class_='tm-article-snippet')
    for keyword in KEYWORDS:
        if keyword in article_preview_data:
            date = article.find(class_='tm-article-snippet__datetime-published').text.strip()
            article_name = article.find(class_='tm-article-snippet__title-link').find('span').text.strip()
            link = article.find(class_='tm-article-snippet__title-link').attrs['href']
            url = f'https://habr.com{link}'
            print(date, article_name, url)
        else:
            pass
