def sum_positive_numbers(arr):
    total_sum = 0
    for num in arr:
        if num > 0:
            total_sum += num
    return total_sum

arr = [10, -3, 5, 8, -22, 1]
positive_sum = sum_positive_numbers(arr)
print("The sum of all positive numbers in the array is:", positive_sum)


