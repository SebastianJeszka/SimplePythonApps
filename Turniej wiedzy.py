#Turniej wiedzy
#Gra sprawdzająca wiedzę ogólną, odczytując dane ze zwykłego pliku tekstowego.

import sys

def open_file(file_name, mode):
    """Otwórz plik"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku", file_name, "Program zostanie zakończony.\n",e)
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Zwróć kolejny wiersz pliku kwiz po sformatowaniu go."""
    line=the_file.readline()
    line= line.replace("/", "\n")
    return line

def next_block(the_file):
    """Zwróć kolejny blok danych z pliku kwiz."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []

    for i in range(4):
        answers.append(next_line(the_file))
    
    correct= next_line(the_file)
    if correct:
        correct=correct[0]
    
    explanation= next_line(the_file)

    return category, question, answers, correct, explanation

def welcome(title):
    """Przywitaj gracza i pobierz jego nazwę"""
    print ("\n Witaj w Turnieju Wiedzy!")
    print ("\t\t", title, "\n")

def main():
    trivia_file = open_file("kwiz.txt", "r")
    title=next_line(trivia_file)
    welcome(title)
    score = 0

    #Pobierz pierwszy blok
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        #Zadaj pytanie
        print (category)
        print(question)
        for i in range(4):
            print ("\t", i + 1, "-", answers[i])
        #uzyskaj odpowiedź
        aswer = input("Jaka jest Twoja odpowiedź?: ")
        #Sprawdź odpowiedź
        if answer == correct:
            print ("Odpowiedź prawidłowa!", end= " ")
            score +=1
        else:
            print("\n Odpowiedź niepoprawna.", end= " ")
        print (explanation)
        print ("Wynik: ", score, "\n\n")
        #Pobierz kolejny blok
        category, question, answers, correct, explanation = next_block(trivia_file)
    trivia_file.close()
    print("To nie było ostatnie pytanie!")
    print("Twój końcowy wynik wynosi", score)

main()

input("\n\n Aby zakończyć program, naciśnij klawisz enter.")

