inventory = ("miecz", "zbroja","tarcza","napój uzdrawiający")

print ("Zawartość Twojego inwentarza: ")
for item in inventory:
    print (item)
input ("Aby kontynuować grę wciśnij enter.")

print ("Twój dobytek zawiera", len(inventory) , "elementy(-ów)")
input ("Aby kontynuować grę wciśnij enter.")

if "napój uzdrawiający" in inventory:
    print ("Dożyjesz dnia w którym stoczysz walkę!")
indeks = int(input("Wprowadź indeks elementu inwentarza: "))
print ("Pod indeksem",indeks, "znajduje się:",inventory[indeks])

poczatek_wycinka= int(input("Podaj indeks wyznaczający początek wycinka: "))
koniec_wycinka = int(input("Podaj indeks oznaczający koniec wycinka: "))

print ("inventory[", poczatek_wycinka, ":", koniec_wycinka, "] to: ", inventory[poczatek_wycinka:koniec_wycinka] )
input("Aby kontynować grę wciśnij enter.")

print ("Znajdujesz skrzynię, która zawiera: <'złoto', 'klejnoty'>")
chest=("złoto","klejnoty")
print("Dodajesz zawartość skrzyni do swojego inwentarza.")
print("twój aktualny inwentarz to: ")
inventory +=chest
print (inventory)
