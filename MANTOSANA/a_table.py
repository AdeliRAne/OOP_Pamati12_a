#Mantošana 23.09
class Table:
    def __init__(self, l, w, h):
        self.lenght=l
        self.width = w
        self.height = h

    def info(self):
        print (f"Lenght: {self.lenght}, Width: {self.width}, Height: {self.height} ")

class DeskTable(Table):
    def square(self):
        return self.width * self.lenght
    
class ComputerTable(DeskTable):
    def galds(self, dators):
        self.dators = dators
        return self.width * self.lenght - self.dators    

class KitchenTable(Table):
    def __init__(self, l, w, h, p):
#       Table.__init__(l, w, h)
        super(). __init__(l, w, h)
        self.places = p


#----------------------------------------------------------------
t1 = Table(1.5, 1.8, 0.75)
t1.info()
#-----------------------------------------------------------------
t2 = DeskTable(0.8, 0.6, 0.5)
print(t2. square())
t2.info()
#-----------------------------------------------------------------
t3 = ComputerTable(0.8, 0.6, 0.7)
print(t3. galds(0.3)) #обязательно сколько стол
#-----------------------------------------------------------------
t4 = KitchenTable(1.5, 2, 0.75, 6)