# Zamarynuj to
# Demonstruje marynowanie i odkładanie danych na półkę

import pickle, shelve

print ("Marynowanie list.")
variety=["łagodny", "pikantny", "kwaszony"]
shape=["cały", "krojony wzdłuż", "w plastrach"]
brand=["Dawtona", "Klimex", "Vortumus"]

f = open("piklel.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle. dump(brand, f)

f.close()

print("\nOdmarynowanie list.")
f = open("piklel.dat", "rb")

variety=pickle.load(f)
shape=pickle.load(f)
brand=pickle.load(f)

print (variety)
print(shape)
print(brand)

f.close()

print("\n Odkładnanie list na półkę.")
s = shelve.open("pikle2.dat")
s["odmiana"] = ["łagodny", "pikantny", "kwaszony"]
s["kształt"] = ["cały", "krojony wzdłuż", "w plastrach"]
s["marka"] = ["Dawtona", "Klimex", "Vortumnus"]

s.sync()

print("\n Pobieranie list z pliku półki")
print("marka -", s["marka"])
print("ksztalt -", s["kształt"])
print("odmiana -", s["odmiana"])

s.close()

input("Aby zakończyć program wciśnij enter.")