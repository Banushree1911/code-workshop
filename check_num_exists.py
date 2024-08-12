def check_number_exists(arr, num):
    return num in arr

arr = [4, 2, 9, 1, 5, 6]
num_to_check = 5
print("Does the number exist in the array?", check_number_exists(arr, num_to_check))
