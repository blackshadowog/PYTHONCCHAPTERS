class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        super().greet()  # Call the parent version first
        print("Hello from Child!")

# Create a Child object
c = Child()
c.greet()
