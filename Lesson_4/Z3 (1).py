# -*- coding: utf-8 -*-

''''
Zmodyfikuj funkcje kalkulator tak, żeby uwzględniała te błędy:
TypeError: Jeżli args nie zawiera liczb lub kwargs nie zawiera znaków
ZeroDivisionError
IndexError: Jeśli ilość kwargs jest równa lub większa niż args
MyError(zdefiniowany przez Ciebie): Jeśli znak jest inny niż +-*/ wyświetl komunikat o niepoprawnym znaku
'''

# arr = ['t', 'y', 'u']
# for index, value in enumerate(arr):
#     print(index, value)

class MyException(Exception):
    pass
def kalkulator(*args, **kwargs):
    for a in args:
        if not isinstance(a, (int, float)):
            raise TypeError("args nie zawiera liczb")

    for k in kwargs.values():
        if not isinstance(k, str):
            raise TypeError("kwargs nie zawiera znaków")

    if len(kwargs.values()) >= len(args):
        raise IndexError("ilość kwargs jest równa lub większa niż args")
    result = args[0]
    temp_liczba=args[1]

    values = kwargs.values()

    for index, dzialanie in enumerate(values):
        match dzialanie:
          case '+':
            result+=args[index+1]
          case '-':
            result-=args[index+1]
          case '*':
            result*=args[index+1]
          case '/':
            try:
                result/=args[index+1]
            except ZeroDivisionError:
                print("you can't divide by 0")
          case _:
              raise MyException("Wprowadzony znak jest inny niż +-*/")
    return result

print(kalkulator(1,3,2,działanie_1='+',działanie_2='-'))