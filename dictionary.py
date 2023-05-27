#set is mutable, unordered, iterable, not sliceable, cannot contain duplicate values.

#dictionary is mutable, unordered, iterable, not sliceable, cannot contain duplicate keys but can contain duplicate values.

#creating a dictionary
#1. using curly braces
#dict_name = {}
#dict_name = {key1:value1, key2:value2, key3:value3, key4:value4, key5:value5}
x={1:'a',2:'b',3:'c',4:'d',5:'e'}
print(x) #{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(type(x)) #<class 'dict'>

#2. using dict() constructor
#dict_name = dict()
#dict_name = dict({key1:value1, key2:value2, key3:value3, key4:value4, key5:value5})
y=dict({1:'a',2:'b',3:'c',4:'d',5:'e'})
print(y) #{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(type(y)) #<class 'dict'>

#---------------------Add---------------------

#1. using update() method
#dict_name.update({key1:value1, key2:value2, key3:value3, key4:value4, key5:value5})
x.update({6:'f'})
print(x) #{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}

#---------------------Remove---------------------

#1. using pop() method
#dict_name.pop(key)
x.pop(6)
print(x) #{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

#2. using popitem() method
#dict_name.popitem()
x.popitem()
print(x) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

#3. using clear() method
#dict_name.clear()
x.clear()
print(x) #{}

#---------------------Update---------------------
