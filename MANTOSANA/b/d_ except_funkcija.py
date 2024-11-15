# Funkcija, kas pieprasa divu sk ievadi un veic to dalīšanu
"""
def divide_numbers():
    try:
        num1 = float(input("Ievadier pirmo sk: "))
        num2 = float(input("Ievadier otro sk: "))
        result = num1 / num2
        print(f"Rezultāt: {result}")
    except ZeroDivisionError:
        print("Kļūda: Dalīšana ar nulli nav atļauta.")
    except ValueError:
        print("Kļūda: Ievadiet derīgus sk.")
    except Exception as e: #непредвиденная ошибка, которую мы не учли
        print(f"Radās neparedzēta kļūda: {e}")
    finally:
        #Šis bloks vienmēr izpildās, neatkarīgi no kļūdām
        print("Darbība pabeigta.")

divide_numbers()

#Funkcja, kas mēģina atvērt un nolasīt failu 
def read_file():
    try:
        filename = input("Ievadiet faila nosaukumu: ")
        with open (filename, 'r') as file:
            #Ja fails tiek veiksmīgi atvērts, izdr ukājam tā saturu
            content = file.read()
            print("Faila saturs: ")
            print(content)
    except FileNotFoundError:
        #Ja fails netiek atrasts
        print(f"Kļūda: Fails '{filename}' netika atrasts.")
    except PermissionError:
        #a nav piekļuves tiesību failam
        print(f"Kļūda: Nav piekļuves tiesību failam '{filename}'.")
    except Exception as e:
        #Ja rodas cita veida kļūda
        print(f"Radās kļūda: {e}")
    finally:
        print("Faila apstrāde pabeigta.")

read_file()

#Calculator klases defiņicija
class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def sum1(self):
#       print(f"{self.num1 + self.num2}")
        return self.num1 + self.num2
    
    def atniemsana(self):
        return self.num1 - self.num2
    
    def reizinasana(self):
        return self.num1 * self.num2
    
    def dalisana(self):
        try:
            result = self.num1 / self.num2
            return result
        except ZeroDivisionError:
            print("Kļūda: Dalīšana ar nulli nav atļauta.")
        except Exception as e:
        #Ja rodas cita veida kļūda
            print(f"Radās kļūda: {e}")
        finally:
            print("Darbība pabeigta.")            

p1=Calculator(2, 0)
print(p1.sum1())
print(p1.atniemsana())
print(p1.reizinasana())
print(p1.dalisana())
"""