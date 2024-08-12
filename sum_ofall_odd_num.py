def sum_of_odd_numbers(arr):
    return sum(num for num in arr if num % 2 != 0)

arr = [4, 2, 9, 1, 5, 6]
print("The sum of all odd numbers in the array is:", sum_of_odd_numbers(arr))
