class Animal:
    legs = 4
    tail = 1

    def voice(self):
        print('Kaut-kāda skaņa')

class Dog(Animal):
    def voice_dog(self):
        print('Woof')
        
class Cat(Animal):
    def voice_cat(self):
        print('Meow')

anim=Animal()
anim.voice()
dog1, dog2 = Dog(),Dog()
cat1, cat2 = Cat(), Cat()

farm_band=[cat1, cat2, dog1, dog2]
for i in farm_band:
    if isinstance(i, Cat):
        i.voice_cat()
    if isinstance(i, Dog):
        i.voice_dog()

#dog1.voice_dog()
#dog2.voice_dog()
#cat1.voice_cat()
#cat2.voice_cat()

