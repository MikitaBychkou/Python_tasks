# -*- coding: utf-8 -*-
'''
Napisz funkcję slowa_podobne(s, words), która wyświetli słowa, które są ,,podobne" do napisu s
w tym sensie, że składające się z tych samych znaków — ale ewentualnie występujących inną liczbę razy
#PRZYKŁAD
slowa_podobne('one', ['one', 'two', 'none', 'three', 'neon', 'eon']) 
>> none neon eon
'''

def slowa_podobne(s, words):
    result = []
    my_set = set(s)
    for word in words:
        new_set = set(word)
        if new_set == my_set:
            result.append(word)
    print(result)
    # result = []
    # for word in words:
    #     cond = True
    #     for letter in word:
    #         if letter not in s:
    #             cond=False
    #     if cond:
    #         result.append(word)
    #
    # print(result)


slowa_podobne('one', ['one', 'two', 'none', 'three', 'neon', 'eon'])