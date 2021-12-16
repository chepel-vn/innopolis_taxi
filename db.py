from sqlalchemy import Column, Integer, String, DateTime, create_engine, \
    ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

engine = create_engine('postgresql://postgres:tree@127.0.0.1:5432/innopolis')
Base = declarative_base()
Base.metadata.create_all(engine)


class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='ID водителя')
    name = Column(String(40), nullable=False, comment='Имя водителя')
    car = Column(String(40), nullable=False, comment='Имя машины')
    # orders = relationship("Order", backref="orders")

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='ID клиента')
    name = Column(String(40), nullable=False, comment='Имя клиента')
    is_vip = Column(String(40), nullable=False, comment='VIP клиент?')
    # orders = relationship("Order", backref="orders")

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True, comment='ID клиента')
    address_from = Column(String, nullable=False, comment='Адрес откуда')
    address_to = Column(String, nullable=False, comment='Адрес куда')
    client_id = Column(Integer, ForeignKey('clients.id'), comment='ID клиента')
    driver_id = Column(Integer, ForeignKey('drivers.id'), comment='ID водителя')
    date_created = Column(DateTime(), default=datetime.now, nullable=False, comment='Дата создания заказа')
    status = Column(String(15), default='not_accepted', nullable=False, comment='Статус')

def add_driver(driver_name: str, car_name: str):
    Session = sessionmaker(bind=engine)
    session = Session()

    new_driver = Driver(name=driver_name, car=car_name)
    session.add(new_driver)

    session.commit()
    session.close()

def add_client(client_name: str, is_vip: bool):
    Session = sessionmaker(bind=engine)
    session = Session()

    new_client = Client(name=client_name, is_vip=is_vip)
    session.add(new_client)

    session.commit()
    session.close()


def add_order(client_id: int, driver_id: int, address_from: str, address_to: str):
    Session = sessionmaker(bind=engine)
    session = Session()

    new_order = Order(client_id=client_id, driver_id=driver_id,
                      address_from=address_from, address_to=address_to)
    session.add(new_order)

    session.commit()
    session.close()

def fill_init_db() -> int:
    try:
        add_driver('Иван Петрович', 'ВАЗ-2107')
        add_driver('Дмитрий Аавович', 'ВАЗ-2109')
        add_client('Дмитрий', True)
    except Exception as e:
        return 1
    else:
        return 0