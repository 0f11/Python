"""
Hello.py.

is a script for calculating body mass index.
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
    print(f"{name}, welcome to {school}")

mass = float(input("Whats your weight(kg)?"))
height = float(input("Whats you height(m)?"))
bmi = mass / (height * height)
if bmi <= 18.49:
    print(f"{bmi},You are underweight!")
elif bmi >= 24.91:
    print(f"{bmi}, You are overweight!")
elif bmi > 18.5 or bmi < 24.9:
    print(f"{bmi},You are in ideal weight!")
