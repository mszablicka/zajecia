# -*- coding: utf-8 -*-
"""30.10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nhVMK5D_188mEFmdm3PTeR4d7pNjfjLi

Zadanie 1
"""

def wyswietl_imiona(imiona):
    if len(imiona) == 5:
        for imie in imiona:
            print(imie)
    else:
        print("Podano niepoprawną liczbę imion. Proszę podać 5 imion.")

lista_imion = ["Jakub", "Ola", "Darek", "Łukasz", "Ewa"]
wyswietl_imiona(lista_imion)

"""Zadanie 2"""

# Wersja 1
def pomnoz_elementy(lista):
    wynik = []
    for liczba in lista:
        wynik.append(liczba * 2)
    return wynik


lista = [1, 2, 3, 4, 5]
wynik = pomnoz_elementy(lista)
print(wynik)

# Wersja 2
def pomnoz_elementy(lista):
    return [liczba * 2 for liczba in lista]

lista = [1, 2, 3, 4, 5]
wynik = pomnoz_elementy(lista)
print(wynik)

"""Zadanie 3"""

def wyswietl_parzyste_elementy(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)

lista = list(range(1, 11))
wyswietl_parzyste_elementy(lista)

"""Zadanie 4"""

def wyswietl_co_drugi_element(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])

lista = list(range(1, 11))
wyswietl_co_drugi_element(lista)