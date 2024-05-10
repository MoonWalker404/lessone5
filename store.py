# Определение класса Store
class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        else:
            return None

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание объектов класса Store
store1 = Store("Продуктовый магазин 'Фрут'", "Ул. Садовая, 1")
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)
store1.add_item("Молоко", 1.25)

store2 = Store("Магазин Одежды 'Мода'", "Пл. Центральная, 5")
store2.add_item("Футболка", 15.99)
store2.add_item("Джинсы", 29.99)
store2.add_item("Куртка", 49.99)

store3 = Store("Аптека 'Здоровье'", "Ул. Лесная, 10")
store3.add_item("Аспирин", 2.99)
store3.add_item("Витамин С", 5.99)
store3.add_item("Бинт", 1.49)

# Добавление товара
store2.add_item("Шапка", 9.99)
print(f"Товар 'Шапка' добавлен в магазин '{store2.name}'")

# Обновление цены товара
store2.update_item_price("Футболка", 17.99)
print(f"Цена товара 'Футболка' обновлена в магазине '{store2.name}'")

# Удаление товара
store2.remove_item("Джинсы")
print(f"Товар 'Джинсы' удален из магазина '{store2.name}'")

# Запрос цены товара
item_name = "Куртка"
item_price = store2.get_item_price(item_name)
if item_price is not None:
    print(f"Цена товара '{item_name}' в магазине '{store2.name}': {item_price}")
else:
    print(f"Товар '{item_name}' не найден в магазине '{store2.name}'")
