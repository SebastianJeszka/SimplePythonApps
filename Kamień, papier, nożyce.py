import random

opcje=["Kamień", "Papier", "Nożyce"]
choice=None
computer_choice = random.choice(opcje)
human_choice=None 
punkty_człowieka=0
punkty_komputera=0
Wybór_człowieka = None

def human_choice():
    """Wybór użytkownika"""

    print("""
    1. Kamień
    2. Papier
    3. Nożyce
    """)
    
    choice = input("Wybierz opcje: ")
    if choice == "1":
        human = "Kamień"
    elif choice =="2":
        human = "Papier"
    elif choice =="3":
        human = "Nożyce"
    
    return human
def wygrana():
    if computer_choice == Wybór_człowieka:
        print("Remis")
        punkty_człowieka +=1
        punkty_komputera +=1
    elif computer_choice == "Kamień" and Wybór_człowieka == "Nożyce":
        print ("Komputer wygrywa")
        punkty_komputera +=1
    elif computer_choice == "Papier" and Wybór_człowieka == "Kamień":
        print ("Komputer wygrywa")
        punkty_komputera +=1
    elif computer_choice == "Nożyce" and Wybór_człowieka == "Papier":
        print ("Komputer wygrywa")
        punkty_komputera +=1
    else:
        print ("Wygrywa człowiek!")
        punkty_człowieka +=1
    

def main():
    Wybór_człowieka = human_choice()
    wygrana()

main()