def count_even_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

arr = [10, 3, 5, 8, 22, 1]
even_count = count_even_numbers(arr)
print("The number of even numbers in the array is:", even_count)
