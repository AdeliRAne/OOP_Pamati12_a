class Person:
    def __init__(self, vaards, vecums):
        self.vaards = vaards
        self.vecums = vecums
    
    def person_info(self):
        print (f"Vārds: {self.vaards}; Vecums: {self.vecums} gadi")

    def apsveikt(self):
        print(f'Apsveikam {self.vaards}!')

class Skolens(Person):
    def __init__(self, vaards, vecums, klase):
        super().__init__(vaards, vecums)
        self.klase = klase

    def person_info(self):
        print (f"Vārds: {self.vaards}; Vecums: {self.vecums} gadi; Klase: {self.klase}")

class Skolotajs(Person):
    def __init__(self, vaards, vecums, uzvaards):
        super().__init__(vaards, vecums)
        self.uzvaards = uzvaards

    def person_info(self):
        print (f"Vārds un uzvārds: {self.vaards} {self.uzvaards}; Vecums: {self.vecums} gadi")
       

p1=Person('Lina', 19)
p1.person_info()
p1.apsveikt()

p2=Skolens('Artjom', 13, '7.b')
p2.person_info()

p3=Skolotajs("Elena", 45, "Bērzova")
p3.person_info()