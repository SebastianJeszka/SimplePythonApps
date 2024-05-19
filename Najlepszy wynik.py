#Najlepsze wyniki
#Demonstruje metody listy

scores =[]
choice = None

while choice != 0:
    print(
    """
    Najlepsze wyniki
    0 - zakończ
    1 - pokaż wyniki
    2 - dodaj wyniki
    3 - usuń wyniki
    4 - posortuj wyniki
    """
    )

    choice = input("Wybierasz opcję: ")
    print ()

    if choice == "0":
        print ("Do widzenia!")

    #Wpisz tabelę najlepszych wyników
    elif choice == "1":
        print ("Najlepsze wyniki")
        for score in scores:
            print (score)
    #dodaj wynik
    elif choice =="2":
        score=int(input("Jaki wynik uzyskałes?: "))
        scores.append(score)
    #usuń wynik
    elif choice == "3":
        score=int(input ("Który wynik chcesz usunąć?: "))
        if score in scores:
            scores.remove(score)
        else:
            print ("Nie ma takiego wyniku na liscie wyników!")
    #sortowanie wyników
    elif choice =="4":
        scores.sort(reverse=True)
    else:
        print ("Niestety", choice, "nie jest prawidłowym wyborem :(")
        input ("Aby zakończyć program kliknij enter.")
