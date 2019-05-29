from product import Product
import datetime
from city import City
import os
import random
from pirate_encounter import PirateEncounter

MENU_DIVIDER = "---------------------------"
GAME_TITLE = "Python Pirate Trader 0.1A"

class GameManager(object):
    def __init__(self, **kwargs):
        self.cash = kwargs['cash']
        self.debt = kwargs['debt']
        self.cannons = kwargs['cannons']
        self.bank = 0
        self.maxshiphold = kwargs['shiphold']
        self.firm_name = kwargs['name']
        self.currentshiphold = 0
        self.ship_health = 100
        Product.create_products()
        City.create_cities()
        self.current_city = City.cities[0]
        self.current_date = datetime.datetime(1820,1,1)

  
    def leave_port(self, city_list, current_date):
        i = 1
        for city in city_list:
            print("{0}) {1}".format(i, city.name))
            i = i+1
        select_city = input("Which city do you wish to go to?")
        current_date += datetime.timedelta(days=1)
        return city_list[int(select_city)-1], current_date


    def buy(self):
        buy_select = input("Which product do you want to buy (1-%s) - C)ancel :" % str(len(Product.products)))
        if buy_select == "C":
            return
        city_product = self.current_city.city_products[int(buy_select)-1]
        qty_to_buy = input("How many " + city_product.product.name + " do you wish to buy?")
        cost_to_buy = city_product.product.price * int(qty_to_buy)
        print(cost_to_buy)
        if cost_to_buy <= self.cash:
            if self.currentshiphold + int(qty_to_buy) <= self.maxshiphold:
                self.cash -= int(qty_to_buy) * city_product.price
                city_product.product.shipqty += int(qty_to_buy)
                self.currentshiphold += int(qty_to_buy)
            else:
                print("There is not enough space to hold those items.")
                print("Continue...press any key")
        else:
            print("You don't enough enough cash")
            input("Continue...press any key")


    def sell(self):
        sell_select = input("Which product do you want to sell (1-%s) - C)ancel :"% str(len(Product.products)))
        if sell_select == "C":
            return
        city_product = self.current_city.city_products[int(sell_select)-1]
        qty_to_sell = input("How many " + city_product.product.name + "do you wish to sell?")
        if int(qty_to_sell) <= city_product.product.shipqty:
            self.cash += int(qty_to_sell) * city_product.price
            city_product.product.shipqty -= int(qty_to_sell)
            self.currentshiphold -= int(qty_to_sell)
        else:
            print("You don't have enough to sell")
            input("Press any key to continue")


    def visit_bank(self):
        input("How much to transfer to the bank?")


    def display_products(self):
        i = 1
        for cityproduct in self.current_city.city_products:
            print(str(i) + ')' + cityproduct.product.name + " -- " + str(cityproduct.price) + "---" + str(cityproduct.product.shipqty))
            i += 1

    def check_price_change(self):
        result = random.randint(0,100)
        if result >= 80:
            for city_product in self.current_city.city_products:
                city_product.generate_random_price()


    def increase_debt(self):
        self.debt *= 1.15


    def visit_money_lender(self):
        payback = input("How much do you wish to pay back? ")
        if int(payback) <= self.cash:
            self.debt -= int(payback)
            self.cash -= int(payback)
        borrow = input("How much do you wish to borrow? ")
        if int(borrow) <= self.cash *20:
            self.debt += int(borrow) * 5
            self.cash += int(borrow)


    def StartUp(self):
        game_running = True


        while game_running:

            os.system("cls")


            print(MENU_DIVIDER)
            print(GAME_TITLE)
            print(MENU_DIVIDER)

            print("Firm Name: %s" % self.firm_name)
            print("Cash: %d " % self.cash)
            print("Debt: %d " % self.debt)
            print("Cannons: %d " % self.cannons)
            print("City: %s " % self.current_city.name)
            print("Ship Health: %s " % self.ship_health)
            print("Date: {:%B %d, %Y}".format(self.current_date))
            print(MENU_DIVIDER)
            print("----City Products----")
            self.display_products()
            has_bank_string = ""

            if self.current_city.has_bank == True:
                has_bank_string ="V)isit Bank,"
            print("Menu: L)eave Port, B)uy, S)ell, T)ransfer Warehouse, V)isit Bank, Q)uit")
            menu_option = input("What is your option?:")

            if menu_option == "L":
                self.current_city, self.current_date = self.leave_port(City.cities, self.current_date)
                self.check_price_change()
                self.increase_debt()
                pirates=PirateEncounter(self)

            elif menu_option == "B":
                self.buy()

            elif menu_option == "S":
                self.sell()

            elif menu_option =="V" and self.current_city.has_bank == True:
                self.visit_bank()

            elif menu_option == "Q":
                game_running = False



