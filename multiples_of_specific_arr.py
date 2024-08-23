def count_multiples(arr, n):
    return sum(1 for x in arr if x % n == 0)

array = [2, 3, 4, 5, 6, 8, 10]
number = 2
result = count_multiples(array, number)
print("Number of multiples of", number, ":", result)
