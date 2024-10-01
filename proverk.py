import itertools
from datetime import time

class Klients:
    id_iter = itertools.count()
    
    def __init__(self, vaards, uzvaards, vecums, personalais_kods, adrese, cena_za_zanyatie, dni_nedeli, vremya_zanyatiya):
        self.Klienta_id = next(self.id_iter)
        self.Klienta_vaards = vaards
        self.Klienta_uzvaards = uzvaards
        self.Klienta_vecums = vecums
        self.Klienta_PK = personalais_kods
        self.Klienta_adrese = adrese
        self.cena_za_zanyatie = cena_za_zanyatie
        self.dni_nedeli = dni_nedeli  # список дней посещений, например ['Pirmdiena', 'Trešdiena', 'Piektdiena']
        self.vremya_zanyatiya = vremya_zanyatiya  # время начала занятия, объект типа datetime.time

    def Klienta_info(self):
        return [
            self.Klienta_vaards, self.Klienta_uzvaards, self.Klienta_vecums, self.Klienta_PK, self.Klienta_adrese
        ]
 
    def Klienta_info_print(self):
        print("Bērna vārds: " + str(self.Klienta_vaards))
        print("Bērna uzvārds: " + str(self.Klienta_uzvaards))
        print("Bērna vecums: " + str(self.Klienta_vecums))
        print("Bērna personalais kods: " + str(self.Klienta_PK))
        print("Adrese: " + str(self.Klienta_adrese))
        print("Cena par vienu nodarbību: " + str(self.cena_za_zanyatie) + " EUR")
        print("Dienas, kad apmeklē nodarbības: " + ", ".join(self.dni_nedeli))
        print("Nodarbību sākuma laiks: " + self.vremya_zanyatiya.strftime('%H:%M'))

    # Метод для расчета общей стоимости занятий за месяц
    def cena_za_menesi(self):
        nodarbibas_nedela = len(self.dni_nedeli)  # Количество занятий в неделю
        nodarbibas_menesi = nodarbibas_nedela * 4  # Примерно 4 недели в месяце
        total_price = nodarbibas_menesi * self.cena_za_zanyatie
        return total_price

    # Метод для вывода стоимости занятий за месяц
    def cena_za_menesi_print(self):
        total_price = self.cena_za_menesi()
        print(f"Kopējā maksa par nodarbībām mēnesī: {total_price} EUR")

class Vecaaks(Klients):
    def __init__(self, vaards, uzvaards, vecums, personalais_kods, adrese, tel_number, cena_za_zanyatie, dni_nedeli, vremya_zanyatiya):
        super().__init__(vaards, uzvaards, vecums, personalais_kods, adrese, cena_za_zanyatie, dni_nedeli, vremya_zanyatiya)
        self.tel_number = tel_number

    def Vecaaks_info_print(self):
        print("Vecāka vārds: " + str(self.Klienta_vaards))
        print("Vecāka uzvārds: " + str(self.Klienta_uzvaards))
        print("Vecāka telefona numurs: " + str(self.tel_number))
        self.Klienta_info_print()

# Создание клиента (ребёнок)
k1 = Klients("Alina", "Ikova", "3", "120621-25415", "Rezekne, Pils iela 1", 
             10,  # цена за одно занятие
             ['Pirmdiena', 'Trešdiena', 'Piektdiena'],  # дни занятий
             time(10, 30))  # время занятий (10:30)

print(f"Klienta ID: {k1.Klienta_id}")
k1.Klienta_info_print()
k1.cena_za_menesi_print()

# Создание родителя (Vecaaks)
v1 = Vecaaks("Jānis", "Ikovs", "35", "120681-25416", "Rezekne, Pils iela 1", 
             "+371 12345678", 10, ['Pirmdiena', 'Trešdiena', 'Piektdiena'], time(10, 30))
