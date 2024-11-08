import json

organizations=[]
def load_data():
    file=open('organizations.json', 'r')
    data=json.load(file)
    file.close()
    global organizations
    print('DATI PIEVIENOTI')
def add_organization():
    organization_name =input('Organizācijas nosaukums: ')
    organization_adress =input('Organizācijas adresse: ')
    organization_id =input('Organizācijas id: ')

    organization={
        'name': organization_name,
        'adress' : organization_adress,
        'id': organization_id,
        'contacts':[]
    }

    while (True):
        response=input("Vai vēlies pievienot kontaktu? (jā/nē)")
        if response=='jā':
            print("Darbinirka informācija:")
            contact_name=input('Ievadiet Darbinieka vārdu: ')
            contact_position = input('Darbinieka adresse: ')
            contact_id=input('Darbinieka id:') 
            contact = {
                'name': contact_name,
                'position': contact_position,
                'id': contact_id
            } 
            organization['contacts'].append(contact)
        elif response=='nē':
                break
    organizations.append(organization)   

def print_organization():
    for organization in organizations:
        print('---ORGANIZATION---')
        print(f"{organization['name']} ({organization['id']})")
        print(f"Adrese:{organization['adress']}")
        print(f"Kontaktu skaits: {len(organization['contacts'])}")
def save_data():
    data = {'organizations': organizations}
    print('SAGLĀBA DATUS.....')
    file = open('organizations.json', 'w')
    json.dump(data, file, indent=4)
    print("DATI SAGLĀBATI")
def find_organization_by_id():
    organization_id=input('Ievadiet organizācijas ID: ')
    for organization in organizations:
        if organization['id']==organization_id:
            print('---ORGANIZĀCIJA---')
            print(f"{organization['name']}({organization['id']})")
            break
def main():
    load_data()
    find_organization_by_id()    
    while(True):
        response=input('(1) - Pievieno organizāciju // (2) - Izvada organzāciju // (3) - Beigt:   ')
        if response =='1':
            add_organization()
        elif response =='2':
            print_organization()
        elif response=='3':
            save_data()
            print('Paldies, par darbu!')
            exit()
        else:
            print("Izvele skaitļu 1, 2 vai 3")
            continue
main()
  