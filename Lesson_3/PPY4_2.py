# -*- coding: utf-8 -*-
#Napisz funkcje validate_pesel, która przyjmuje ciąg znaków (str) i sprawdza, czy jest on poprawnie sformatowanym numerem PESEL.
#Numer PESEL składa się z 11 cyfr. W celu sprawdzenia sumy kontrolnej użyj wag [1, 3, 7, 9, 1, 3, 7, 9, 1, 3].
#Tutaj suma kontrolna to wynik odejmowania jedności od 10.
#Funkcja powinna zwracać wartość logiczną: True jeśli numer PESEL jest poprawny, False w przeciwnym przypadku.

def validate_pesel(pesel):
  if len(pesel) != 11:
    return False

  if not pesel.isdigit():
    return False

  wag = [1,3, 7, 9, 1, 3, 7,9, 1,3 ]
  sum = 0
  for i in range(10):
    sum += int(pesel[i]) * wag[i]
  print(sum)

  last_number = 10 - (sum % 10)
  print(last_number)

  if last_number == 10:
    last_number = 0

  return last_number == int(pesel[10])

print(validate_pesel('12345678901'))  # False
print(validate_pesel('44051401458'))  # True