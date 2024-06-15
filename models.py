import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker


Base = declarative_base()



class Publisher(Base):
    __tablename__ = "publisher"

    publisher_id = sq.Column(sq.Integer, primary_key=True)
    name_publish = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'({self.name_publish})'

class Book(Base):
     __tablename__ = "book"

     book_id = sq.Column(sq.Integer, primary_key=True)
     title_book = sq.Column(sq.String(length=40), unique=True)
     id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.publisher_id'), nullable=False)

     publisher = relationship(Publisher, backref='book')

     def __str__(self):
        return f'{self.book_id}:{self.title_book}'


class Shop(Base):
      __tablename__ = "shop"

      shop_id = sq.Column(sq.Integer, primary_key=True)
      shop_name = sq.Column(sq.String(length=40), unique=True)

      def __str__(self):
        return f'{self.shop_id}:{self.shop_name}'
      
class Stock(Base):
      __tablename__ = "stock"

      stock_id = sq.Column(sq.Integer, primary_key=True)
      id_book = sq.Column(sq.Integer, sq.ForeignKey('book.book_id'), nullable=False)
      id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.shop_id'), nullable=False)
      count_stock = sq.Column(sq.Integer, nullable=False)

      book = relationship(Book, backref='stock')
      shop = relationship(Shop, backref='stock')

class Sale(Base):
      __tablename__ = 'sale'
      
      sale_id = sq.Column(sq.Integer, primary_key=True)
      price_sale = sq.Column(sq.Numeric, nullable=False)
      date_sale = sq.Column(sq.DateTime, nullable=False)
      id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.stock_id'), nullable=False)
      count_sale = sq.Column(sq.Integer, nullable=False)

      stock = relationship(Stock, backref='sale')

      def __str__(self):
        return f'{self.sale_id}:{self.price_sale}, {self.date_sale}, {self.count_sale}'
      


def create_tables(engine):
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)