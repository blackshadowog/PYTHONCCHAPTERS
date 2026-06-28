class dudesinfo():

    language = "py"
    salary = " 250 million dollor "

    def getinfo(self):
        print(f"your language is {self.language} and salary is {self.salary}")

abhishek = dudesinfo()
abhishek.language= "java"

# print(abhishek.language , abhishek.salary)
# dudesinfo.getinfo(abhishek)
abhishek.getinfo()