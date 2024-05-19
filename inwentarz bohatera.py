inventory =() #pusta krotka

if not inventory:
    print("Nie posiadasz niczego!")

input ("Aby kontynuować misję wciśnij enter.")

inventory = ("miecz","zbroja", "tarcza","napój uzdrawiający")
print ("Zawartość krotki to: ")
print (inventory)

for item in inventory:
    print (item, end=" ")

input ("\n Aby zakończyć grę wciśnij enter.")