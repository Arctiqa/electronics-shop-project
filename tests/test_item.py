from src.item import Item
import pytest


@pytest.fixture
def test_object():
    return Item('Смартфон', 50, 30)


def test_init_(test_object):
    assert test_object.name == 'Смартфон'

    assert test_object.price == 50
    assert test_object.quantity == 30
    assert test_object in test_object.__class__.all


def test_calculate_total_price():
    item1 = Item('item_name1', 30, 20)
    item2 = Item('item_name2', 35, 2)
    assert item1.calculate_total_price() == 600
    assert item2.calculate_total_price() == 70


def test_apply_discount():
    item1 = Item('item_name1', 100, 50)
    item2 = Item('item_name2', 40, 50)
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 100 * item1.pay_rate
    assert item2.price == 40 * item1.pay_rate


def test_instantiate_from_csv():
    Item.instantiate_from_csv('items.csv')

    assert Item.all[-5].name == 'Смартфон'
    assert Item.all[-5].price == '100'
    assert Item.all[-5].quantity == '1'

    assert Item.all[-1].name == 'Клавиатура'
    assert Item.all[-1].price == '75'
    assert Item.all[-1].quantity == '5'


def test_string_to_number():
    assert Item.string_to_number('7') == 7
    assert Item.string_to_number('7.8') == 7


def test_name():
    item1 = Item('Смартфон', 10500, 9)
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_repr():
    item = Item('Смартфон', 105000, 6)
    assert repr(item) == "Item('Смартфон', 105000, 6)"
    assert str(item) == "Смартфон"
