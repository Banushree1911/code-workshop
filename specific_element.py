def count_occurrences(arr, element):
    count = 0
    for num in arr:
        if num == element:
            count += 1
    return count

arr = [10, 3, 5, 8, 3, 1, 3]
element_to_count = 3
occurrences = count_occurrences(arr, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the array.")
