import json

organizations=[]
file=open('centrs.json', 'r')
data=json.load(file)
file.close()
organizations=data['organizations']
print('DATI PIEVIENOTI')
while(True):
    response=input('(1) - Pievieno apmeklētāju // (2) - Izprinte apmeklētāja datus // (3) - Iziet:   ')
    if response =='1':
        berna_name =input('Apmeklētāja vārds: ')
        berna_phone =input('Tālrunis: ')
        berna_city = input('Pilsēta: ')
        berna_id =input('Apmeklētāja id: ')

        organization={
            'name': berna_name,
            'phone' : berna_phone,
            'city' : berna_city,
            'id': berna_id,
            'contacts':[]
        }
        while (True):
            response=input("Vai vēlaties pieteikties apmeklejumam? (y/n)")
            if response=='y':
              print("Nodarbība pieteikšana: ")
              nod_time=input('Cik ilgs apmeklējums: ')
              ber_daudzums = input('Bērnu daudzums: ')
              apmeklejuma_id=input('Apmeklējuma id:') 
              contact = {
                  'time': nod_time,
                  'daudzums': ber_daudzums,
                  'id': apmeklejuma_id
              } 
              organization['contacts'].append(contact)
            elif response=='n':
                break
        organizations.append(organization)
    
    elif response =='2':
        for organization in organizations:
            print('---ORGANIZATION---')
            print(f"{organization['name']} ({organization['id']})")
            print(f"Tālrunis:{organization['phone']}")
            print(f"Pilsēta: {organization}")
            print(f"Kontaktu skaits: {len(organization['contacts'])}")
    elif response=='3':
        data = {
            'organizations': organizations
        }
        print('SAGLĀBA DATUS.....')
        file = open('centrs.json', 'w')
        json.dump(data, file, indent=4)
        print('Paldies, par darbu!')
        exit()
    else:
        print("Izvele skaitļu 1, 2 vai 3")
        continue