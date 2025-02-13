# Find the Largest Number in a List
# Question: Write a function find_largest(numbers) that takes a list of numbers and returns the largest number in the list.

# Example Input/Output:
# Enter numbers (comma separated): 3, 7, 2, 9, 5
# Largest number: 9


def find_largest(numbers):
    max_num=numbers[0]
    for i in numbers:
        if i>max_num:
            max_num=i
    return max_num
numbers = list(map(int, input("Enter numbers separated by commas: ").split(',')))

print(find_largest(numbers))








