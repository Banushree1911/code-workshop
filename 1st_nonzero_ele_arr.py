def first_non_zero(arr):
    for x in arr:
        if x != 0:
            return x
    return None  
array = [0, 0, 0, 3, 5, 0, 7]
result = first_non_zero(array)
print("First non-zero element:", result)
