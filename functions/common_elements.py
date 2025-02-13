# Write a function that returns the common elements between two lists.
def merging(str1, str2):
    merged = []
    # Add characters from str1
    for char1 in str1:
     for char2 in str2:
        if char1==char2 not in merged:
            merged.append(char1)
       
    return merged

str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

result = merging(str1, str2)
print("common elements:", result)
            
            