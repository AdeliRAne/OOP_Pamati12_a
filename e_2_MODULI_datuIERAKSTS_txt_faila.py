with open("data.txt", "r", encoding="utf-8") as file:
    saturs = file.read()
print(saturs)

#Atver failu un nolasiet to pa rindiņām
with open("data.txt", "r", encoding="utf-8") as file:
    rindas = file.readlines()
print(rindas) 
for rinda in rindas:
    print(rinda.strip()) #Izvada katru rindiņu, noņemot liekās atstarpes