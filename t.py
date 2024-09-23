#polimorfisms metode
class Animal:
    legs = 4
    tail = 1

    def voice(self):
        print('Kaut-kāda skaņa')

class Dog(Animal):
    def voice(self):
        print('Woof')
        
class Cat(Animal):
    def voice(self):
        print('Meow')

anim=Animal()
anim.voice()
dog1, dog2 = Dog(),Dog()
cat1, cat2 = Cat(), Cat()

farm_band=[cat1, cat2, dog1, dog2]
for i in farm_band:
    i.voice()