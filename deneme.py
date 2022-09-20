kilo = int(input("Geben Sie Ihr Gewicht ein:"))
Größe = float(input("Geben Sie Ihre Körpergröße ein:"))

Größequadrat = (Größe ** 2)

Prozess = (kilo / Großequadrat)
print(Prozess)
if 0 < Prozess < 18.5:
    print("Du bist schwach")
elif 18.5 < Prozess < 24.9:
    print("normal")
elif 24.9 < Prozess < 40.0:
    print("du bist übergewichtig")
elif 40.0 < Prozess:
    print("Sie sind fettleibig")
