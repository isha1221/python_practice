our_list = [1, 3, 4, "Adam"]
new_items = []

for i in our_list:
    if str(i).lower() == "adam":
        i = i.upper()
    new_items.append(i)

# Now extend the original list
our_list=new_items
print(our_list)
