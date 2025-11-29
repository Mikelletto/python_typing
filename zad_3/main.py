def is_even_number(number):
    return number % 2 == 0  # Zwraca True, jeśli liczba jest parzysta, False jeśli nie

# Pobranie liczby od użytkownika i konwersja na int
liczba = int(input("Podaj liczbę: "))

wynik = is_even_number(liczba)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
