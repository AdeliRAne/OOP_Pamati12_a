class person:
    def set(self, name,age):
        self.name=name
        self.age=age
    def output(self):
        print(self.name,self.age)
    def labdien(self):
        print (f"Labdien, {self.name}!")

p=person()
sk=int(input("Ievadiet cilvēku skaits: "))
for i in range(sk):
    name=input("Ievadiet vārdu: ")
    age=input("Ievadiet vecumu: ")
    person.set(p,name,age)
    person.output(p)

p=person()
p.set("Lina", 19)
p.output()
p.labdien()

d=person()
d.set("Alesja", 18)
d.output()


