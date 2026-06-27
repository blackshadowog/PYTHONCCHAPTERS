# A set is an unordered collection of unique elements in Python.
# It does not allow duplicate values and is mutable (can be modified after creation).

'''Key Features of Sets:
Unordered → Elements have no fixed position.

Unique → No duplicate elements allowed.

Mutable → Can add/remove elements, but individual elements are immutable.

Uses {} curly brackets or the set() function.

'''

# Using curly brackets
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Using set() function
another_set = set([1, 2, 2, 3, 3,])  # Removes duplicates
print(another_set)  # Output: {1, 2, 3, 4}

s={1,2,3,3,3,3,3}
print(s)



# Creating an empty set
empty_set = set()  # {} creates an empty dictionary, not a set
print(type(empty_set))  # Output: <class 'set'>
