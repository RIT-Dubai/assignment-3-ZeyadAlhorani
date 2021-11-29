
class Home_category:
    # a class that identifies the item's state
    __slots__ = ["name", "letter_code", "price"]

    def __init__(self, name, letter_code, price):
      self.name = name
      self.letter_code = letter_code
      self.price = int(price)


class Home(object):
    # basket class
    basket = []

    def _init_(self,item_list):
        self.item_list = item_list

    def print_items(self, item):
        self.basket.append(str(item))
        print(list(item))

    def add(self, i):
        self.basket.append(i)

    def get_basket(self):
        return self.basket


def print_garden():
    # function to print garden items options
    print("   Garden Items :- ")
    print("      Garden Hose for $15 (Use code G1 to add item)")
    print("      Soil for $5 a pack (Use code G2 to add item)")
    print("      Tools for $30 (Use code G3 to add)")


def print_indoor():
    # function to print indoor items options
    print("  Indoor Items :- ")
    print("      Couch for $250 (Use code I1 to add item)")
    print("      Rug for $85 (Use code I2 to add item)")
    print("      Table for $170 (Use code I3 to add")


def print_bathroom():
    # function to print bathroom items options
    print("   Bathroom Items:- ")
    print("      Bathroom Mirror for $50 (Use code B1 to add item)")
    print("      Bathroom Rug for $20 (Use code B2 to add item)")
    print("      Bathroom Curtain for $10 (Use code B3 to add")

def main():

    print("Welcome to Home Ideas Center, where all orders include a new home feeling!")
    print("For your new Home space ...")
    garden_items = {"G1": ("Garden Hose", 15), "G2": ("Soil", 5), "G3": ("Tools", 30)}
    indoor_items = {"I1": ("Couch", 250), "I2": ("Rug", 85), "I3": ("Table", 170)}
    bathroom_items = {"B1": ("Bathroom Mirror",50), "B2": ("Bathroom Rug", 20), "B3": ("Bathroom Curtain", 10)}

    print("Choose 0 to display the options for the garden category, or Input the code for your wanted item, enter n for next category")
    print("----Enter X to Exit and Receive Invoice---")

    command = input()
    cart = 50
    H = Home()
    user = Home()
    amount = []
    while command != 'n':
        if command == "0":
            print_garden()

        elif command in garden_items:
            if command == "G1":
                H.print_items("Garden Hose")
                user.add("Garden Hose")
                amount.append(Home())
                cart += 15
                print("   You added Garden Hose to your cart")

            elif command == "G2":
                H.print_items("Soil")
                user.add("Soil")
                cart += 5
                print("   You added Soil to your cart")


            elif command == "G3":
                H.print_items("Tools")
                user.add("Tools")
                cart += 30
                print("   You added Tools to your cart")


        elif command == "X":
            break

        elif command == 'n':
            break

        else:
            print("Input is not valid.")

        print("Choose 0 to display the options for the garden category, or Input the code for your wanted item, enter n for next category")
        print("----Enter X to Exit and Receive Invoice---")
        command = input()

    print("Choose 0 to display the options for the indoor category, or Input the code for your wanted item, enter n for next category")
    print("----Enter X to Exit and Receive Invoice---")
    command = input()

    while command != "n":
        if command == '0':
            print_indoor()

        elif command in indoor_items:

            if command == "I1":
                H.print_items("Couch")
                user.add("Couch")
                cart += 250
                print("   You added Couch to your cart")

            elif command == "I2":
                H.print_items("Rug")
                user.add("Rug")
                cart += 85
                print("   You added Rug to your cart")

            elif command == "I3":
                H.print_items("Table")
                user.add("Table")
                cart += 170
                print("   You added Table to your cart")

        elif command == "X":
             break

        elif command == 'n':
            break

        else:
            print("Input is not valid")
        print("Choose 0 to display the options for the indoor category, or Input the code for your wanted item, enter n for next category")
        print("----Enter X to Exit and Receive Invoice---")
        command = input()

    print("Choose 0 to display the options for the bathroom category, or Input the code for your wanted item, enter n for exit")
    print("----Enter X to Exit and Receive Invoice---")
    command = input()
    while command != "n":
        if command == '0':
            print_bathroom()

        elif command in bathroom_items:
            if command == "B1":
                H.print_items("Bathroom Mirror")
                user.add("Bathroom Mirror")
                cart += 50
                print("   You added Bathroom Mirror to your cart")

            elif command == "B2":
                H.print_items("Bathroom Rug")
                user.add("Bathroom Rug")
                cart += 20
                print("   You added Bathroom Rug to your cart")

            elif command == "B3":
                H.print_items("Bathroom Curtain")
                user.add("Bathroom Curtain")
                cart += 10
                print("   You added Bathroom Curtain to your cart")

        elif command == "X":
             break

        elif command == 'n':
            break

        else:
            print("Input is not valid")

        print("Choose 0 to display the options for the bathroom category, or Input the code for your wanted item, enter n for exit")
        print("----Enter X to Exit and Receive Invoice---")
        command = input()


    for an_item in amount:
        print("------------------------------------------------------------------Invoice------------------------------------------------------------------")
        print("                                                      #Thank You For Using Our Website#    ")
        print("Items in cart:", user.get_basket())
        print("Your Total is (after the $50 base charge) :", cart, "US Dollars")
        print("                                                             #Have A Nice Day#                   ")
        print("------------------------------------------------------------------Invoice------------------------------------------------------------------")





main()
