A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))   # Union: {1, 2, 3, 4, 5, 6}
print(A & B)   # Intersection: {3, 4}
print(A - B)   # Difference: {1, 2}
print(A ^ B)   # Symmetric Difference: {1, 2, 5, 6}
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))  # True (A is inside B)
print(B.issuperset(A))  # True (B contains A)


# A frozenset is an immutable version of a set.
frozen = frozenset([1, 2, 3, 4])
print(frozen)  # Output: frozenset({1, 2, 3, 4})

# Cannot modify a frozenset
frozen.add(5)  # ❌ Error!
