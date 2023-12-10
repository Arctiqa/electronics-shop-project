import csv
import os.path


class InstantiateCSVError(Exception):
    def __init__(self, filename):
        super().__init__(f'Файл {filename} поврежден')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Error')
        else:
            return self.quantity + other.quantity

    @name.setter
    def name(self, value):
        self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        try:
            with open(os.path.join(os.path.dirname(__file__), csv_file), encoding='cp1251') as csvfile:
                reader = list(csv.DictReader(csvfile))
                print(len(reader))
            if len(reader) == 0 or len(reader[0]) != 3:
                raise InstantiateCSVError(csv_file)
            for row in reader:
                name, price, quantity = row['name'], row['price'], row['quantity']
                Item(name, float(price), int(quantity))
        except FileNotFoundError:
            raise f'Файл {csv_file} отсутствует'

            # for row in reader:
            #     name, price, quantity = row.values()
            #     if name not in [i.name for i in Item.all]:
            #         Item(name, price, quantity)
            #         # print(Item.all)
            #     else:
            #         for i in Item.all:
            #             if i.name == name:
            #                 i.price = price
            #                 i.quantity = quantity

    @staticmethod
    def string_to_number(value):
        value = int(float(value))
        return value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

#
# Item.instantiate_from_csv('items.csv')
# print(Item.all)