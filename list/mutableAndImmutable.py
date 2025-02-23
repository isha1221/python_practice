# NOTE:A list value is a mutable data type: it can have values added, removed, or changed.
# However, a string is immutable: it cannot be changed.


#A way to mute a string is using slicing and concatination creating new string
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]#in this counting we are considering spaces as well
print(newName)
# print(name[0:9])


##################

#Even though lists are mutable 
eggs = [1, 2, 3]
eggs = [4, 5, 6]
# this is not muting here it is just overwriting the older list with newer list
# for actually muting a list you will have to do the following:
eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)