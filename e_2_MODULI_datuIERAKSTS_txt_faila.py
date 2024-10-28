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
print("Unikālo vārdu skaits: ", un_vaardi)
#-----------------------------------------------------------------------------------
#UZD - Rindu numerācija un izvade
#enumerate()
with open("data.txt", "r", encoding="utf-8") as file:
    rindas = file.readlines()
for index, rinda in enumerate(rindas, start=1):
    if rinda.strip():
        print(f"{index}: {rinda.strip()}")
#-----------------------------------------------------------------------------------
#UZD -  Vārdi kā sakas k
noraditais_burts = "k"
with open("teksts.txt", "r", encoding="utf-8") as file:
    saturs = file.read()
    saturs = saturs.lower() #Teksts ar maziem burtiem
    vardi = saturs.split() #Sadalām tekstu vārdos
vardi_ar_k = []
for vards in vardi:
    #Pārbaudām, vai pirmais burts ir norādītais burts
    if len(vards) > 0 and vards[0] == noraditais_burts:
        vardi_ar_k.append(vards)

#Izvadām rezultātu
print(f"Vārdi, kas sākas ar burtu '{noraditais_burts}':")
for vards in vardi_ar_k:
    print(vards)"""

#Mans VARIANTS
with open("teksts.txt", "r", encoding="utf-8") as file: 
    words = file.readline().split()
    for word in words:
        if "m" in word[0]:
            print(word)

#-----------------------------------------------------------------------------------