
##NOTE: difference between slicing and indexing => indexing returns a particular nuber of the list but 
# slicling returns a sub list of given range from the list


list=['1','2','3','4','5','6']
print(list[1:3])
#otp:['2','3']
#[where to start:where to end] can be from [0]:[length of list] 

print(list[::-1]) 
#reverse list 
#slicing can also be [where to start:where to end:how many steps to move]
# here it is [start=0:end=length of list:step=-1 which means it will iterrate in the reverse order i.e opposite side

print(len(list))
# length of list=6

list[0]='isha'
print(list)

# concatination
listA=['1','2','3']
listB=['2','3','4']
print(listA+listB)

#replication
listA=['1','2','3'] * 3
print(listA)

#deletion
del list[2]
print(list)