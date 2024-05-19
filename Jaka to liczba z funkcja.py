import random
number = random.randint(1,100)

def welcome():
  """Powitanie użytkownika"""
  print('Witaj w grze "Zgadnij jaka to liczba", zasady są proste... Musisz trafić liczbę w zakresie 1-100 którą komputer wylosował!\n Powodzenia!')


def ask_number():
    """Obliczenia"""
    print("Wpisz liczbe z zakresu 1-100: ")
    tries = 1
    response = int(input())
    while response != number:
      if response < number:
        print("Za mała")
      else:
        print("Za duża")
      response = int(input('Spróbuj jeszcze raz: '))
      tries +=1
    return tries

def main():
  welcome()
  ask = ask_number()
  print("Udało Ci się odgadnąć",'ta liczba to',number,'odgadłeś za', ask,'razem')

main()