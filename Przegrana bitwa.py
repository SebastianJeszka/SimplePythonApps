print ("Twoj bohater otoczony jest przez liczbe troli")

zdrowie = 10
trole = 0
Obrazenia = 3

while zdrowie > 0:
    zdrowie -= Obrazenia
    trole += 1
    print ("Bohater pokonuje trola, ale traci", Obrazenia, "punkty zdrowia")

print ("Zabiłes", trole, "troli zanim umarłes")