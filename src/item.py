class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all: list[str] = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        if not isinstance(name, str):
            raise TypeError('Неправильный тип данных для name(str)')
        if not isinstance(price, (int, float)):
            raise TypeError('Неправильный тип данных для unit_cost(int, float)')
        if not isinstance(quantity, int):
            raise TypeError('Неправильный тип данных для quantity(int)')
        if quantity <= 0 or price <= 0:
            raise ValueError('ValueError')

        self.name = name
        self.price = price
        self.quantity = quantity

        if name in self.all:
            raise ValueError('Имя уже есть в списке')

        self.all.append(name)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
