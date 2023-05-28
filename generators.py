#generators in python
#generator is a function that returns an object (iterator) which we can iterate over (one value at a time)
#generator function contains one or more yield statement
#when called, it returns an object (iterator) but does not start execution immediately
#methods like __iter__() and __next__() are implemented automatically
#once the function yields, the function is paused and the control is transferred to the caller
#local variables and their states are remembered between successive calls
#finally, when the function terminates, StopIteration is raised automatically on further calls


#simple generator function
# def my_gen():
#     n = 1
#     print('This is printed first')
#     yield n
#     n += 1
#     print('This is printed second')
#     yield n
#     n += 1
#     print('This is printed at last')
#     yield n
# a = my_gen()
# print(next(a)) #This is printed first 1
# print(next(a)) #This is printed second 2
# print(next(a)) #This is printed at last 3
# print(next(a)) #StopIteration

#generator syntax
#(expression for item in iterable)
#(expression for item in iterable if condition)
#(expression for item1 in iterable1 if condition1
#            for item2 in iterable2 if condition2
#            for item3 in iterable3 if condition3
#            ....
#            for itemN in iterableN if conditionN)

#generator expression
# a = (x*x for x in range(3))
# print(next(a)) #0
# print(next(a)) #1
# print(next(a)) #4
# print(next(a)) #StopIteration


#generator 
def my_gen():
    n = 1
    print('This is printed first')
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n
a = my_gen()
print(next(a)) #This is printed first 1
print(next(a)) #This is printed second 2
print(next(a)) #This is printed at last 3
print(next(a)) #StopIteration

#generator using yield with arguments
def rev_str(my_str):
    length = len(my_str)
    for i in range(length -1, -1, -1):
        yield my_str[i]
for char in rev_str("hello"):
    print(char) #o l l e h

#generator expression
a = (x*x for x in range(3))
print(next(a)) #0
print(next(a)) #1
print(next(a)) #4
print(next(a)) #StopIteration

#generator using yield with arguments and return   
def rev_str(my_str):
    length = len(my_str)
    for i in range(length -1, -1, -1):
        return my_str[i]
for char in rev_str("hello"):
    print(char) #o l l e h
