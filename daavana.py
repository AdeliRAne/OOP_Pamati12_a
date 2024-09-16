class daavana:
    def set(self,name,cena):
        self.name=name
        self.cena=cena
    def output(self):
        print (f"Dāvana nosaukums: {self.name}, Cena: {self.cena}")

p=daavana()
p.set("Grāmata", 15)
p.output()