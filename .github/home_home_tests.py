import home_home


class test_home():
    home_item1 = home_home.Home("Garden Hose", "G1", 10)
    assert home_item1.name == "Garden Hose"
    assert home_item1.letter_code == "G1"
    assert home_item1.price == 10


test_home()
