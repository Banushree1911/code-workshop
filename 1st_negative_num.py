def find_first_negative(arr):
    for num in arr:
        if num < 0:
            return num
    return None 


arr = [4, 2, -9, 1, -5, 6]
print("The first negative number in the array is:", find_first_negative(arr))
