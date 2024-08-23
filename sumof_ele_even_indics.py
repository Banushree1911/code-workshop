def sum_even_indices(arr):
    return sum(arr[i] for i in range(len(arr)) if i % 2 == 0)

array = [1, 2, 3, 4, 5, 6]
result = sum_even_indices(array)
print("Sum of elements at even indices:", result)
