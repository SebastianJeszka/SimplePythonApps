"""
2. Napisz program Kreator postaci do gry z podziałem na role. Gracz powinien
otrzymać pulę 30 punktów, którą może spożytkować na cztery atrybuty: siła,
zdrowie, mądrość i zręczność. Gracz powinien mieć możliwość przeznaczania
punktów z puli na dowolny atrybut, jak również możliwość odbierania
punktów przypisanych do atrybutu i przekazywania ich z powrotem do puli.
"""
#Kreator postaci

Atrybuty = {
    "Siła":0,
    "Zdrowie":0,
    "Mądrość":0,
    "Zręczność":0
}
Punkty=30

print ("Twoja postać ma do rozdysponowania 30 punktów umiejętności!")
print ("Twoje aktualne statystyki wyglądają w następująco: \n")

for k, v in Atrybuty.items():
    print (k, "- aktualnie wynosi:", v)

while Punkty > 0:
    choice = input ("Wpisz nazwę atrybutu jaki chcesz edytować: ")
    if choice in Atrybuty:
        print ("Modyfikujesz parametr", choice)
        Point = int(input("O ile punktów chcesz zwiększyć lub zmniejszyć (jeśli zmniejszyć dopisz '-' przed liczbą) dany atrybut?: "))
        if Point <= Punkty:
            if (Atrybuty[choice] + Point) >= 0:
                Atrybuty[choice] += Point
                Punkty -= Point
                print (Atrybuty[choice], "została powiększona o", Point, "punkty!")
                print ("Do dyspozycji masz jeszcze", Punkty, "punkty(-ów)")
            else:
                print("Atrybut nie może być mniejszy niż 0!")
        else:
            print("Nie masz do dyspozycji tylu punktów umiejętności!\n")
    else:
        print ("Podałeś blędną nazwę atrybutu!")
    print("Twoje aktualne statystyki wyglądają w następująco: ")
    for k, v in Atrybuty.items():
        print (k, "- aktualnie wynosi:", v)
    print("Do wykorzystania pozostało Ci", Punkty, "punktów")
    

print("Wykorzystałeś już wszystkie punkty umiejętnośći!")
choice_now = input("Chcesz dokonać zmian? TAK/NIE ")
choice_now=choice_now.upper()
if choice_now == "TAK":
    input()
elif choice_now == "NIE":
    input ("Wciśnij enter aby zakończyć program!")
else: 
    print ("Nie rozumiem!")
    input ("Wciśnij enter aby zakończyć program!")
