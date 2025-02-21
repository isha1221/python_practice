# index method => returns the index of a given element if present in the list

cat=['fluffy','white','persian']
print(cat.index('fluffy'))

## append() adds an elemet at the end of the list
## insert() adds an element at any provided index
#append() and insert() are list specific methods
cat.append('sassy')
print(cat)

cat.insert(2,'pretty')
print(cat)

cat.remove('pretty')
print(cat)

#sorts in alphabetical order
cat2=['fluffy','flat','flower']
cat2.sort()
print(cat2)

#to sort in reverse order
cat.sort(reverse=True)
print(cat)

##cannot sort lists that have both number values and string values 
##sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings.

#below to sort in normal alphabetical order
cat.sort(key=str.lower)
print(cat)

cat.reverse()
print(cat)