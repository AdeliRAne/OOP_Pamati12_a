class Shape:
    def __init__(self, a, b):
        self.pirmamala= a
        self.otramala = b
    
    def laukums(self):
        pass

    def perimetrs(self):
        pass

class Rectangle(Shape):
    def __init__(self, a, b):
        self.pirmamala = a
        self.otramala = b

        print('Tainstūris laukums un perimetrs')
    def laukums(self):

        return self.pirmamala * self.otramala **2
    
    def perimetrs(self):
        return self.pirmamala * self.otramala / 2
    
class Circle(Shape):
    def __init__(self, r):
        self.radiuss = r

    def laukums(self):
        print('Riņķa laukums un perimetrs')
        return 4 * 3.14 * self.radiuss **2
    
    def perimetrs(self):
        return 2 * 3.14 *self.radiuss

sk1 = Rectangle(12, 16)
#print(sk1.laukums())
#print(sk1.perimetrs())

sk2 = Circle(3)
#print(sk2.laukums())
#print(sk2.perimetrs())

figur=[sk1, sk2, Circle(5)]
for i in figur:
    print(f'Figūras laukums: {i.laukums()} un perimetrs {i.perimetrs()}')