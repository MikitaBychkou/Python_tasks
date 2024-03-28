# -*- coding: utf-8 -*-
#Napisz funckje, która przyjmuje dowolną ilość liczb (args*) i znaków działania (kwargs**), gdzie znakami działania mogą być:
#'+', '-', '*', '/'
#Funckcja ma zwracać wynik działania na liczbach
def kalkulator(*args, **kwargs):

    karr = []
    for key, value in kwargs.items():
        karr.append(value)

    arr = list(args)
    for i in range(len(karr)):
        match karr[i]:
            case "*":
                arr[i+1] = arr[i] * arr[i+1]
            case "+":
                arr[i+1] = arr[i] + arr[i+1]
            case "-":
                arr[i+1] = arr[i] - arr[i+1]
            case "/":
                arr[i+1] = arr[i] / arr[i+1]
    print(arr[len(arr)-1])

#Przykładowe użycie funkcji
kalkulator(10,8,2, działanie_1='*', działanie_2="+") #82