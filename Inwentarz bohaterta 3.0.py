#Inwentarz bohatera 3.0
#Demonstracja Listy
#Tworzenie listy i wyświetlanie jej zawartości
#pętla for

inventory = ["miecz", "zbroja", "tarcza", "napój uzdrawiający", "złoto", "klejnoty"]
print ("Elementy Twojego inwentarza: ")
for item in inventory:
    print (item, end=", ")

print ("Twój dobytek zawiera", len(inventory), "elementów.")
input ("Aby kontynuować wciśnij enter: ")

if "napój uzdrawiający" in inventory:
    print ("Dożyjesz dnia, w którym stoczysz walkę")

index = int(input("Wprowadz indeks elementu inwentarza: "))
print ("Pod indeksem o numerze", index, "znajduje się", inventory[index], ".")

start=int(input("Podaj indeks wyznaczający początek wycinka: "))
finish=int(input("Podaj indeks wyznaczający koniec wycinka: "))

print ("inventory [", start, ":", finish, "] to: ", end=" ")
print (inventory[start:finish])
input ("Aby kontynować grę wciśnij enter")

chest = ("złoto", "klejnoty")
print ("Znajdujesz skrzynię, która zawiera: ")
print (chest)
print ("dodajesz zawartośc skrzyni do swojego inwentarza")
inventory += chest
print ("Twój aktualny inwentarz to: ")
print (inventory)
input ("Aby kontynuować wciśnij enter!")

#przypisz poprzez indeks

print ("Wymieniasz swój miecz na kusze!")
inventory [0] = "kusza"
print ("Twój aktualny inwentarz to: ")
print (inventory)
input ("Aby kontynuować grę wciśnij enter!")

print ("Zużywasz swoje złoto i klejnoty na zakup kuli do wrózenia. ")
inventory [4:6] = ["Kula do wrózenia"]
print ("Twój aktualny inwentarz to: ")
print (inventory)
input ("Aby kontynuowac gre wcisnij enter: ")

#usun element

print ("W wielkiej bitwie Twoja tarcza została zniszczona!")
del inventory [2]
print ("Twój aktualny inwentarz to: ")
print (inventory)

#usun wycinek

print ("Twoja kusza i zbroja zostały skradzione przez złodzieji")
del inventory[:2]
print ("Twój aktualny inwentarz to: ")
print (inventory)