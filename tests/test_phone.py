from src.phone import Phone
from src.item import Item
import pytest


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_number_of_sim_less_than_0():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
