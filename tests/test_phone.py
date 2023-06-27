import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture()
def phone_name():
    return Phone("iPhone 14", 120_000, 5, 2)

def test_init(phone_name):
    assert phone_name.name == "iPhone 14"
    assert phone_name.price == 120000
    assert phone_name.quantity == 5
    assert phone_name.number_of_sim == 2

def test_repr(phone_name):
    assert repr(phone_name) == "Phone('iPhone 14', 120000, 5, 2)"

def test_str(phone_name):
    assert str(phone_name) == "iPhone 14"


def test_add(phone_name):
    item_name = Item("Смартфон", 10000, 20)
    assert item_name + phone_name == 25
    assert phone_name + phone_name == 10
    #assert phone_name + 10 == Exception
