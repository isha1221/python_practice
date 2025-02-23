#normal Storing of value for immutable value:
spam = 42
cheese = spam
spam = 100
print(spam, cheese)

# but as list is mutable storing for list work differntly:
# when a list is copied a refernce is created not a new list
spam = [0, 1, 2, 3, 4, 5]
cheese = spam # The reference is being copied, not the list.
cheese[1] = 'Hello!' # This changes the list value.
print(spam,cheese)

#NOTE: list variables don’t actually contain lists—they contain references to lists