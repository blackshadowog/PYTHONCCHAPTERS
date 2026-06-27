'''
   Method                  	Description	                                           Example	                  Output
add(element)	            Adds an element to the set	                           s.add(6)	                  {1, 2, 3, 4, 5, 6}
update(iterable)	        Adds multiple elements from an iterable	               s.update([7, 8])	          {1, 2, 3, 4, 5, 7, 8}
remove(element)	            Removes an element (raises error if not found)	       s.remove(3)	              {1, 2, 4, 5}
discard(element)	        Removes an element (no error if not found)	           s.discard(10)	          {1, 2, 4, 5}
pop()	                    Removes a random element	                           s.pop()	                  {2, 4, 5}
clear()	                    Removes all elements	                               s.clear()	                  {}

'''
s = {1, 2, 3, 4, 5}

s.add(6)   # Adds 6
print(s)
s.update([7, 8])  # Adds multiple elements
print(s)

s.remove(3)  # Removes 3 (Error if not found)
print(s)
s.discard(10)  # No error if 10 is not in the set
print(s)

print(s.pop())  # Removes a random element
print(s)
s.clear()  # Clears the set

print(s)  # Output: set()
