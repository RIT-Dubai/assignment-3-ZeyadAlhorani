

garden_items = {"G1": ("Garden Hose", 15), "G2": ("Soil", 5), "G3": ("Tools", 30)}
indoor_items = {"I1": ("Couch", 250), "I2": ("Rug", 85), "I3": ("Table", 170)}
bathroom_items = {"B1": ("Bathroom Mirror",50), "B2": ("Bathroom Rug", 20), "B3": ("Bathroom Curtain", 10)}


class Home_category:
    # a class that identifies the item's state
    __slots__ = ["name", "letter_code", "price"]

    def __init__(self, name, letter_code, price):
     self.name = name
     self.letter_code = letter_code
     self.price = price


class Home:
    # basket class
    __slots__ = ["garden", "indoor", "bathroom"]

    def __init__(self, garden, indoor, bathroom):
        self.garden = garden
        self.bathroom = bathroom
        self.indoor = indoor




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


def main():
    #Home()
    print("Welcome to Home Ideas Center, where all orders include a new home feeling!")
    print("For your new Home space ...")

    def options():
        print(" Choose a letter to display option for each category")
        print("    G for Garden Items   ", "   I for Indoor Items   ",   "B for Bathroom Items   ")

        cart = 0

        command = input()

        while command != "n":
            if command == "G":
               print_garden()

            elif command == "G1":
                price = garden_items["G1"][1]
                print("   You added Garden Hose to your cart, total is:"   , cart)
                cart += price


            elif command == "G2":
                price = garden_items["G2"][1]
                cart += price
                print("   You added Soil to your cart, total is:"   , cart)

            elif command == "G3":
                price = garden_items["G3"][1]
                cart =+ price
                print("   You added Tools to your cart, total is:"   , cart)

            print(cart + 50)


            break

        options()


        while command != "n":
            if command == "I":
                print(print_indoor())

            elif command == "I1":
                price = indoor_items["I1"][1]
                print("   You added Couch to your cart, total is:"   , cart)
                cart += price

            elif command == "I2":
                price = indoor_items["I2"][1]
                print("   You added Rug to your cart, total is:"   , cart)
                cart += price

            elif command == "I3":
                price = indoor_items["I3"][1]
                print("   You added Table to your cart, total is:"   , cart)
                cart += price
            break


        while command != "n":
            if command == "B":
                print(print_bathroom())

            elif command == "B1":
                price = bathroom_items["B1"][1]
                print("   You added Bathroom Mirror to your cart, total is:"   , cart)
                cart += price

            elif command == "B2":
                price = bathroom_items["B2"][1]
                print("   You added Bathroom Rug to your cart, total is:"   , cart)
                cart += price

            elif command == "B2":
                price = bathroom_items["B3"][1]
                print("   You added Bathroom Curtain to your cart, total is:"   , cart)
                cart += price
            break


    options()

"""""        
        if command == "G":
           print(print_garden())
           pass
           options()

        if command == "I":
            print(print_indoor())
            options()

        if command == "B":
            print(print_bathroom())
            pass
            options()

        elif command == "G1":
            cart += 15
            print("***You added Garden Hose to your cart, total is:***", cart)
            options()

        elif command == "G2":
            price = garden_items["G2"][1]
            cart += price
            print("You added Soil to your cart, total is:", cart)
            options()

        elif command == "G3":
            price = garden_items["G3"][1]
            cart =+ price
            print("You added Tools to your cart, total is:", cart)
            options()

        print(cart + "Base charge",50)

    options()



    garden_items = {"G1": ("Garden Hose", 15), "G2": ("Soil", 5), "G3": ("Tools", 30)}
    indoor_items = {"I1": ("Couch", 250), "I2": ("Rug", 85), "I3": ("Table", 170)}
    bathroom_items = {"B1": ("Bathroom Mirror",50), "B2": ("Bathroom Rug", 20), "B3": ("Bathroom Curtain", 10)}
"""""




main()
