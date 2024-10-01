import itertools
from datetime import time

class Klients:
    id_iter = itertools.count(1) #Айди будет с начинатся с 1
    
    def __init__(self, vaards, uzvaards, vecums, personalais_kods, adrese, cena_par_men, dienas, nodarbiiba_laiks):
        self.Klienta_id = next(self.id_iter)
        self.Klienta_vaards = vaards
        self.Klienta_uzvaards = uzvaards
        self.Klienta_vecums = vecums
        self.Klienta_PK = personalais_kods
        self.Klienta_adrese = adrese
        self.cena_par_men = cena_par_men
        self.dienas = dienas
        self.nodarbiiba_laiks = nodarbiiba_laiks


    def Klienta_info(self):
        return [
            self.Klienta_vaards, self.Klienta_uzvaards, self.Klienta_vecums, self.Klienta_PK, self.Klienta_adrese
        ]
 
    def Klienta_info_print(self):
        print("Bērna vārds un uzvārds: " + str(self.Klienta_vaards), (self.Klienta_uzvaards))
        print("Bērna vecums: " + str(self.Klienta_vecums))
        print("Bērna personalais kods: " + str(self.Klienta_PK))
        print("Adrese: " + str(self.Klienta_adrese))
        print("-" * 100)

    def nodarbiiba_laiks_info(self, cena_par_men, diena, nodarbiiba_laiks):
        print(f"Cena par mēnesi: {self.cena_par_men} EUR")
        print("Dienas, kad notiek nodarbības: " + ", ".join(self.dienas))
        print(f"Nodarbību laiks: {self.nodarbiiba_laiks.strftime('%H:%M')}")
        print("-" * 100)

        
class Vecaaks:
    
    def __init__(self, vaards, uzvaards, tel_number):
        self.Vecaaka_vaards = vaards
        self.Vecaaka_uzvaards = uzvaards
        self.tel_number = tel_number

    def Vecaaks_info_print(self):
        print("Vecāka vārds un uzvārds: " + str(self.Vecaaka_vaards), str(self.Vecaaka_uzvaards))
        print("Vecāka telefona numurs: " + str(self.tel_number))
        print("-" * 100)
 

k1 = Klients("Alīna", "Suškova", "3", "120621-25415", "Rēzekne, Pils iela 1", 25, ["Pirmdiena", "Trešdiena", "Piektdiena", "Sestdiena"], time(16, 30))
print(f"Klienta ID: {k1.Klienta_id}")
k1.Klienta_info_print()
k1.nodarbiiba_laiks_info(25, ["Pirmdiena", "Trešdiena", "Piektdiena"], time(16, 30))

v1 = Vecaaks("Artemijs", "Suškovs", "+371 23345678")
v1.Vecaaks_info_print()
