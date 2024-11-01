import json
with open ('f_skoleni.json', 'r', encoding="utf-8") as file:
    skoleni = json.load(file)
    print(skoleni)

print("Cilvēks, kuram vērtējums ir vairāk par 4 un mazāk par 7: ")
for vairak in skoleni:
    if vairak["vertejums"] > 4 and vairak["vertejums"] < 7:
        print(vairak["vards"])