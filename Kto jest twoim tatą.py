# Program "Kto jest Twoim tatą?"
# Program umożliwia użytkownikowi wprowadzenie imienia i nazwiska mężczyzny
# Następnie program wyświetla imię i nazwisko jego ojca
# Dodatkowo użytkownik może modyfikować, dodawać lub usuwać pary syn-ojciec

"""
Napisz program Kto jest twoim tatą?, który umożliwia użytkownikowi
wprowadzenie imienia i nazwiska osoby płci męskiej i przedstawia imię
i nazwisko jej ojca. (Możesz dla zabawy wykorzystać nazwiska celebrytów,
osób fikcyjnych lub nawet postaci historycznych). Umożliw użytkownikowi
dodawanie, wymianę i usuwanie par syn-ojciec

Udoskonal program Kto jest moim tatą? poprzez dodanie opcji, która umożliwi
użytkownikowi wprowadzenie imienia i (lub) nazwiska jakiejś osoby i uzyskanie
odpowiedzi, kto jest jej dziadkiem. Twój program powinien nadal wykorzystywać
tylko jeden słownik par syn-ojciec. Pamiętaj, aby włączyć do swojego słownika
kilka pokoleń, tak aby możliwe było tego rodzaju dopasowanie.
"""

Drzewo = {
    "Sebastian Jeszka":"Jacek Jeszka",
    "Jacek Jeszka":"Edmund Jeszka",
    "Stas Gierszewski":"Mateusz Gierszewski",
    "Mateusz Gierszewski":"Stanisław Gierszewski",
    "Marcel Kiedrowski":"Arkadiusz Kiedrowski",
    "Arkadiusz Kiedrowski":"Genio Kiedrowski"
}

choice=None
while choice != "0":
    print ("""
        0. Zamknij program
        1. Poznaj ojca
        2. Dodaj parę syn-ojciec
        3. Zmień ojca
        4. Usuń parę syn-ojciec
        5.[NOWOŚĆ] Sprawdź kto jest dziadkiem!
    """)

    choice=input("Wybierz opcję:  \n")
    if choice =="0":
        print ("Do zobaczenia!")
    if choice=="1":
        syn=input("Podaj imie i nazwisko syna: ")
        if syn in Drzewo:
            ojciec=Drzewo[syn]
            print ("Twoim ojcem jest", ojciec)
        else:
            print ("Nie znam takiej osoby!")
    elif choice == "2":
        syn = input("Podaj imię i nazwisko syna: ")
        if syn not in Drzewo:
            ojciec = input ("Podaj imię i nazwisko ojca: ")
            Drzewo[syn]=ojciec
            print ("Udało się! Nowa para syn-ojciec została dodana!")
        else:
            print ("Ta para już istnieje w bazie!")
    elif choice == "3":
        syn = input("Podaj imię i nazwisko syna: ")
        if syn in Drzewo:
            ojciec=input("Podaj imię i nazwisko ojca: ")
            Drzewo[syn]=ojciec
            print ("Ma już nowego ojca, jest nim",ojciec)
        else:
            print ("Nie znam ojca tej osoby")
    elif choice == "4":
        syn=input("Podaj imię i nazwisko syna: ")
        if syn in Drzewo:
            del Drzewo[syn]
            print (Drzewo)
    elif choice == "5":
        wnuczek=input("Podaj imię i nazwisko osoby, której chcesz poznać dziadka: ")
        if wnuczek in Drzewo:
            syn = Drzewo [wnuczek]
            ojciec=Drzewo[syn]
            print ("Dziadkiem", wnuczek, "jest", ojciec)
        else:
            print ("Niestety nie znam dziadka tej osoby :(")
    else:
        print ("Nie ma takiej opcji w menu!")
        
input ("Aby zakończyć program wciśnij enter.")
