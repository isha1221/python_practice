#NOTE: Tuple is an immutable form of the list data type.i.e Tuples cannot have their values modified, appended, or removed.

type(('hello',))# single value in a tupel
# <class 'tuple'>
type(('hello'))# this will be considered string
# <class 'str'>

a=tuple(['cat', 'dog', 5])
('cat', 'dog', 5)
print(a)
b=list(('cat', 'dog', 5))
['cat', 'dog', 5]
print(b)
c=list('hello')
print(c)