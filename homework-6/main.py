from src.item import Item

if __name__ == '__main__':
    # Файл broken_csv.csv отсутствует.
    Item.instantiate_from_csv('not_existing_file.csv')
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле broken_csv.csv удалена последняя колонка.
    # Item.instantiate_from_csv('../tests/broken_csv.csv')
    # InstantiateCSVError: Файл item.csv поврежден
