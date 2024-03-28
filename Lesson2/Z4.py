# -*- coding: utf-8 -*-
"""
Stwórz listę tupli, gdzie każda tupla zawiera informacje o produkcie: nazwę, cenę i kategorię. 
#Przykład
products = [
    ("Laptop", 1500, "Elektronika"),
    ("Kubek", 10, "Dom"),
    ("Słuchawki", 100, "Elektronika"),
    ("Sok", 5, "Żywność"),
    ("Telefon", 2000, "Elektronika"),
    ("Długopis", 2, "Biuro"),
    ("Papier", 10, Biuro),
    ("Koszulka", 20, "Moda"),
    ("Pomarańcza", 5,"Żywność" )
]

Utwórz set zawierający wszystkie unikalne kategorie produktów.
Oblicz średnią cenę produktów oraz średnią cene produków z danej kategorii.
Znajdź najdroższy i najtańszy produkt oraz najdroższy i najtańszy produkt z danej kategorii.
Stwórz listę zawierającą nazwy wszystkich produktów o cenie powyżej 100 zł.
Wypisz informacje o produktach, których kategoria zaczyna się od litery "E".
"""
products = [
    ("Laptop", 1500, "Elektronika"),
    ("Kubek", 10, "Dom"),
    ("Słuchawki", 100, "Elektronika"),
    ("Sok", 5, "Żywność"),
    ("Telefon", 2000, "Elektronika"),
    ("Długopis", 2, "Biuro"),
    ("Papier", 10, "Biuro"),
    ("Koszulka", 20, "Moda"),
    ("Pomarańcza", 5,"Żywność")
]

my_products = set()
for product in products:
    my_products.add(product[2])
print(my_products)
# ///////////////////////////////////
result = 0
for product in products:
    result += product[1]

print("average of all products:", result/len(products))


for kategoria in my_products:
    count = 0
    result = 0
    for product in products:
        if product[2] == kategoria:
            count += 1
            result += product[1]
    print("kategoria:", kategoria, "-> average of products:", result/count)
# ///////////////////////////////////

max = products[0][1]
maxIndex = 0
for index, product in enumerate(products):
    if product[1] > max:
        max = product[1]
        maxIndex = index
print("Max:", products[maxIndex][0])

