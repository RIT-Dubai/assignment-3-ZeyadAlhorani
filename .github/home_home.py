
class Home_category:
    # a class that identifies the item's state
    __slots__ = ["name", "letter_code", "price"]

    def __init__(self, name, letter_code, price):
      self.name = name
      self.letter_code = letter_code
      self.price = int(price)


class Home(object):
    # basket class

    def __init__(self,item_list):
        self.item_list = item_list

    def print_items(self):
        print(self.item_list)


def print_garden():
    # function to print garden items options
    print("   Garden Items :- ")
    print("      Garden Hose for $15 (Use code G1 to add item)")
    print("      Soil for $5 a pack (Use code G2 to add item)")
    print("      Tools for $30 (Use code G3 to add)")


def print_indoor():
    # function to print indoor items options
    print("  Indoor Items :- ")
    print("      Couch for $250 (Use code I2 to add item)")
    print("      Rug for $85 (Use code I2 to add item)")
    print("      Table for $170 (Use code I3 to add")


def print_bathroom():
    # function to print bathroom items options
    print("   Bathroom Items:- ")
    print("      Bathroom Mirror for $50 (Use code B1 to add item)")
    print("      Bathroom Rug for $20 (Use code B2 to add item)")
    print("      Bathroom Curtain for $10 (Use code I3 to add")


def invoice_cart():
        print("          ----------Invoice----------          ")



        print("          ----------Invoice----------          ")


def main():
    garden_items = {"G1": ("Garden Hose", 15), "G2": ("Soil", 5), "G3": ("Tools", 30)}
    indoor_items = {"I1": ("Couch", 250), "I2": ("Rug", 85), "I3": ("Table", 170)}
    bathroom_items = {"B1": ("Bathroom Mirror",50), "B2": ("Bathroom Rug", 20), "B3": ("Bathroom Curtain", 10)}

    print("Choose 0 to display the options for each category, or Input the code for your wanted item")
    print("----Enter X to Exit and Receive Invoice---")

    command = input()
    cart = 50
    H = Home
    amount = []

    if command == "0":
        print_garden()
        print_indoor()
        print_bathroom()
        main()

    if command != "n":
        while command != "n":
            if command in garden_items:
                if command == "G1":
                    amount.append(Home("Garden Hose"))
                    cart += 15
                    print("   You added Garden Hose to your cart")
                    main()

                elif command == "G2":
                    amount.append(Home("Soil"))
                    cart += 5
                    print("   You added Soil to your cart")
                    main()

                elif command == "G3":
                    amount.append(Home("Tools"))
                    cart += 30
                    print("   You added Tools to your cart")
                    main()

            elif command == "X":
                break

            break

        while command != "n":

            if command in indoor_items:

                if command == "I1":
                    amount.append(Home("Couch"))
                    cart += 250
                    print("   You added Couch to your cart")
                    main()

                elif command == "I2":
                    amount.append(Home("Rug"))
                    cart += 85
                    print("   You added Rug to your cart")
                    main()

                elif command == "I3":
                    amount.append(Home("Table"))
                    cart += 170
                    print("   You added Table to your cart")
                    main()

            elif command == "X":
                 break
            break

        while command != "n":

            if command in bathroom_items:
                if command == "B1":
                    amount.append(Home("Bathroom Mirror"))
                    cart += 50
                    print("   You added Bathroom Mirror to your cart")
                    main()

                elif command == "B2":
                    amount.append(Home("Bathroom Rug"))
                    cart += 20
                    print("   You added Bathroom Rug to your cart")
                    main()

                elif command == "B3":
                    amount.append(Home("Bathroom Curtain"))
                    cart += 10
                    print("   You added Bathroom Curtain to your cart")
                    main()

            elif command == "X":
                 break
            break

    for an_item in amount:
        an_item.print_items()
        print(cart)


if __name__ == '__main__':
    print("Welcome to Home Ideas Center, where all orders include a new home feeling!")
    print("For your new Home space ...")
    main()

"""""
g1 = garden1.get("G1", [1])
item_list.append("Garden Hose")
amount.append(15)
counter = counter + 1
total_price = total_price + 15
print("   You added Garden Hose to your cart, total is:"   ,amount)
main()
"""""
