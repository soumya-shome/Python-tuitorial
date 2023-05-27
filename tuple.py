#list is mutable, ordered, iterable, sliceable, can contain duplicate values.

#tuple is immutable, ordered, iterable, sliceable, can contain duplicate values.

#creating a tuple
#1. using parentheses
#tuple_name = ()
#tuple_name = (element1, element2, element3, element4, element5)
x=(1,2,3,4,5)
print(x) #(1, 2, 3, 4, 5)
print(type(x)) #<class 'tuple'>

#2. using tuple() constructor
#tuple_name = tuple()
#tuple_name = tuple([element1, element2, element3, element4, element5])
y=tuple([1,2,3,4,5])
print(y) #(1, 2, 3, 4, 5)
print(type(y)) #<class 'tuple'>

#---------------------Add---------------------

#adding elements to a tuple is not possible as tuples are immutable

#---------------------Remove---------------------

#removing elements from a tuple is not possible as tuples are immutable

#---------------------Update---------------------

#updating elements of a tuple is not possible as tuples are immutable

#---------------------Access---------------------

#1. using index
#tuple_name[index]
print(x[0]) #1
print(x[1]) #2

#2. using negative index
#tuple_name[-index]
print(x[-1]) #5
print(x[-2]) #4

#3. using slice
#tuple_name[start_index:end_index]
print(x[0:2]) #(1, 2)
print(x[1:3]) #(2, 3)

#4. using negative slice
#tuple_name[start_index:end_index]
print(x[-2:-1]) #(4,)
print(x[-3:-1]) #(3, 4)

#5. using stride
#tuple_name[start_index:end_index:stride]
print(x[0:4:2]) #(1, 3)
print(x[1:5:2]) #(2, 4)

#6. using negative stride
#tuple_name[start_index:end_index:stride]
print(x[-1:-5:-2]) #(5, 3)
print(x[-2:-6:-2]) #(4, 2)

#7. using stride with no start_index and end_index
#tuple_name[::stride]
print(x[::2]) #(1, 3, 5)
print(x[1::2]) #(2, 4)

#---------------------Others---------------------


