# -*- coding: utf-8 -*-
#Napisz funkcje silnii używając rekurencji

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

