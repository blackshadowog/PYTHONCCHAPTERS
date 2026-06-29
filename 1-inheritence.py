# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):  # Overriding parent's method
        print(f"{self.name} barks.")

# Another child class
class Cat(Animal):
    def speak(self):  # Overriding parent's method
        print(f"{self.name} meows.")

# Using the classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()   # Buddy barks.
cat.speak()   # Whiskers meows.
