#Auto mantošana
class Vehicle:
    total=0
    def __init__(self, make, model, year, price): 
        self.make=make
        self.model=model
        self.year=year
        self.price=price

    def display_info(self):
        print (f"Auto nosaukums: {self.make}, Modelis: {self.model}, Gads: {self.year}, Cena: {self.price} euro")

    def total_vehicles(self):
        Vehicle.total+=self.price
        print(f"Auto cena ir {Vehicle.total}")
        return Vehicle.total

class Car(Vehicle):
    def __init__(self, make, model, year, price,num_doors, body_style):
        super().__init__(make, model, year, price)
        self.num_doors = num_doors
        self.body_style = body_style

        print (f" {self.num_doors}, {self.body_style}")

class Truck(Vehicle):
    def __init__(self, make, model, year, price, bed_length, towing_capacity):
        super().__init__(make, model, year, price)
        self.bed_length = bed_length
        self.towing_capacity = towing_capacity

        print (f" {self.bed_length}, {self.towing_capacity}")

auto= Vehicle("Volva", "XC-90", 2006, 6000)
auto.display_info()
auto.total_vehicles()

car = Car('Toyota', 'Camry', 2022, 29000, 4, 'sedan')
car.display_info()      
car.total_vehicles()

truck= Truck('Audi', 'a3', 2018, 10000, 3, 20 )
truck.display_info()
truck.total_vehicles()

