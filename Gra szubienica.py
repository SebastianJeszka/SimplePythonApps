# Szubienica

# Klasyczna gra w szubienicę. Komputer losowo wybiera słowo,
# a gracz próbuje odgadnąć jego poszczególne litery. Jeśli gracz
# nie odgadnie w porę całego słowa, mały ludzik zostaje powieszony.
# import modułów

import random

# stałe
HANGMAN = (
"""
 ------
 | |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 | |
 | O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 | |
 | O
 | -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 | |
 | O
 | /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 | |
 | O
 | /-+-/
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 | |
 | O
  | /-+-/
 | |
 |
 |
 |
 |
----------
""",
"""
 ------
 | |
 | O
 | /-+-/
 | |
 | |
 | |
 | |
 |
----------
""",
"""
 ------
 | |
 | O
 | /-+-/
 | |
 | |
 | | |
 | | |
 |
----------
""")

Max_wrong = len(HANGMAN)-1
Words = ("POLITECHNIKA", "SAMOCHÓD", "KOBIETA", "TOWARZYSTWO", "MARZEC", "KASZUBY", "PYTHON")
Word = random.choice(Words)
so_far = "-" * len(Word)
wrong = 0
used = []  
while wrong != Max_wrong and so_far != Word:
    print (HANGMAN[wrong])
    print ("Wykorzystałeś już następujące litery: ", used)
    print ("Na razie zagadkowe słowo wygląda tak: ", so_far)

    guess= input ("Podaj literę: ")
    guess = guess.upper()
    while guess in used:
        print ("Już wykorzystałeś literę", guess)
        guess = input ("Podaj inną litere: ")
        guess = guess.upper()
    used.append(guess)

    if guess in Word:
        print ("Taak! Litera", guess, "znajduje się w tym słowie!")
        new = ""
        for i in range(len(Word)):
            if guess in Word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far=new
    else:
        print ("Niestety litera", guess, "Nie znajduje sie w tym słowie!")
        wrong += 1
    
    if wrong == Max_wrong:
        print (HANGMAN[wrong])
        print ("Niestety, ale zostałes powieszony")
    else:
        print ("Odgadłeś! ")
        print ("Odgadywane słowo to:", Word)
input ("Aby zakończyć program wciśnij enter")