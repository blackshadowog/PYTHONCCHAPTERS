a = {
    "rohan": 54 ,
    "ram"  : 56,
    "abhi" :60  
    }
 
print(type(a))

print(a["rohan"])

print(a.items())

print(a.keys())

print(a.values())

a.update({"ram" : 100, "renuka" : 99})

print(a)

print(a.get("renuka"))

print(a["renuka"])
