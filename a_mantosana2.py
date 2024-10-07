#Mantošana 17.09
class Geom:
    name="Geom"
#    print(f'{name}')

    def set_coords(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def draw(self):
        print('Ģeom.fig. zīmēšana')

class Line(Geom):
    name='Line' #имя класса
    def draw(self):
        print('Līnijas zīmēšana')

class Rect(Geom):
#    def draw(self):
#        print('Tainsnstūra zīmēšana')
    pass

g=Geom()
l=Line()
r=Rect()
l.set_coords(1,1,2,2)
r.set_coords(1,1,2,2,)
l.draw()
print(l.name)
r.draw()
print(r.name)
print(l.__dict__) #конкретно какие координаты
print(r.__dict__)
g.set_coords(0,0,0,0)
print(g.__dict__)
