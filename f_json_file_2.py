import json
""""""
#Vairāk cilvēku ieraksts
try:
    with open ('user_data.json', 'r', encoding="utf-8") as file:
        data = json.load(file) 
except FileNotFoundError:
    data = []

while True:
    name = input("Ievadi vārdu: ")
    age = input("Ievadi vecums: ")
    city = input("Ievadi pilsētu: ") 
    
    data.append({
    "name": name,
    "age" : age,
    "city" : city
    })
    another = input("VAi vēlies pievienot vēl vienu cilvēku? (jā/nē)").strip().lower()
    if another !="jā": #"!=" неравно
        break

with open ('data.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4)
print("Dati ir veiksmīgi saglabāti JSON failā!")

 