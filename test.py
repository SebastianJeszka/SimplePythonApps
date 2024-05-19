#Jaka to liczba (na funkcjach)

import random
liczba = random.randint(1,100)

def przywitanie():
    """Tutaj witamy użytkownika"""
    print ("Witaj w grze jaka to liczba, komputer losuje liczbe z zakresu 1-100 i ty musisz ją odgadnąć, powodzenia!")

def obliczenia():
    """Tutaj jest mechanizm gry"""
    tries=1
    response = int(input("Podaj liczbe: "))
    while response != liczba:
        if response > liczba:
            print ("Za duża")
        else:
            print ("Za mała")
        response = int(input("Spróbuj ponownie: "))
        tries+=1
    return tries

def main():
    przywitanie()
    ask= obliczenia()
    print("Udało Ci się odgadnąć",'ta liczba to',liczba,'odgadłeś za', ask,'razem')

main()

        
    