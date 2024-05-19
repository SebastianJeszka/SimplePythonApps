import random

słowa=["oko", "czoło", "głowa", "nos", "policzki", "usta"]

użyte = []

while słowa:

    losowo=random.choice(słowa)
    if losowo in słowa:
        użyte.append(losowo)
        słowa.remove(losowo)
       
print (użyte)
input("Aby zakończyć program kliknij enter!")
