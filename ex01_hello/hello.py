"""
Hello.py. is a script for claclulating body mass index.
"""
name = input("Hello! What's your name?")

if name == "":
    print("Name was not inserted!")
else:
    print(f"Hello,{name}!")
school = input("Where do you study?")
if school == "":
    print("School was not entered!")
else:
    print(f"{name}, welcome to {school}!")

weight = float(input("Whats your weight?"))
height = float(input("Whats you height?"))
if height > 2.3:
    print("Please enter in meters!")
body_mass_index = weight / height * height
if body_mass_index < 18.5:
    print("You are underweight!")
elif body_mass_index > 18.5:
    print("You are in ideal weight!")
elif body_mass_index > 24.9:
    print("You are overweight!")

# 1. Programm küsib sisendit: (input)
# "What's your name?:" ja "Where do you study?:"
# Nimi ja kool on nõutud(Ei tohi o.lla tühjad).
# Kui nimi on puudu peab programm printima "Name was not inserted!",
# kui kooli nimi on puudu tuleb printida "School was not inserted!"
# Lõpus peaks programm printima "(Sisestatud nimi), welcome to (sisestatud kool)"
# 2. Arvuta kehamassi indeks kasutades sisendit (input).
# Üks sisend on mass(kg) teine sisend height(m). Lõpuks peab programm printima "(kehamassiindeks), (kehamassitüüp)" **kehamassitüüp printida väikeste tähtedega
