organizations=[]
organizations_a={
    'name':'Tesla Motors',
    'adress':'Tesla ave 1, USA',
    'id':'8646678',
    'contacts':[
        {
            'name':'Elon',
            'position':'CEO',
            'id':1
        },
        {
            'name':'Vlas',
            'position':'CTO',
            'id':2        
        }
    ]
}
organizations_b={
    'name':'Eesti posti',
    'adress':'Super street 2, Tartu',
    'id':'1295843',
    'contacts':[
        {
            'name':'Anna',
            'position':'CEO',
            'id':3
        },
        {
            'name':'Alina',
            'position':'CTO',
            'id':4        
        }
    ]
}
organizations.append(organizations_a)
organizations.append(organizations_b)
print(organizations)

for organization in organizations:
    print('---ORGANIZATION---')
    print(f"{organization['name']} ({organization['id']})")
    print(f"Adrese:{organization['adress']}")
    print(f"Kontaktu skaits: {len(organization['contacts'])}")