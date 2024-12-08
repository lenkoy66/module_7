#Учет товаров
from pprint import pprint

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        list_of_prod = file.read()
        file.close()
        return list_of_prod

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for p in products:
            if isinstance(p, Product) and p.name not in self.get_products():
                file.write(f'{p}\n')
            else:
                print(f'Продукт {p.name} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
