
import random
from product import Product

class City(object):
    cities = []
    def __init__(self, name, has_warehouse, has_bank):
        self.name = name
        self.has_warehouse = has_warehouse
        self.has_bank = has_bank
        self.city_products = []
        self.create_city_products()
    @classmethod
    def create_cities(cls):
        cls.cities.append(City("Hong Kong", True, True))
        cls.cities.append(City("Shanghai", False, False))
        cls.cities.append(City("London", False, False))
    def create_city_products(self):
        for product in Product.products:
            self.city_products.append(CityProduct(self, product))

class CityProduct(object):
    def __init__(self, city, product):
        self.city = city
        self.product = product
        self.generate_random_price()
    def generate_random_price(self):
        self.price = random.randint(self.product.minprice, self.product.maxprice)


