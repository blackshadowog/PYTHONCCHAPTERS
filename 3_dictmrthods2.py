d = {"name": "John", "age": 25, "city": "New York"}

print(d.pop("age"))  # 25 (removes 'age' key)
print(d)  # {'name': 'John', 'city': 'New York'}

print(d.popitem())  # ('city', 'New York') (removes last item)
print(d)  # {'name': 'John'}

del d["name"]  # Deletes 'name' key
print(d)  # {}

d.clear()  # Removes all elements
print(d)  # {}
