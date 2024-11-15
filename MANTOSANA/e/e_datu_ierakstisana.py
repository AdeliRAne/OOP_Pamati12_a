#'w'- rakstīšanas režīms
#'a' - pievieno
#'x' - eksluzīvā 
#-------------------------------------------------------------------------
# UZD
"""
a=input("Ievadiet jūsu vārdu: ")
with open("tek.txt", "w", encoding="utf-8") as faila_objekts:
    for ieraksts in a:
        faila_objekts.write(ieraksts)
#-------------------------------------------------------------------------
# UZD
edieni = ["Pankukas", "Makaroni", "Salad"]
with open("edieni.txt", "w", encoding="utf-8") as faila_objekts:
    for ediens in edieni:
        faila_objekts.write(ediens + '\n')"""
#-------------------------------------------------------------------------
#UZD
while True: 
      ievade = input('Ievadiet yes or no: ')
      if ievade =='yes':
        n = input("Ievadiet grānatas nosaukumu: ")
        a = input("Ievadiet autoru: ")
        gads = int(input("Ievadiet gadu: "))
        book_inf = (f'Nosaukums: {n}\n Autors: {a}\n Gads: {gads}')
      else:
            break 

with open("book.txt", "w", encoding="utf-8") as faila_objekts:
        for file in book_inf:
              faila_objekts.write(file)

print("\nInformācija par grāmatu: ")
with open("book.txt", "r", encoding="utf-8") as faila_objekts:
    for rinda in faila_objekts:
        print(rinda.strip())

