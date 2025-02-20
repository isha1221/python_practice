# The Multiple assignment Trick => Tuple upacking
# assign multiple variables with the values in a list in one line

# if you do this:

cat=['fluffy','white','persian']
size=cat[0]
color=cat[1]
breed=cat[2]
print(size)

# then instead you can do this:
cat=['fluffy','white','persian']
size,color,breed=cat
print(size)

for index,items in enumerate(cat):
    print('The '+str(index)+' poperty of cat is '+ items)