from headers import HEADERS
import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com'

response = requests.get(url, headers=HEADERS)
response.raise_for_status
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
	for word in KEYWORDS:
		if word in article.text:
			data = article.find('time').attrs['title']
			title = article.find('h2').find('span')
			href = article.find(class_='tm-article-snippet__title-link').attrs['href']            
			link = url + href
			result = f'{data[0:10]} - {title.text.strip()} - {link}'
			print(result)
