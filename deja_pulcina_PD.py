import itertools
from datetime import time
class Klients:
    Klienta_vaards = " "
    Klienta_uzvaards = " "
    Klienta_vecums = " "
    Klienta_PK = " "
    Klienta_adrese = " "
    id_iter = itertools.count()

    def init(self, vaards, uzvaards, vecums, personalais_kods, adrese ):
        self.Klienta_id = next(self.id_iter)
        self.Klienta_vaards = vaards
        self.Klienta_uzvaards = uzvaards
        self.Klienta_vecums = vecums
        self.Klienta_PK = personalais_kods
        self.Klienta_adrese = adrese

    def Klienta_info(self):
        return[
            self.Klienta_vaards, self.Klienta_uzvaards,self.Klienta_vecums, self.Klienta_PK, self.Klienta_adrese
        ]
 
    def Klienta_info_print(self):
        print("Bērna vārds: " + str(self.Klienta_vaards))
        print("Bērna uzvārds: " + str(self.Klienta_uzvaards))
        print("Bērna vecums: " + str(self.Klienta_vecums))
        print("Bērna personalais kods: " + str(self.Klienta_PK))
        print("Bērna adrese: " + str(self.Klienta_adrese))

class Vecaaks(Klients):
    def init(self, vaards, uzvaards, vecums, personalais_kods, adrese, tel_number ):
        self.Klienta_id = next(self.id_iter)
        self.Klienta_vaards = vaards
        self.Klienta_uzvaards = uzvaards
        self.Klienta_vecums = vecums
        self.Klienta_PK = personalais_kods
        self.Klienta_adrese = adrese
        self.tel_number = tel_number
 

k1 = Klients("Alina", "ikova", "3", 120621-25415, "Rezeke, Pils iela 1"  )
print(k1.Klienta_id)
k1.Klienta_info()
k1.Klienta_info_print()  