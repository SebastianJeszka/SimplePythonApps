import random

WORDS=("programowanie", "komputer", "mikrofon", "motywacja")

word=random.choice(WORDS)

high=len(word)
low=-len(word)

for i in word:
    position = random.randrange(low,high)
    print (word[position], end="")
słowo=input("\nUłóż z wymieszanych literek poprawne słowo: ")

while słowo !=word:
    print("To nie jest to słowo!")
    słowo=input("Ułóż z wymieszanych literek poprawne słowo: ")

print ("Gratulacje, odgadłeś słowo!")

    
