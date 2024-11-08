#JSON - vārdnīca // Atkartošāna
import json
"""
data = {
    "name" : "Alina",
    "age" : "19",
    "city" : "Rēzekne",
}
with open ('data.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4) 

with open ('data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

print(data)
print("Vecums:", data["age"]) #Вывести в консоль конкретное значение из json failā
#indent=4 palīdz padarīt JSON failu lasāmāku (rasta ar atstarpēm)
#json.dump - palīdz ierakstīt datus failā
#json.load - nolasīs faila saturu un izvāda
#print(data) - izdrukās saturu konsolē 

#---------------------------------------------------------------------------------------

#Saraksta ierakstīšana
words = ['ābele', 'bumbieri']
with open ('words.json', 'w', encoding="utf-8") as file:
    json.dump(words, file, indent=4)
#---------------------------------------------------------------------------------------
"""

