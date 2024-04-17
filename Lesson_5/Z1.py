# -*- coding: utf-8 -*-
'''
- Napisz klasę Kwadrat, Trójkąt, które są subklasami klasy Wielokąt
- Klasa Wielokąt ma zawierać  
    -Metodę askNSides(), która pyta użytkownika o ilość boków wielokąta (która się przyda tylko, gdy wywołamy obiekt poprzez klasę Wielokąt)
    -Metode inputSides(), która przyjmuje (od użytkownika przez input) wielkość każdego boku
    -Metode dispSides(), która wyświetla długości boków
    -Metode circuit(), która wyświetla obwód
    
- Klasa Trójkąt ma zwierać:
    -Zainicjowanie liczby boków trójkąta do 3 przez wywołanie metody __init__ klasy Polygon
    -Metode area(), która liczy pole, o wskazanych przez użytkownika długościach
    -Metoda isright(), która sprawdza czy trójkąt jest prostkątny
    
- Klasa Kwadrat ma zwierać:
    -Zainicjowanie liczby boków kwadratu do odpowiednio 1 przez wywołanie metody __init__ klasy Polygon
    -Metode area(), która liczy pole, o wskazanych przez użytkownika długościach
'''
import math


class Wielokat:
    def __init__(self, numberOfSize):
        self.numberOfSize = numberOfSize
        self.sizeOfSides = [0 for _ in range(numberOfSize)]

    def askNSides(self):
        self.numberOfSize = int(input("Enter number of size: "))

    def inputSides(self):
        self.sizeOfSides = [int(input("Enter size of side: ")) for _ in range(self.numberOfSize)]

    def dispSides(self):
        for side, size in enumerate(self.sizeOfSides):
            print(f"side-{side}, size-{size}")

    def circuit(self):
        print(sum(self.sizeOfSides))

    def __str__(self):
        return f"{self.numberOfSize} : sise of sides - {self.sizeOfSides}"

class Trojkat(Wielokat):
    def __init__(self):
        super().__init__(3)

    def area(self):
        a, b, c = sorted(self.sizeOfSides)
        tmp = sum(self.sizeOfSides)/2
        result = math.sqrt(tmp * (tmp-a)*(tmp-b)*(tmp-c))
        print("area is: "+str(result))

    def isright(self):
        a, b, c = sorted(self.sizeOfSides)
        print(a, b, c)

        if a**2+b**2 == c**2:
            print("jest prostkątny")
        else:
            print("nie jest prostkątny")


class Kwadrat(Wielokat):
    def __init__(self):
        super().__init__(1)

    def area(self):
        print("area is: "+str(sum(self.sizeOfSides)**2))


# w = Wielokat(4)
# Wielokat.askNSides(w)
# w.inputSides()
# w.dispSides()
# w.circuit()
# print(w)

t = Trojkat()
t.inputSides()
t.dispSides()
t.circuit()
t.area()
t.isright()
print(t)

k = Kwadrat()
k.inputSides()
k.dispSides()
k.area()
print(k)










