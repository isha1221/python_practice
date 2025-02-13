def spam(divideBy):
    try: 
        return 42 / divideBy
    except ZeroDivisionError:
        print('lol dividing by zero huh?')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# print(spam(1)) is never executed below as once you reach the error message it won't go to try block again 
def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')