import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale
import json
import pprint
from sqlalchemy.dialects.postgresql import JSONB, insert 


DSN = 'postgresql://postgres:1990@localhost:5432/projectshop'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

name1 = Publisher(name_publish = 'Пушкин')

b1 = Book(title_book = 'Капитанская дочка', publisher = name1)
b2 = Book(title_book = 'Руслан и Людмила', publisher = name1)
b3 = Book(title_book = 'Борис Годунов', publisher = name1)
b4 = Book(title_book = 'Евгений Онегин', publisher = name1)
b5 = Book(title_book = 'Пиковая дама', publisher = name1)
session.add_all([b1, b2,b3,b4,b5])

s1 = Shop(shop_id = 1, shop_name = "Буквоед")
s2 = Shop(shop_id = 2, shop_name = "Лабиринт")
s3 = Shop(shop_id = 3, shop_name = "Книжный дом")
s4 = Shop(shop_id = 4, shop_name = "Читай город")
s5 = Shop(shop_id = 5, shop_name = "Книгозор")
session.add_all([s1, s2,s3,s4,s5])

st1 = Stock(count_stock = 1, shop = s1, book = b1)
st2 = Stock(count_stock = 5, shop = s2, book = b2)
st3 = Stock(count_stock = 7, shop = s3, book = b3)
st4 = Stock(count_stock = 4, shop = s4, book = b4)
st5 = Stock(count_stock = 3, shop = s5, book = b5)
session.add_all([st1, st2,st3,st4,st5])

sl1 = Sale(price_sale = "600", date_sale = "09-11-2022", count_sale = 16, stock  = st1)
sl2 = Sale(price_sale = "500", date_sale = "08-11-2022", count_sale = 10, stock  = st2)
sl3 = Sale(price_sale = "580", date_sale = "05-11-2022", count_sale = 9, stock  = st3)
sl4 = Sale(price_sale = "490", date_sale = "02-11-2022", count_sale = 5, stock  = st4)
sl5 = Sale(price_sale = "601", date_sale = "26-10-2022", count_sale = 5, stock  = st5)
session.add_all([sl1, sl2,sl3,sl4,sl5])



def project_shop(res_):
    query = session.query(
        Book.title_book, Shop.shop_name, Sale.price_sale, Sale.date_sale,
    ).select_from(Shop).join(Stock).join(Book).join(Publisher).join(Sale)
    if res_.isdigit():
        shop_query = query.filter(Publisher.publisher_id == res_).all()
    else:
        shop_query = query.filter(Publisher.name_publish == res_).all()
    for title_book, name_shop, price_sale, date_sale in shop_query:
        print(f'{title_book} | {name_shop} | {price_sale} | {date_sale}')
    

if __name__ == '__main__':
    res_ = input('Введите имя автора: ')
    project_shop(res_)
  
session.commit()
session.close()