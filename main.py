import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model import create_tables, Publisher, Book, Shop, Stock, Sale


DSN = 'postgresql://postgres:qwerty@localhost:5432/homeworkorm'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


def sales_request(id=None, name=None):
    req = session.query(Book.title, Shop.name, Sale.price,
                        Sale.count, Sale.date_sale).\
                        join(Publisher).join(Stock).join(Sale).join(Shop).\
                        filter(Publisher.id == id,
                               Publisher.name.like(f'%{name}%'))
    for book, shop, price, count, date in req:
        print(f'{book} | {shop} | {price} | {count} | {date}')
    return print('Автора с таким именем или id нет')


session.close()


if __name__ == '__main__':
    publisher_input = input('Введи id или имя автора: ')
    if publisher_input.isdigit():
        sales_request(id=int(publisher_input))
    else:
        sales_request(name=publisher_input)
