from bank import value

def test_1():
    assert value('a')==100
    assert value('ha')==20
    assert value('hello')==0
def test_capital_letters():
    assert value('A')==100
    assert value('Ha')==20
    assert value('HELLO')==0
