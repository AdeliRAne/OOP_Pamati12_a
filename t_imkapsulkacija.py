class Pupil:
#    _age=0 #protected
    __age=0 #private
#    age=0   #public
    name="Ali"
    def say(self):
        print(self.__age, self._age, self.age)

#setter piekļuve datiem
    def set_age(self, value: int):
        if value >=0:
            self.__age=value
        else:
            print('Vecums nevar būt negatīvs')

#getter metode, lai piekļūtu privātam mainīgajam
    def get_age(self):
        return self.__age
    
pupil=Pupil()
pupil.set_age(-1)
pupil.set_age(10)
print(pupil.get_age())

"""
pupil.age=-1 #сколько ему лет 
pupil._age=-2
pupil.__age=-3
print(pupil.age)
print(pupil._age)
print(pupil.__age)
#print(dir(pupil))
pupil.say()
"""