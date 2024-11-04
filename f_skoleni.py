import json
with open ('f_skoleni.json', 'r', encoding="utf-8") as file:
    skoleni = json.load(file)
    print(skoleni)

print("Cilvēks, kuram vērtējums ir vairāk par 4 un mazāk par 7: ")
for v in skoleni:
    if v["vertejums"] > 4 and v["vertejums"] < 7:
        print(v["vards"])