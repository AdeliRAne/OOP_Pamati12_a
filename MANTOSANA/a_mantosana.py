class Person:
    def __init__(self, name, age): 
        self.name=name
        self.age=age
        print("Person created")
    
    def say_hallo(self):
        print(f'{self.name} says Hello!')

class Student(Person):
    def __init__(self, name, age, average_grade):
        #Person.__init__(self,name,age)
        super().__init__(name,age)
        self.average_grade=average_grade
        print("Student created")
    def study(self):
        print(f"{ self.name} studies")
    def say_hello(self):
        print(f"Student with name: {self.name} says Hello!")

class Teacher(Person):
    def teacher(self):
        print(f"{ self.name}  teachers")

    def introduce(person):
        print("Now, a peron will say hello")
        person.say_hello()

people_arr=[Student("Tom", 15, 4.5), Teacher("Lina", 30), Student('Bob', 36, 4.7)]

for person in people_arr:
    introduce(person)

p1=Student("Tom", 16)
t1=Teacher("Alina", 31)
p1.study()
t1.teacher()
p1.say_hallo()
t1.say_hallo()