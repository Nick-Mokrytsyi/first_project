class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def display_info(self):
        print("Name:", self.__name, "\nAge: ", self.__age)


class Employer(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def display_info(self):
        super().display_info()
        print("Company:", self.company)


class Student(Person):
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    def display_info(self):
        print("Student:", self.name, "\nUniversity:", self.university)


people = [Person("tom", 23), Student("Bob", 19, "KPI")]
for person in people:
    person.display_info()
    print()
