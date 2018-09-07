"""

Kitchen.py.

Lihtne vestlus kliendiga kus küsitakse kliendi nime ning joogi eelistusi if/else stringiga.

"""
print("Welcome to the kitchen.")
# Küsi kasutajalt nimi ja salvesta see muutujasse
name = input("What is your name? ")
# Tervita kasutajat: Hi there, [nimi]!.
print(f"Hi there, {name}!")
# Küsi kasutajalt, mida ta juua soovib. Salvesta see muutujasse
drink = input("What would you like to drink?")
# Kui kasutaja vastas tea, kuvab programm ekraanile Have a nice tea!
if drink == "tea":
    print("Have a nice tea!")
# Kui kasutaja vastas coffee, kuvab programm ekraanile Feeling tired?
elif drink == "coffee":
    print("Feeling tired?")
# Muul juhul kuvab programm ekraanile We only serve water.
else:
    print("We only serve water.")
