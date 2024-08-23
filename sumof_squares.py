def sum_of_squares(arr):
    return sum(x**2 for x in arr)

array = [1, 2, 3, 4]
result = sum_of_squares(array)
print("Sum of the squares of the elements:", result)
