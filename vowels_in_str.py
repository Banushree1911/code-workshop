def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

input_string = "Hello World"
vowel_count = count_vowels(input_string)
print(f"The number of vowels in the string is: {vowel_count}")
