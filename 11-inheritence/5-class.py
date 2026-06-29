class p():
    a = 1
    @classmethod
    def value(cls):
        print(f"the the value of a is {cls.a}")

a = p()
a.a = 45
a.value()
