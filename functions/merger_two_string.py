# # Write a function to merge two lists and remove duplicates

# def merging(str1, str2):
#     # Merging the two lists and removing duplicates by converting to a set
#     merged = list(set(str1 + str2))
#     return merged

# str1 = input('Enter string 1: ')
# str2 = input('Enter string 2: ')

# result = merging(str1, str2) 
# # it is set therfore the output always will be in randome order
# print("Merged list without duplicates:", result)


# OR
def merging(str1, str2):
    merged = []
    # Add characters from str1
    for char in str1:
        if char not in merged:
            merged.append(char)
    # Add characters from str2, avoiding duplicates already in merged
    for char in str2:
        if char not in merged:
            merged.append(char)
    return merged

str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

result = merging(str1, str2)
print("Merged list without duplicates:", result)
