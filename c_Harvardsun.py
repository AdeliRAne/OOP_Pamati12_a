#Сам вводишь данные и они выводятся
#Or. Ob. Pr.
"""
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ") #kā mainīgais
def get_house():
    return input("House: ")

if __name__ == "__main__":
    main() 

#-----------------------------------------------
#2. variants
def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main() 

#-----------------------------------------------
#Iepakojot šo kortežu tā, lai mēs varētu atgriezt 
#abus vienumus mainīgajam ar nosaukumu student, mēs varam modificēt savu kodu šādi.
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main() 

#-----------------------------------------------
#4.variants - list
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]


if __name__ == "__main__":
    main() 
#-----------------------------------------------
#Šajā īstenošanā var izmantot arī vārdnīcu. 
#Atcerieties, ka vārdnīcas nodrošina atslēgu un vērtību pāri.
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main() 
#-----------------------------------------------
#Tomēr mūsu kodu var vēl vairāk uzlabot. 
#Ievērojiet, ka ir nevajadzīgs mainīgais. Mēs varam noņemt student = {}, 
#jo mums nav jāizveido tukša vārdnīca.
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main() 
#-----------------------------------------------
#Mēs varam nodrošināt savu īpašo gadījumu ar Padma mūsu koda vārdnīcas versijā.
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main() """
#-----------------------------------------------
class Student:
    ...
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main() 