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
kehamassiindeks = mass / (height * height)
if kehamassiindeks <= 18.49:
    print(f"{kehamassiindeks},underweight!")
elif kehamassiindeks >= 24.91:
    print(f"{kehamassiindeks}, overweight!")
elif kehamassiindeks > 18.5:
    print(f"{kehamassiindeks},ideal weight!")
