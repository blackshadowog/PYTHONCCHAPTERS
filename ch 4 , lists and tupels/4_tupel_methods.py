# Creating a tuple
t = (1, 2, 3, 4, 3, 5)

# Counting occurrences
print(t.count(3))  # Output: 2

# Finding index
print(t.index(4))  # Output: 3

# Tuple concatenation
t2 = (6, 7)
print(t + t2)  # Output: (1, 2, 3, 4, 3, 5, 6, 7)

# Repetition
print(t * 2)  # Output: (1, 2, 3, 4, 3, 5, 1, 2, 3, 4, 3, 5)

# Checking membership
print(3 in t)  # Output: True

# Getting length
print(len(t))  # Output: 6
 

# to convert tupel int  a list 
t = (1, 2, 3)
t_list = list(t)  # Convert to list
t_list.append(4)  # Modify the list
t = tuple(t_list)  # Convert back to tuple
print(t)  # Output: (1, 2, 3, 4)
