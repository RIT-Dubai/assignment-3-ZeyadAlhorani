
class Home_category:
    # a class that identifies the item's state
    __slots__ = ["name", "letter_code", "price"]

    def __init__(self, name, letter_code, price):
      self.name = name
      self.letter_code = letter_code
      self.price = price


class Home:
    # basket class
    shopping_cart = []

    #__slots__ = ["garden", "indoor", "bathroom"]

    #def __init__(self, garden, indoor, bathroom):
        #self.garden = garden
        #self.bathroom = bathroom
        #self.indoor = indoor

    def add_cart(item):
        shopping_cart = []
        shopping_cart.append(item)
        print(shopping_cart, "50")


def print_garden():
    # function to print garden items options
    print("Garden Items :- ")
    print("   Garden Hose for $15 (Use code G1 to add item)")
    print("   Soil for $5 a pack (Use code G2 to add item)")
    print("   Tools for $30 (Use code G3 to add)")


def print_indoor():
    # function to print indoor items options
    print("Indoor Items :- ")
    print("   Couch for $250 (Use code I2 to add item)")
    print("   Rug for $85 (Use code I2 to add item)")
    print("   Table for $170 (Use code I3 to add")


def print_bathroom():
    # function to print bathroom items options
    print("Bathroom Items:- ")
    print("   Bathroom Mirror for $50 (Use code B1 to add item)")
    print("   Bathroom Rug for $20 (Use code B2 to add item)")
    print("   Bathroom Curtain for $10 (Use code I3 to add")


def invoice_cart():
        print("          ----------Invoice----------          ")



        print("          ----------Invoice----------          ")


def main():
    #Home()

    garden_items = {"G1": ("Garden Hose", 15), "G2": ("Soil", 5), "G3": ("Tools", 30)}
    indoor_items = {"I1": ("Couch", 250), "I2": ("Rug", 85), "I3": ("Table", 170)}
    bathroom_items = {"B1": ("Bathroom Mirror",50), "B2": ("Bathroom Rug", 20), "B3": ("Bathroom Curtain", 10)}

    print(" Choose a letter to display option for each category, or Input the code for your wanted item")
    print("    G for Garden Items   ", "   I for Indoor Items   ",   "B for Bathroom Items   ")
    print("----Enter X to Exit and Receive Invoice---")

    command = input()
    cart = 0

    while command != "n":
        try:
            if command == "G":
                print_garden()
                break

            elif command in garden_items:
                if command == "G1":
                    g1 = garden_items.get("G1", [1])
                    print(g1)
                    #Home.add_cart(g1)
                    print("   You added Garden Hose to your cart, total is:"   ,)
                    break

                if command == "G2":
                    g2 = garden_items.get("G2", [1])
                    print(g2)
                    print("   You added Soil to your cart, total is:"   , cart)

                if command == "G3":
                    g3 = garden_items.get("G3", [2])
                    print(g3)
                    print("   You added Tools to your cart, total is:"   , cart)

            break

        except ValueError:
            print("Item not found")
            continue

    while command != "n":
        try:
            if command == "I":
                print(print_indoor())

            elif command in indoor_items:
                if command == "I1":
                    i1 = indoor_items.get("I1", [1])
                    print(i1)
                    print("   You added Couch to your cart, total is:"   , cart)

                elif command == "I2":
                    i2 = indoor_items.get("I2", [2])
                    print(i2)
                    print("   You added Rug to your cart, total is:"   , cart)

                elif command == "I3":
                    i3 = indoor_items.get("I3", [1])
                    print(i3)
                    print("   You added Table to your cart, total is:"   , cart)
            break
        except ValueError:
            print("Item not found")
            continue

    while command != "n":
        try:
            if command == "B":
                print(print_bathroom())

            elif command in bathroom_items:
                if command == "B1":
                    b1 = bathroom_items.get("B1", [1])
                    print(b1)
                    print("   You added Bathroom Mirror to your cart, total is:"   , cart)

                elif command == "B2":
                    b2 = bathroom_items.get("B2", [1])
                    print(b2)
                    print("   You added Bathroom Rug to your cart, total is:"   , cart)

                elif command == "B3":
                    b3 = bathroom_items.get("B3", [1])
                    print(b3)
                    print("   You added Bathroom Curtain to your cart, total is:"   , cart)

            break
        except ValueError:
            print("Item not found")
            continue

    while command == "X":
        print("Done")
        break

    main()


if __name__ == '__main__':
    print("Welcome to Home Ideas Center, where all orders include a new home feeling!")
    print("For your new Home space ...")
    main()
