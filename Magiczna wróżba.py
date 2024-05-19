import random

wrozba_1 = "Pojedziesz na mecz Realu"
wrozba_2 = "Obejrzysz film z Cristiano Ronaldo"
wrozba_3 = "Ktos krzyknie na ulicy \"Siuuu\""
wrozba_4 = "Wygrasz w lotto"
wrozba_5 = "Będziesz jezdził oplem"

losowa = (random.randint(1,5))
if losowa == 1:
    print (wrozba_1)
elif losowa == 2:
    print (wrozba_2)
elif losowa == 3:
    print (wrozba_3)
elif losowa == 4:
    print (wrozba_4)
elif losowa == 5:
    print (wrozba_5)
else:
    print ("Nie ma takiej wrozby!")
