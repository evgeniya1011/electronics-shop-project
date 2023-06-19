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


