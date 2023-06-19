"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def item_name():
    return Item("Смартфон", 10000, 20)


def test_item_init(item_name):
    assert item_name.price == 10000
    assert item_name.name == "Смартфон"
    assert item_name.quantity == 20


def test_item_calculation(item_name):
    assert item_name.calculate_total_price() == 200000.0


def test_item_discount(item_name):
    item_name.pay_rate = 0.8
    item_name.apply_discount()
    assert item_name.price == 8000.0


def test_get_name(item_name):
    assert item_name.name == "Смартфон"


def test_set_name(item_name):
    item_name.name = "СуперСмартфон"
    assert item_name.name == "СуперСмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item_name1 = Item.all[0]
    assert item_name1.name == "Смартфон"
    item_name2 = Item.all[1]
    assert item_name2.name == "Ноутбук"


def test_string_to_number():
    Item.instantiate_from_csv()
    assert Item.string_to_number(5) == 5
