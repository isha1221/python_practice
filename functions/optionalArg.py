# You are required to make a function which should accept 3 arguments first 
# arg=position to remove/add, second arg list, third arg(Optional) add="n", value=""


def functionality(position,list1:list,add='n',value=''):
    if(add=='n'):
        list1.remove(list1[position])
        return list1
    elif(add=='y'):
        list1.insert(position,value)
        return list1
    else:
        print('mand manus')
        return 'dumb ass'

list1=input('enter elements of list: ').split(',')
position=int(input('enter a number'))
add= input('enter a value y(to add value) or n(to not add value): ')
value=input('enter a vlaue to be added')

finalList=functionality(position,list1,add,value)
print(finalList)