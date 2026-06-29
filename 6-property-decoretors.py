class p():
    a = 1
    @classmethod
    def empole(cls):
        print(f"the the value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname}, {self.lname}"
    @name.setter
    def name(self,value):
         self.fname = value.split(" ")[0]
         self.lname = value.split(" ")[1]
        
    
a = p()
a.a = 45
a.name = "abhishek tiwari"
print(a.fname , a.lname)

a.empole()