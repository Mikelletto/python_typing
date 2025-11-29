def isGreaterThanThird(x,y,z):
    return x+y>z

first = int(input("Podaj pierwszą liczbe: "))
second = int(input("Podaj drugą liczbe: "))
third = int(input("Podaj trzecią liczbe: "))

wynik = isGreaterThanThird(first,second,third)
print(wynik)