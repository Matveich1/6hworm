from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=60))


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String, )
    publisher_id = Column(Integer, ForeignKey('publisher.id'), nullable=False)

    publisher = relationship(Publisher, backref='book')


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=60))


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
    shop_id = Column(Integer, ForeignKey('shop.id'), nullable=False)
    count = Column(Integer)
    book = relationship(Book, backref='book')
    shop = relationship(Shop, backref='shop')


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    date_sale = Column(Integer)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    count = Column(Integer)
    stock = relationship(Stock, backref='stock')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
