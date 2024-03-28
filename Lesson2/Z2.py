# -*- coding: utf-8 -*-
'''

Napisz definicje, która przeprowadzi analizę tekstu. Program powinien wykonać następujące czynności:
- Wczytać tekst
- Podzielić tekst na słowa.
- Usunąć znaki interpunkcyjne i zamienić wszystkie litery na małe litery.
- Utworzyć kolekcję słów i zliczyć ile razy każde słowo występuje w tekście.
- Wyświetlić 10 najczęściej występujących słów wraz z ich liczbami wystąpień.
- Wyświetlić 10 najrzadziej występujących słów wraz z ich liczbami wystąpień.
- Wyświetlić liczbę unikalnych słów w tekście.
- Wyświetlić średnią długość słowa w tekście.
'''

with open('Z2_txt.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    print(line)

arr = line.split()
print(arr)

count_words = {}

for word in arr:
    if word in count_words:
        count_words[word] += 1
    else:
        count_words[word] = 1

print(count_words)

