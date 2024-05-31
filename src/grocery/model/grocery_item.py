from sqlalchemy import Column, String, Float, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "grocery"
    SKU = Column(String, primary_key=True)
    Name = Column(String)
    Description = Column(String)
    Quantity = Column(Float)
    Price = Column(Float)
    Expiration_date = Column(Date)


#Buider design pattern: La clase Item tiene muchos parametros, por lo que se usa un builder para facilitar su implementación en otros componentes
class ItemBuilder:

    def __init__(self):
        self.Item = None
        self.SKU = ''
        self.Name = ''
        self.Description = ''
        self.Quantity = 0.0
        self.Price = 0.0
        self.Expiration_date = None

    def with_sku(self, sku):
        self.SKU = sku
        return self

    def with_name(self, name):
        self.Name = name
        return self

    def with_description(self, description):
        self.Description = description
        return self


    def with_quantity(self, quantity):
        self.Quantity = quantity
        return self

    def with_price(self, price):
        self.Price = price
        return self

    def with_exp_date(self, expdate):
        self.Expiration_date = expdate
        return self

    def build(self):
        self.Item = Item(SKU=self.SKU, Name=self.Name, Description=self.Description, Quantity=self.Quantity, Price=self.Price, Expiration_date=self.Expiration_date)
        return self.Item