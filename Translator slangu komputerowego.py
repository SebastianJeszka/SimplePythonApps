# Translator slangu komputerowego
# Demonstruje używanie słowników

geek = {"404": "ignorant; od używanego w sieci WWW komunikatu o błędzie 404\n - nie  znaleziono strony.",
 "Googling": "googlowanie; wyszukiwanie w internecie informacji dotyczących jakiejś osoby.",
 "Keyboard Plaque" : "(skojarzone z kamieniem nazębnym)zanieczyszczenia nagromadzone w klawiaturze komputera.",
"Link Rot" : "(obumieranie linków) proces, w wyniku którego linki do stron WWW  stają się nieaktualne.",
 "Percussive Maintenance" : "(konserwacja perkusyjna)naprawa urządzenia elektronicznego przez stuknięcie.",
 "Uninstalled" : "(odinstalowany) zwolniony z pracy; termin szczególnie popularny w okresie bańki internetowej."}


choice = None

while choice != "0":
    print ("""
     0 - zakończ
     1 - znajdź termin
     2 - dodaj nowy termin
     3 - zmień definicję terminu
     4 - usuń termin
    """)
    choice = input ("Wybierasz opcje: ")

    if choice == "0":
        print ("Do widzenia!")
    elif choice == "1":
        termin = input ("Podaj termin jaki Cie interesuje: ")
        if termin in geek:
            definition = geek[termin]
            print("\n", termin, "oznacza", definition)
            #print ("Znam definicje tego terminu! \n")
            #print (geek["404"])
        else:
            print ("Niestety nie znam definicji tego terminu :(")
    elif choice == "2":
        termin = input ("Jaki termin mam dodać?: ")
        if termin not in geek:
            definition = input("Podaj definicje tego terminu: ")
            geek[termin] = definition
            print ("termin został pomyślnie dodany!")
        else:
            print ("Znamy już definicje tego terminu! \n")
    elif choice == "3":
        termin = input ("Jaki termin chcesz przedefiniować?: ")
        if termin in geek:
            definition = input("Jaka jest nowa definicja?: ")
            geek[termin] = definition
            print ("Termin słowa", termin, "został przedefiniowany pomyślnie")
        else:
            print ("Niestety nie znamy definizji słowa", termin, "spróbój dodać jeg definicje do naszego słownika!")
    elif choice == "4":
        termin = input ("Podaj termin jaki chcesz usunąć: ")
        if termin in geek:
            del geek[termin]
            print ("Pomyślnie usuneliśmy termin ze słownika")
        else:
            print ("Niestety nie możemy usunąć tego terminu, bo on nie istnieje w naszym słowniku!")
    else:
        print ("Nieznamy tej opcji") 

input ("Wciśnij enter aby zakończyć program.")
    
            
