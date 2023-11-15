from src.item import Item
import pytest


@pytest.fixture()
def clear_class_items():
    Item.class_items = []


def test_calculate_total_price(clear_class_items):
    item1 = Item('item_name1', 30, 20)
    item2 = Item('item_name2', 35, 2)
    assert item1.calculate_total_price() == 600
    assert item2.calculate_total_price() == 70


def test_apply_discount(clear_class_items):
    item1 = Item('item_name3', 100, 50)
    item2 = Item('item_name4', 40, 50)
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 100 * item1.pay_rate
    assert item2.price == 40 * item1.pay_rate


@pytest.mark.parametrize('name, cost, quantity', [(4, 40, 40),
                                                  ('name1', 30, 'str'),
                                                  ('name2', '', 38)])
def test_init_raises(name, cost, quantity):
    with pytest.raises(TypeError):
        Item(name, cost, quantity)


@pytest.mark.parametrize('name, cost, quantity', [('name1', 45, -38),
                                                  ('name2', -45, 38)])
def test_init_value_errors(name, cost, quantity):
    with pytest.raises(ValueError):
        Item(name, cost, quantity)


def test_name_already_list():
    with pytest.raises(ValueError):
        Item('item_name', 100, 50)
        Item('item_name', 40, 50)
