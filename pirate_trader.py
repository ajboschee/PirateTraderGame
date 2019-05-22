
import os
import datetime
import random
from product import Product
from city import City

MENU_DIVIDER = "---------------------------"
GAME_TITLE = "Python Pirate Trader 0.1A"

def welcome_message():
    print("Welcome to Python Pirate Trader")


def get_firm_name():
    #firm_name = input("Please enter your firm name: ")
    return "test firm"
    

def get_starting_options():
    #starting_options = input("How do you wish to start. 1) Cash & Debt 2) Cannons no debt.: ")
    starting_options = "1"
    if starting_options == "1":
        cash = 250
        debt = cash
        cannons = 0
    else:
        cash = 0
        debt = 0
        cannons = 5
    return cash, debt, cannons

def leave_port(city_list, current_date):
    i = 1
    for city in city_list:
        print("{0}) {1}".format(i, city.name))
        i = i+1
    select_city = input("Which city do you wish to go to?")
    current_date += datetime.timedelta(days=1)
    return city_list[int(select_city)-1], current_date

def buy():
    input("What do you want to buy?")

def sell():
    input("What do you want to sell?")

def visit_bank():
    input("How much to transfer to the bank?")

def display_products():
    for product in Product.products:
        print(product.name + " -- " + str(product.price))

class GameManager(object):
    def __init__(self, cash, cannons):
        self.cash = cash
        self.debt = cash
        self.cannons = cannons
        self.bank = 0
        self.shiphold = shiphold
        Product.create_products()
        City.create_cities()
        self.currentcity = City.cities[0]


game = GameManager(200,5, 100)




welcome_message()
firm_name = get_firm_name()
game.cash, game.debt, game.cannons = get_starting_options()

game_running = True

current_date = datetime.datetime(1820,1,1)
while game_running:

    os.system("cls")


    print(MENU_DIVIDER)
    print(GAME_TITLE)
    print(MENU_DIVIDER)

    print("Firm Name: %s" % firm_name)
    print("Cash: %d " % game.cash)
    print("Debt: %d " % game.debt)
    print("Cannons: %d " % game.cannons)
    print("City: %s " % current_city.name)
    print("Date: {:%B %d, %Y}".format(current_date))
    print(MENU_DIVIDER)
    print("----City Products----")
    display_products()
    has_bank_string = ""
    if current_city.has_bank == True:
        has_bank_string ="V)isit Bank,"
    print("Menu: L)eave Port, B)uy, S)ell, T)ransfer Warehouse, V)isit Bank, Q)uit")
    menu_option = input("What is your option?:")
    if menu_option == "L":
        game.current_city, current_date = leave_port(City.cities, current_date)
    elif menu_option == "B":
        buy()
    elif menu_option == "S":
        sell()
    elif menu_option =="V" and game.current_city.has_bank == True:
        visit_bank()
    elif menu_option == "Q":
        game_running = False
