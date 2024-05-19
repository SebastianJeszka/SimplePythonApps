import random

name=input("Podaj swoje imie: ")
print ("Witaj ", name)
print ("Gra polega na odgadnięciu liczby z przedziału 1-100")
print ("Jeśli nie odgadniesz liczby poinformujemy Ciebie czy ta liczba jest większa czy mniejsza")
print ("Masz 10 prób!")

the_number = random.randint(1, 100)
guess = int(input("Podaj liczbe: "))
tries = 1

while guess != the_number:
    print ("To Twoja", tries, "próba!")
    if guess > the_number:
        print ("za duza")
    else:
        print ("za mala")
    
    guess = int(input("Podaj liczbe: "))
    tries += 1
    if tries > 9:
        print ("Niestety przegrales")
        break
if guess == the_number:
    print ("WYGRALES!")
input ("Aby zakonczyc wcisnij enter")