#Najlepszy wynik 2.0
#Demonstracja sekwencji zagnieżdzonych

scores = []
choice = None

while choice != 0:
    print ("""
    Najlepszy wynik 2.0

    0. Zakończ
    1. Wyświetl wynik
    2. Dodaj wynik
    """)
    choice = input ("Wybierz opcje: ")

    #zakończ
    if choice == "0":
        print ("Do widzenia!")

    elif choice == "1":
        #Wyswietl tabele najlepszych wyników
        print ("Najlepsze wyniki \n")
        print ("GRACZ \t WYNIK")
        for entry in scores:
            score, name = entry
            print (score, "\t", name)

    elif choice == "2":
        #add
        name = input("Podaj nazwe gracza: ")
        score = int(input("Podaj wynik uzyskany przez gracza: "))
        entry=(name, score)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores [:5]
    else:
        print ("Niestety", choice, "to nie jest dobry wybór :(")
        input ("Aby zakończyć program wciśnij enter")
