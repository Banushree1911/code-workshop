def contains_uppercase(s):
    return any(char.isupper() for char in s)

s = "Hello World"
print("Does the string contain uppercase letters?", contains_uppercase(s))
