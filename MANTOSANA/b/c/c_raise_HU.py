#Objektorientētā programma mudina jūs iekļaut visu klases funkcionalitāti klases definīcijā. Ko darīt, ja kaut kas noiet greizi? Ko darīt, ja kāds mēģina ierakstīt kaut ko nejauši? Ko darīt, ja kāds mēģina izveidot studentu bez vārda? Mainiet savu kodu šādi:
"""
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main() 
#-------------------------------------------------------------------------
#Tā nu ir gadījies, ka Python ļauj izveidot īpašu funkciju, ar kuras palīdzību var izdrukāt objekta atribūtus. Mainiet savu kodu šādi:

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main() 
#-------------------------------------------------------------------------
#Ņemiet vērā, ka def __str__(self) nodrošina līdzekli, kuru izsaucot tiek atgriezts students. Tāpēc tagad, kā programmētājs, varat izdrukāt objektu, tā atribūtus vai gandrīz visu, ko vēlaties, kas saistīts ar šo objektu.

#__str__ ir iebūvēta metode, kas nāk kopā ar Python klasēm. Tā nu sagadījies, ka varam izveidot savas metodes arī klasei! Mainiet savu kodu šādi:
class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return ""
            case "Otter":
                return ""
            case "Jack Russell terrier":
                return ""
            case _:
                return ""

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)

if __name__ == "__main__":
    main() 
#-------------------------------------------------------------------------
#Pirms turpināt, ļaujiet mums noņemt mūsu patrona kodu. Mainiet savu kodu šādi:3
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name= name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main() 
#-------------------------------------------------------------------------
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for house
    @property
    def house(self):
        return self._house

    # Setter for house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main() 
#-------------------------------------------------------------------------
#Papildus mājas nosaukumam mēs varam aizsargāt arī mūsu studenta vārdu. Mainiet savu kodu šādi:

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main() 
#-------------------------------------------------------------------------
#Šeit ir piemērs, kā neizmantot klases metodi. Termināļa logā ierakstiet  code 
#hat.py un kodējiet šādi:
import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry") 
#-------------------------------------------------------------------------
#Tomēr mēs varam vēlēties palaist kārtošanas funkciju, 
# neveidojot konkrētu kārtošanas cepures instanci 
# (galu galā ir taču tikai viena cepure!). Mēs varam modificēt savu kodu šādi:
import random
class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry") 
#-------------------------------------------------------------------------
#Mēs varam modificēt savu kodu šādi, 
#risinot dažas neizmantotās iespējas saistībā ar @classmethod:
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main() 
#-------------------------------------------------------------------------
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name  
    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
...""" 
#-------------------------------------------------------------------------

