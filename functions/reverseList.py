# Write a function to reverse a list in-place (without using the reverse() method).

#Method one
# def reverse_list(lst):
#     left, right = 0, len(lst) - 1  # Start from both ends
#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]  # Swap elements
#         left += 1
#         right -= 1

# lst = input("Enter elements separated by space: ").split()
# reverse_list(lst)  # Modifies lst in-place
# print("Reversed list:", lst)

#Method two(slicing)
def reverse_list(lst):
    return lst[::-1]  # Returns a new reversed list

lst = input("Enter elements separated by space: ").split()
lst = reverse_list(lst)  # Store the reversed list
print("Reversed list:", lst)
