#zad1
print(2+2)
print(5/2)
print(10*5)
print(25*33/5+2)
print()

#zad2
imie=input("podaj imie\n")
print("Witaj "+imie)

#zad3
print(float(int(input("Podaj 1 liczbe \n")) + int(input("Podaj 2 liczbe \n"))))

#zad4

print(str(sum(range(8,81,1))))


#zad 5

from datetime import date
today = date.today()

data=date(2017,1,1)
czas= abs(today-data)
print(str(czas.days))

#zad 6

while True:
    x = input("Wybierz dzialanie: \n1 - Dodawanie \n2 - Odejmowanie \n3 - Mnozenie\n4 - Dzielenie\n0 - Koniec\n")
    x = int(x)

    if x == 1:
        a = int(input("Podaj 1 liczbe: \n"))
        b = int(input("Podaj 2 liczbe: \n"))
        print(a+b)
    elif x == 2:
        a = int(input("Podaj 1 liczbe: \n"))
        b = int(input("Podaj 2 liczbe: \n"))
        print(a-b)
    elif x == 3:
        a = int(input("Podaj 1 liczbe: \n"))
        b = int(input("Podaj 2 liczbe: \n"))
        print(a*b)
    elif x == 4:
        a = int(input("Podaj 1 liczbe: \n"))
        b = int(input("Podaj 2 liczbe: \n"))
        print(a/b)
    elif x == 0:
        break
