import fuel
import pytest

def test_convert():
    assert fuel.convert("1/4")==25
    assert fuel.convert("3/4")==75
    assert fuel.convert("4/4")==100
    assert fuel.convert("0/4")==0
    with pytest.raises(ValueError):
        fuel.convert("5/4")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("5/0")

def test_gauge():
    assert fuel.gauge(100)=="F"
    assert fuel.gauge(0)=="E"
    assert fuel.gauge(75)=="75%"
    assert fuel.gauge(1)=="E"
    assert fuel.gauge(99)=="F"
    ##with pytest.raises (ZeroDivisionError):
    ##    fuel.gauge(0.75)
