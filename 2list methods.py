# Creating a list
lst = [1, 2, 3]

# Adding elements
lst.append(4)  # [1, 2, 3, 4] 

print(lst)

lst.insert(1, 10)  # [1, 10, 2, 3, 4]

print(lst)

lst.extend([5, 6])  # [1, 10, 2, 3, 4, 5, 6]

print(lst)

# Removing elements
lst.remove(10)  # [1, 2, 3, 4, 5, 6]
print(lst)

lst.pop(2)  # Removes index 2 -> [1, 2, 4, 5, 6]
print(lst)

lst.clear()  # []
print(lst)

# Sorting and reversing

lst = [3, 1, 4, 2]
print(lst)
lst.sort()  # [1, 2, 3, 4]
print(lst)
print(sorted(lst))

lst.reverse()  # [4, 3, 2, 1]

print(lst)
