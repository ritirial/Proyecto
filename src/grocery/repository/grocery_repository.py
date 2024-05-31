import abc
import grocery.config as config
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from grocery.handler.csv_handler import read_csv_to_dict
from grocery.model.grocery_item import Item, ItemBuilder, Base as ItemBase

#Dependency
class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: Item):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, sku) -> Item:
        raise NotImplementedError

    @abc.abstractmethod
    def get_item(self, sku) -> Item:
        raise NotImplementedError

    @abc.abstractmethod
    def reset_database(self, sku) -> Item:
        raise NotImplementedError

    @abc.abstractmethod
    def clean_database(self, sku) -> Item:
        raise NotImplementedError


#Principio de Inversión de Dependencias
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self):
        self.engine = create_engine(config.get_postgres_uri())
        ItemBase.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine, expire_on_commit=False)

    def get(self):
        with self.Session() as session:
            items = session.query(Item).all()
            return items

    def add(self, item: Item):
        with self.Session() as session:
            session.add(item)
            session.commit()

    def delete(self, sku):
        with self.Session() as session:
            item = self.get_item(sku)
            session.delete(item)
            session.commit()

    def get_item(self, sku):
        with self.Session() as session:
            item = session.query(Item).filter_by(SKU=sku).one()
            return item

    def reset_database(self):
        with self.Session() as session:
            self.clean_database()
            rows = read_csv_to_dict("sample_grocery.csv")
            for row in rows:
                item = ItemBuilder().with_sku(row['SKU']).with_name(row['Name']).with_description(row['Description']).with_quantity(float(row['Quantity'])).with_price(float(row['Price'])).with_exp_date(datetime.strptime(row['Expiration Date'], '%Y-%m-%d')).build()
                session.add(item)
            session.commit()

    def clean_database(self):
        ItemBase.metadata.drop_all(bind=self.engine)
        ItemBase.metadata.create_all(bind=self.engine)
