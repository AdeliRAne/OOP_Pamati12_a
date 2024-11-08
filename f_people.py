import json

with open ('f_people.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

print("Cilvēki vecāki par 18 gadiem")
for person in data:
    if person["age"] > 18:
        print(person["name"])

new_person = {"name":"Laura", "age":13, "city": "Rēzekne"} #jaunas data pierakstīšana
data.append(new_person)
with open ('people.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(data)