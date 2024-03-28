# -*- coding: utf-8 -*-
"""
Napisz program, który umożliwia zarządzanie książką adresową. Program powinien umożliwiać użytkownikowi wykonywanie następujących operacji:

Dodawanie nowego kontaktu do książki adresowej.
Wyświetlanie wszystkich kontaktów z książki adresowej.
Wyszukiwanie kontaktu po nazwie.
Usuwanie kontaktu z książki adresowej.

Użyj słownika, gdzie kluczem będzie nazwa kontaktu, a wartością będzie lista informacji o kontakcie (np. imię, nazwisko, numer telefonu).
"""
dict={}

def addNew(name, number):
    dict[name]=number

def show():
    print(dict)

def find(name):
    print(dict.get(name))

def delete(name):
    dict.pop(name)

addNew("Pit","123")
addNew("Max","321")
addNew("Pit","222")
show()
find("Pit")
delete("Pit")
show()


