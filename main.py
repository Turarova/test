# import requests
# from bs4 import BeautifulSoup as BS

# base_url = 'https://24.kg'

# def get_soup(url):
#     if url.startswith('https'):
#         html = requests.get(url).text
#     else:
#         html = requests.get(base_url + url).text

#     soup = BS(html, 'html.parser')
#     return soup

# def get_categories():
#     soup = get_soup(base_url)
#     cat_block = soup.find('ul', {'class': 'nav navbar-nav'})
#     a_tags = cat_block.find_all('a')
#     return [tag.get('href') for tag in a_tags]

# def get_news_title(cat_url):
#     soup = get_soup(base_url + cat_url)
#     title_divs = soup.find_all('div', {'class': 'one'})
#     return [div.find('a').get('href') for div in title_divs]

# def get_news_article(news_url):
#     soup = get_soup(news_url)
#     article_block = soup.find('div', {'itemprop': 'articleBody'})
#     if article_block:
#         return article_block.text

# def main():
#     all_news = []

#     # получаем список с ссылками на все категории
#     categories_urls = get_categories()
#     # проходимся по каждой ссылке
#     for category_url in categories_urls:
#         print(category_url)
#         # получаем все заголовки по данной категории
#         news_urls = get_news_title(category_url)
#         for n_url in news_urls:
#             # получаем текст одной новости
#             res_text = get_news_article(n_url)
#             all_news.append(res_text)

#     return all_news

# print(main())



# PARSING TASK2
# import requests
# from bs4 import BeautifulSoup
# import lxml
# source = requests.get('http://www.example.com/').text
# my_page = BeautifulSoup(source, 'lxml')
# print('h1: ', my_page.h1.text)
# print('p: ', my_page.p.text)
# print('a: ', my_page.find('a').get('href'))

# TASK3
# import requests
# from bs4 import BeautifulSoup
# import lxml
# source = requests.get('https://www.wikipedia.org/').text
# de = BeautifulSoup(source, 'lxml')
# res = de.find(id="js-link-box-de")
# print(res.strong.text)
# print(res.small.text)

# TASK4
# import requests
# from bs4 import BeautifulSoup
# import lxml
# def getTitle(url):
#     source = requests.get(url).text
#     soup = BeautifulSoup(source, 'lxml')
#     if soup.h1:
#         return soup.h1.text
#     else:
#         return 'Title could not be found'

# print('<h1>',getTitle('http://www.example.com/'),'</h1>')


# TASK5
# import requests
# from bs4 import BeautifulSoup
# import lxml
# source = requests.get('https://www.makers.kg').text
# soup = BeautifulSoup(source, 'lxml')
# t = soup.find_all('h3', 'feature-cards-card-info-title')
# for x in t:
#     print(x.text)