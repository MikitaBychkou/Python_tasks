# -*- coding: utf-8 -*-


'''
1. Utwórz katalog o nazwie zajecia
2. Do pliku dzis.txt zapisz dzisiejszą datę
3. Przenieść plik dzis.txt do katalogu zajecia
4. Utworz listę integerow z w zakresie 1-15.
5. Do pliku liczby.txt w katalogu zajecia zapisz liczby z utworzonej listy, ale tak, aby każdy był w nowej linijce. Upewnij się, że dane nie zostały nadpisane.
6. Do pliku liczby_parzyste.txt zapisz liczby parzyste z utworzonej wcześniej listy, a do pliku liczby_nieparzyste.txt zapisz liczby nieparzyste z tej listy.
7. Wszystkie te pliki z polecenia 6 umieść w katalogu zajecia albo przy tworzeniu albo po zapisaniu do nich.
8. Wyświetl zawartość katalogu zajecia
'''
import os

#wynikiem ma być ["dzis.txt", "liczby.txt", "liczby_nieparzyste.txt", "liczby_parzyste.txt]

z = []
for i in range(1, 16):
    z.append(i)

with open('zajecia/dzis.txt', 'a')as myfile:
    myfile.write("04.09.2024")

with open('zajecia/liczby.txt', 'a')as file:
    for n in z:
        file.write(str(n)+'\n')

with open('zajecia/liczby_parzyste.txt', 'a')as file:
    for n in z:
        if(n % 2 == 0):
            file.write(str(n)+'\n')

with open('zajecia/liczby_nieparzyste.txt', 'a') as file:
    for n in z:
        if (n % 2 != 0):
            file.write(str(n) + '\n')

path = 'zajecia'
content = os.listdir(path)
for name in content:
    print(name)

# os.mkdir('nowykatalog')