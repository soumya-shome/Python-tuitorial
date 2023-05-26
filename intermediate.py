#list is mutable, ordered, iterable, sliceable, can contain duplicate values.

#list can be written in two ways
#1. using square brackets
#2. using list() constructor

#1. using square brackets
#list_name = [element1, element2, element3, element4, element5]
x=[1,2,3,4,5]
print(x) #[1, 2, 3, 4, 5]
print(type(x)) #<class 'list'>

#2. using list() constructor
#list_name = list([element1, element2, element3, element4, element5])
y=list([1,2,3,4,5])
print(y) #[1, 2, 3, 4, 5]
print(type(y)) #<class 'list'>


#creating an empty list
#list_name = []
#list_name = list()
x=[]

#adding elements to the list
#list_name.append(element)
#list_name.insert(index, element)
#list_name.extend(iterable)

#1. list_name.append(element)
#adds element to the end of the list
x.append(1)
print(x) #[1]
x.append(2)
print(x) #[1, 2]
x.append(3)
print(x) #[1, 2, 3]

#2. list_name.insert(index, element)
#adds element at the specified index
x.insert(0, 0)
print(x) #[0, 1, 2, 3]
x.insert(2, 4)
print(x) #[0, 1, 4, 2, 3]
x.insert(5, 5)

#3. list_name.extend(iterable)
#adds elements of iterable to the end of the list
x.extend([6,7,8,9,10])
print(x) #[0, 1, 4, 2, 3, 5, 6, 7, 8, 9, 10]

#removing elements from the list
#list_name.pop()
#list_name.pop(index)
#list_name.remove(element)
#list_name.clear()

#1. list_name.pop()
#removes and returns the last element of the list
x.pop()
print(x) #[0, 1, 4, 2, 3, 5, 6, 7, 8, 9]

#2. list_name.pop(index)
#removes and returns the element at the specified index
x.pop(0)
print(x) #[1, 4, 2, 3, 5, 6, 7, 8, 9]

#3. list_name.remove(element)
#removes the first occurence of the specified element
x.remove(4)
print(x) #[1, 2, 3, 5, 6, 7, 8, 9]

#4. list_name.clear()
#removes all the elements from the list
x.clear()
print(x) #[]
print(len(x)) #0

#modifying elements of the list
#list_name[index] = new_element
#list_name[start_index:end_index] = new_list
#list_name[start_index:end_index:step_size] = new_list

#1. list_name[index] = new_element
#modifies the element at the specified index
x=[1,2,3,4,5,6,7,8,9,10]
x[0] = 0
print(x) #[0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x[9] = 11
print(x) #[0, 2, 3, 4, 5, 6, 7, 8, 9, 11]

#2. list_name[start_index:end_index] = new_list
#modifies the elements from start_index to end_index-1
x[0:5] = [1,2,3,4,5]
print(x) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
x[2:5] = [3,4,5]
print(x) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

#3. list_name[start_index:end_index:step_size] = new_list
#modifies the elements from start_index to end_index-1 with step_size
x[0:10:2] = [1,3,5,7,9]
print(x) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

#deleting elements from the list
#del list_name[index]
#del list_name[start_index:end_index]







x=[1,2,3,4,5,6,7,8,9,10]

#accessing elements of the list
#list_name[index]
#list_name[start_index:end_index]
#list_name[start_index:end_index:step_size]

#1. list_name[index]
#returns the element at the specified index
print(x[0]) #1
print(x[1]) #2

#2. list_name[start_index:end_index]
#returns the elements from start_index to end_index-1
print(x[0:5]) #[1, 2, 3, 4, 5]
print(x[2:5]) #[3, 4, 5]
print(x[0:10]) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#3. list_name[start_index:end_index:step_size]
#returns the elements from start_index to end_index-1 with step_size
print(x[0:10:2]) #[1, 3, 5, 7, 9]
print(x[0:10:3]) #[1, 4, 7, 10]

#slicing
#list_name[start_index:end_index:step_size]
#returns the elements from start_index to end_index-1 with step_size
print(x[0:10:2]) #[1, 3, 5, 7, 9]
print(x[0:10:3]) #[1, 4, 7, 10]

#iterating over the list
#list_name = [element1, element2, element3, element4, element5]
# for element in list_name:
#     print(element)

for element in x:
    print(element)


