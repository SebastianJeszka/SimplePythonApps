komunikat=input("Wprowadz komuninikat: ")
nowy_komunikat=""

SAMOGŁOSKI = "aąeęiouóy"

print ()

for letter in komunikat:
    if letter.lower() not in SAMOGŁOSKI:
        nowy_komunikat += letter
        print ("Został utworzony nowy łańcuch: ", nowy_komunikat)

print ("Twój komunikat bez samogłosek to: ", nowy_komunikat)