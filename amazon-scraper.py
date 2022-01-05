import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://www.amazon.com/Best-Sellers-Books-Big-Data/zgbs/books/6524631011')

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all(class_='zg-item-immersion')

for book in books:
    rank = book.find(class_='zg-badge-text').get_text()
    img_src = book.a.img['src']
    title = book.a.img['alt']
    book_format = book.find(class_='a-size-small a-color-secondary').get_text()
    price = book.find(class_='p13n-sc-price').get_text()
    stars = book.find(class_='a-icon-row a-spacing-none').get_text().strip()[0:18]
    reviews = book.find(class_='a-icon-row a-spacing-none').get_text().strip()[20:]
    author = book.find(class_=['a-size-small a-link-child', 'a-size-small a-color-base']).get_text()
    print(author)


# for item in soup.select('.item'):
#     print(item.get_text())