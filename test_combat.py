from Final_Project import Player

def test_currency():
    p = Player()
    p.add_currency(20)
    assert p.currency == 20

def test_inventory():
    p = Player()
    p.add_item("Potion", 2)
    assert "Potion" in p.inventory
    assert p.inventory["Potion"]["quantity"] == 2