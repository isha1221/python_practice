def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Swap if the element is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print(sorted_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
