import home_home as H


class test_home():
    home_item1 = H.Home("Garden Hose", "G1", 10)
    assert home_item1.name == "Garden Hose"
    assert home_item1.letter_code == "G1"
    assert home_item1.price == 10



def test_main():
    H.main()
    command = input()
    assert command == "G"

test_home()
