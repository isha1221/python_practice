#arg type to be displa
def removeFromlist(position,list1:list):
    list1.remove(list1[position])
    return list1

list1=input('enter elements of list: ').split(',')
print('position should be between 0 to', len(list1)-1)
position= int(input('enter a position to be eleminated from the list : '))


finalList=removeFromlist(position,list1)
print(finalList)