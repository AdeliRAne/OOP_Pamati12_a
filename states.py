import json
with open('states.json') as f:
    data=json.load(f)

for state in data['states']:
    print(state)
for state in data['states']:
    print(state["name"], state["abbreviation"])
   
with open("states.json", "r", encoding="utf-8") as file: 
    words = file.readline().split()
    for word in words:
        if "a" in word[0]:
            print(word)

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=4)