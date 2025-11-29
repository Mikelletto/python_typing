def concatenateAndPower(first,second):
    connected = first+second
    dist = list(dict.fromkeys(connected))
    dist = [pow(x,3) for x in dist]
    return dist

x = [1,2,3]
y = [2,3,4,5,6]

wynik = concatenateAndPower(x,y)
print(wynik)
