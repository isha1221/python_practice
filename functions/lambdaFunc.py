# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))


# Square a number using lambda
from functools import reduce


def squ(n):
    return lambda a:a**n

power_of_num= squ(5)
print(power_of_num(2))



# Sort a list of tuples by second element
# # Given: [(1, 2), (3, 1), (5, 0)]
#output: [(5, 0), (3, 1), (1, 2)]
# Sort using a lambda that extracts the second element.

sorted_data = sorted([(1, 2), (3, 1), (5, 0)], key=lambda x: x[1])
print(sorted_data)


# Map in lambda
# Use lambda with map() to double every number
# Given a list [1, 2, 3, 4], use map + lambda to get [2, 4, 6, 8]

lambda_map=list(map(lambda n: 2 * n, [1, 2, 3, 4]))
print(lambda_map)



# Use lambda with filter() to keep only odd numbers
# Given a list [1, 2, 3, 4, 5], use filter + lambda to get [1, 3, 5]

nums = [1, 2, 3, 4, 5]
lambda_filter=list(filter(lambda n: n % 2 == 1, nums))
print(lambda_filter)



# Use lambda with reduce() to find the product of a list
# From functools import reduce
# Example: [1, 2, 3, 4] -> 24
lambda_reduce = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(lambda_reduce)