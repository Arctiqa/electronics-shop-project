import csv
import os.path


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
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"

    def __str__(self):
        return f"'{self.name}', '{self.price}', '{self.quantity}'"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        with open(os.path.join(os.path.dirname(__file__), csv_file)) as csvfile:
            reader = list(csv.DictReader(csvfile))
            for row in reader:
                name, price, quantity = row.values()
                Item(name, price, quantity)

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
