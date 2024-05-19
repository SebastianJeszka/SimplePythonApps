import random

word = "indeks"
print ("Wartość zmiennej \'word\' to: ", word)

high = len(word)
low = -len(word)

for i in range (10):
    position = random.randrange(low, high)
    print ("Word [", position, "]\t", word[position])

