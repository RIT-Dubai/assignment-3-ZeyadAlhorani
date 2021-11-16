

garden_items = {"Garden Hose": ("G1", 15), "Soil": ("G2", 5), "Tools": ("G3", 30)}
indoor_items = {"Couch": ("I1", 250), "Rug": ("I2", 85), "Table": ("I3", 170)}
bathroom_items = {"Bathroom Mirror": ("B1",50), "Bathroom Rug": ("B2", 20), "Bathroom Curtain": ("B3", 10)}



class Home:
    # a class that identifies an item
    __slots__ = ("name", "letter_code", "price")

    def __init__(self, name, letter_code, price):
     self.name = " "
     self.letter_code = " "
     self.price = " "

    garden_items = {"Garden Hose": ("G1", 15), "Soil": ("G2", 5), "Tools": ("G3", 30)}
    indoor_items = {"Couch": ("I1", 250), "Rug": ("I2", 85), "Table": ("I3", 170)}
    bathroom_items = {"Bathroom Mirror": ("B1",50), "Bathroom Rug": ("B2", 20), "Bathroom Curtain": ("B3", 10)}



class Home_Category:
    # these dictionaries are only examples for now
    garden_items = {"Garden Hose": ("G1", 15), "Soil": ("G2", 5), "Tools": ("G3", 30)}
    indoor_items = {"Couch": ("I1", 250), "Rug": ("I2", 85), "Table": ("I3", 170)}
    bathroom_items = {"Bathroom Mirror": ("B1",50), "Bathroom Rug": ("B2", 20), "Bathroom Curtain": ("B3", 10)}

"""""
class item:
# a class that identifies an item
    __slots__ = ("name", "letter_code", "price")
    def __init__ (self, name, letter_code, price):
     self.name = " "
     self.letter_code = " "
     self.price = 0

"""""
garden_ant = {"Garden Plant", "F1", 20}

class Avatar:
    def __init__(self, category, base_charge):
      self.category = " "
      self.base_charge = 50


def make_order():
# function that allows the user to orders
    return


def print_garden():
    print("Garden Items :- ")
    print("Garden Hose for $15 (Use code G1 to add item)", "Soil for $5 a pack (Use code G2 to add item)", "Tools for $30 (Use code G3 to add")

def print_indoor():
    print("Indoor Items :- ")
    print("Couch for $250 (Use code I2 to add item)", "Rug for $85 (Use code I2 to add item)", "Table for $170 (Use code I3 to add")

def print_bathroom():
    print("Bathroom Items:- ")
    print("Bathroom Mirror for $50 (Use code B1 to add item)", "Bathroom Rug for $20 (Use code B2 to add item)", "Bathroom Curtain for $10 (Use code I3 to add")


def main():
    #Home()
    print("Welcome to Home Ideas Center, where all orders include a new home feeling!")
    print("For your new Home space ...")
    print("Enter one of the letters to display the options for each catagory")
    print("    G for Garden Items   ", "   I for Indoor Items   ",   "B for Bathroom Items   ")

    command = input()
    if command == "G":
        print(print_garden())

    if command == "I":
        print(print_indoor())

    if command == "B":
        print(print_bathroom())




main()
