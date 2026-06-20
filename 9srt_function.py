name = "abhishek"

print(len(name))
print(name.endswith("shek"))
print(name.startswith("abhi"))
print(name.capitalize())
print(name.count("h"))


s = "    Hello,            World!    "
print(s.upper())      # Convert to uppercase
print(s.lower())      # Convert to lowercase
print(s.strip())      # Remove leading and trailing spaces
print(s.replace("World", "Python"))  # Replace substring
print(s.split(","))   # Split string into list
print(s.find("World"))