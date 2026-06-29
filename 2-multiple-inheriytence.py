class Employee:
    company = "ITC"

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Coder:
    language = "Python"

    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


# Create objects
a = Employee()
a.name = "John"
a.salary = 50000

b = Programmer()
b.name = "Alice"
b.salary = 75000

# Method calls
b.show()
b.printLanguages()
b.showLanguage()
