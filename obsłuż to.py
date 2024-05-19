#Obsłuż to
#Demonstruje obsługę wyjątków

#try/ except
try:
    num=float(input("Wprowadź liczbę: "))
except:
    print ("Wystąpił jakiś błąd!")

#Specyfikacja typu wyjątku

try:
    num=float(input("\n Wprowadź liczbę: "))
except ValueError:
    print("To nie była liczba!")

#Obsłuż kilka typów wyjątków
print()
for value in (None, "Hej!"):
    try:
        print("Próba konwersji:", value, "-->", end=" ")
        print (float(value))
    except TypeError:
        print("Możliwa jest tylko konwersja łańcucha lub liczby!")
    except ValueError:
        print("Możliwa jest tylko konwersja łańcucha cyfr!")

#Pobierz argument wyjątku

try:
    num=float(input("\n Wprowadź liczbę: "))
except ValueError as e:
    print("To nie była liczba! Lub wyrażając to na sposób Pythona...")
    print (e)

#try/except/else

try:
    num=float(input("\n Wprowadź liczbę: "))
except ValueError:
    print("To nie była liczba!")
else:
    print("Wprowadziłeś liczbę", num)

input ("\n Aby zakończyć program wciśnij enter.")