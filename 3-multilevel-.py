class Employee:
    a = 1   # Attribute 'a'

class Programmer(Employee):
    b = 2   # Attribute 'b' comes in addition to 'a'

class Manager(Programmer):
    c = 3   # Attribute 'c' comes in addition to 'a' and 'b'


# Creating an Employee object
o = Employee()
print(o.a)   # Works → 'a' is in Employee
# print(o.b)  # ❌ Would cause error → Employee has no 'b'

# Creating a Programmer object
o = Programmer()
print(o.a, o.b)  # Works → Programmer inherits 'a' from Employee and has its own 'b'

# Creating a Manager object
o = Manager()
print(o.a, o.b, o.c)  # Works → Manager inherits 'a' from Employee, 'b' from Programmer, and has its own 'c'
