import random
losowanie = random.randint (1, 2)
orzel=0
reszka=0
rzut = 0
while rzut < 100:
    losowanie = random.randint (1, 2)
    rzut +=1
    if losowanie ==1:
        orzel +=1
    elif losowanie ==2:
       reszka +=1
print ("Wypadlo", orzel, "orlow, a reszek wypadlo", reszka)

input("Enter aby zakonczyc: ")

