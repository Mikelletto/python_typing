
def contains_number(lista, liczba):
    return liczba in lista  # Zwraca True, jeśli liczba jest w liście, False jeśli nie

moja_lista = [1, 3, 5, 7, 9]
szukana_liczba = int(input("Podaj drugi parametr: "))

wynik = contains_number(moja_lista, szukana_liczba)
print(wynik)