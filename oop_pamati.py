class person:
    def set(self, name,age):
        self.name=name
        self.age=age
    def output(self):
        print(self.name,self.age)

p=person()
p.set("Peter", 20)
p.output()