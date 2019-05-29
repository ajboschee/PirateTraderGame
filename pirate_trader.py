
import os
import datetime
import random
from product import Product
from city import City
from gamemanager import GameManager



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

welcome_message()
firm_name = get_firm_name()

cash, debt, cannons = get_starting_options()

game = GameManager(name=firm_name, cash=cash, debt=debt, cannons=cannons, shiphold=100)

game.StartUp()


