def first_non_repeated_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

string = "swiss"
result = first_non_repeated_char(string)
print("First non-repeated character:", result)
