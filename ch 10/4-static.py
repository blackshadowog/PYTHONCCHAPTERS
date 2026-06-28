class dudesinfo():

    language = "py"
    salary = " 250 million dollor "

    def getinfo(self):
        print(f"your language is {self.language} and salary is {self.salary}")
    @staticmethod
    def greet():
        print("good morning")

abhishek = dudesinfo()
abhishek.language= "java"

# print(abhishek.language , abhishek.salary)
abhishek.greet()
# dudesinfo.getinfo(abhishek)
abhishek.getinfo()