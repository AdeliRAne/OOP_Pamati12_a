"""
with open("data.txt", "r", encoding="utf-8") as file:
    saturs = file.read()
print(saturs)

#Atver failu un nolasiet to pa rindiņām
with open("data.txt", "r", encoding="utf-8") as file:
    rindas = file.readlines()
print(rindas) 
for rinda in rindas:
    print(rinda.strip()) #Izvada katru rindiņu, noņemot liekās atstarpes

with open("data.txt", "r", encoding="utf-8") as file:
    for rinda in file:
        print(rinda.strip())
#-----------------------------------------------------------------------------------
#UZD - Cik vārdus teikuma
with open("teksts.txt", "r", encoding="utf-8") as file:
    saturs = file.read()
vaardi = saturs.split()
un_vaardi = len(set(vaardi))
print(vaardi)
print(len(vaardi))
print("Unikālo vārdu skaits: ", un_vaardi)"""
#-----------------------------------------------------------------------------------
#UZD - Rindu numerācija un izvade
#enumerate()
with open("data.txt", "r", encoding="utf-8") as file:
    rindas = file.readlines()
for index, rinda in enumerate(rindas, start=1):
    if rinda.strip():
        print(f"{index}: {rinda.strip()}")