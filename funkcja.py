"""wyświetl instrukcję gry
ustal, do kogo należy pierwszy ruch
utwórz pustą planszę gry
wyświetl planszę
dopóki nikt nie wygrał ani nie padł remis
 jeśli ruch należy do człowieka
 odczytaj ruch człowieka
 zaktualizuj planszę przez zaznaczenie ruchu
 w przeciwnym wypadku
 wyznacz ruch komputera
 zaktualizuj planszę przez zaznaczenie ruchu
 wyświetl planszę
 zmień wykonawcę ruchu"""

 
def instructions():
    """Wyświetl instrukcję gry."""
    print("""
    Witaj w grze kółko i krzyżyk.
    Będzie to ostateczna rozgrywka między Tobą, a komputerem.

    Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
    Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:

                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8

   Przygotuj się. \n             
    """)
#main
print ("Oto instrukcja do gry 'Kółko i krzyżyk': ")
instructions()