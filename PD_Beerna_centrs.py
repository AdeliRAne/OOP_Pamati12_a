import json
import datetime

organizations=[]
def load_data():
    file=open('bernacentrs.json', 'r')
    data=json.load(file)
    file.close()
    global organizations
    organizations=data['organizations']
    print('DATI PIEVIENOTI')

def add_organization():
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


def print_organization():
    for organization in organizations:
        print('APMEKLEĀJS: ')
        print(f"{organization['name']} ({organization['id']})")
        print(f"Tālrunis:{organization['phone']}")
        print(f"Pilsēta: {organization['city']}")
        print('-' * 100)
        print(f"{organization['name']} (ID:{organization['id']}, {organization['phone']}, {organization['city']} )")
        print(f"Kontaktu skaits: {len(organization['contacts'])}")
        print("Reģistrācijas datumsun laiks:")
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

def save_data():
    data = {'organizations': organizations}
    print('SAGLĀBA DATUS.....')
    file = open('bernacentrs.json', 'w')
    json.dump(data, file, indent=4)
    print("DATI SAGLĀBATI")

def find_organization_by_id():
    ap_id=input('Ievadiet apmeklētāju ID: ')
    for organization in organizations:
        if organization['id']==ap_id:
            print('---Apmeklētājs---')
            print(f"{organization['name']} (ID:{organization['id']}, {organization['phone']}, {organization['city']} )")
            break

def uudens_daudzums():
    uudens = float(input("Ievadiet dzeramo ūdeni daudzumu ( (1) - infotmācija par cenu ): "))
    if uudens == 1:
        print("1 dzeramo ūdens maksā 0,45 EUR ")
    else:
        cena = uudens * 0.45
        print('Jūsu cena ir: ')
        print(cena)

def cena():
    a = input('Vai vēlaties uzzināt par cenām un atlaidēm? y/n:')
    if a == 'y':
        print('Cena par nedeļu nodarbību ir 10 EUR')
        print('Bērnu centrā notiek akcija!')
        sk = input('Ievadiet nodarbību daudzums vai (info), lai uzzināt par akciju:')
        if sk == 'info':
            print("Bērnu centrā notiek akcija! Ja apmeklēja 100 stundas, tad katram nākamam apmeklējumam ir atlaide 5%, bet ja apmeklēja 200 stundas, tad skaitās VIP apmeklētājs 10%")
        elif sk == 100:
            print("Katram nākamam apmeklējumam ir atlaide 5%")
            print('Jūsu cena: 9.50 EUR')
        elif sk == 200:
            print("Apsveicam! Jūs esat VIP un katram nākamam apmeklējumam ir atlaide 10%")
            print('Jūsu cena: 9.00 EUR')   
        else:
            print("Bērnu centrā notiek akcija! Ja apmeklēja 100 stundas, tad katram nākamam apmeklējumam ir atlaide 5%, bet ja apmeklēja 200 stundas, tad skaitās VIP apmeklētājs 10%")
    else:
        print('-'*100)


def main():
    load_data()
    cena()
    while(True):
        response=input('(1) - Pievieno apmeklētāju  // (2) - Izprinte apmeklētāja datus  // (3) - Iziet //  (4) - Atrast kontaktu  ')
        if response =='1':
            add_organization()
            uudens_daudzums()             
        elif response =='2':
            print_organization()
        elif response=='3':
            save_data()
            print('Paldies, par darbu!')
            exit()
        elif response == '4' :
            find_organization_by_id()
        else:
            print("Izvele skaitļu 1, 2 vai 3")
            continue
main()
  