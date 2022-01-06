import requests
from bs4 import BeautifulSoup
from csv import writer
from datetime import datetime


response = requests.get('https://www.amazon.com/Best-Sellers-Books-Big-Data/zgbs/books/6524631011')

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all(class_='zg-item-immersion')

with open('book_rankings.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['book_ranking', 'book_title', 'book_price', 'date']
    csv_writer.writerow(headers)

    for book in books:
        rank = book.find(class_='zg-badge-text').get_text()
        title = book.a.img['alt']
        price = book.find(class_='p13n-sc-price').get_text()
        date = datetime.today().strftime('%Y-%m-%d')
        csv_writer.writerow([rank, title, price, date])


with open('books.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['book_title', 'book_author', 'book_format', 'book_img_src',
               'num_of_stars', 'num_of_reviews']
    csv_writer.writerow(headers)

    for book in books:
        title = book.a.img['alt']
        author = book.find(class_=['a-size-small a-link-child', 'a-size-small a-color-base']).get_text()
        book_format = book.find(class_='a-size-small a-color-secondary').get_text()
        img_src = book.a.img['src']
        stars = book.find(class_='a-icon-row a-spacing-none').get_text().strip()[0:18]
        reviews = book.find(class_='a-icon-row a-spacing-none').get_text().strip()[20:]
        csv_writer.writerow([title, author, book_format, 
                             img_src, stars, reviews])


with open('calendar_date.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['date', 'year', 'month_num', 'month_name',
               'day_num', 'day_name']
    csv_writer.writerow(headers)

    for book in books:
        date = datetime.today().strftime('%Y-%m-%d')
        year = datetime.today().strftime('%Y')
        month_num = datetime.today().strftime('%m')
        month_name = datetime.today().strftime('%B')
        day_num = datetime.today().strftime('%d')
        day_name = datetime.today().strftime('%A')
        csv_writer.writerow([date, year, month_num,
                             month_name, day_num, day_name])




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
