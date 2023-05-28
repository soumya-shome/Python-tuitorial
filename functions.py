#funtions in python
# def function_name(parameters):
#     """docstring"""
#     statement(s)
#     return [expression]

def printme(str):
    print(str)
    return
printme("I'm first call to user defined function!") #I'm first call to user defined function!

#function
def changeme(mylist):
    mylist.append([1,2,3,4])
    print("Values inside the function: ", mylist)
    return
changeme(mylist = [10,20,30]) #Values inside the function:  [10, 20, 30, [1, 2, 3, 4]]

#function arguments
def printinfo(name, age):
    print("Name: ", name)
    print("Age: ", age)
    return
printinfo(age = 50, name = "miki") #Name:  miki Age:  50

#function with default arguments
def printinfo2(name, age=35):
    print("Name: ", name)
    print("Age: ", age)
    return
printinfo2(age = 50, name = "miki") #Name:  miki Age:  50

#function with variable-length arguments
def printinfo3(arg1, *vartuple):
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo3(10) #Output is:  10

#anonymous functions
sum = lambda arg1, arg2: arg1 + arg2
print("Value of total: ", sum(10,20)) #Value of total:  30

#recursion
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
print(factorial(5)) #120

#global vs local variables
total = 0 #global variable
def sum(arg1, arg2):
    total = arg1 + arg2 #local variable
    print("Inside the function local total: ", total)
    return total
sum(10,20) #Inside the function local total:  30

#global keyword
def sum2(arg1, arg2):
    global total
    total = arg1 + arg2
    print("Inside the function local total: ", total)
    return total
sum2(10,20) #Inside the function local total:  30

#pass by reference
def changeme2(mylist):
    mylist = [1,2,3,4]
    print("Values inside the function: ", mylist)
    return
mylist = [10,20,30]
changeme2(mylist) #Values inside the function:  [1, 2, 3, 4]

#pass by value
def changeme3(mylist):
    mylist.append([1,2,3,4])
    print("Values inside the function: ", mylist)
    return
mylist = [10,20,30]
changeme3(mylist) #Values inside the function:  [10, 20, 30, [1, 2, 3, 4]]

#empty function
def functionname():
    pass
functionname() #no output

#scope function
def outer_function():
    a = 20
    def inner_function():
        a = 30
        print("a = ", a)
    inner_function()
    print("a = ", a)
a = 10
outer_function() #a =  30 a =  20

#returning multiple values
def func():
    str = "Hello World"
    x = 20
    return str, x
str, x = func()
print(str) #Hello World
print(x) #20

#function documentation
def printme(str):
    """This prints a passed string into this function"""
    print(str)
    return
printme("I'm first call to user defined function!") #I'm first call to user defined function!
print(printme.__doc__) #This prints a passed string into this function

#-----------------Lambda----------------

#using lambda
def sum(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function local total: ", total)
    return total
sum(10,20) #Inside the function local total:  30

#lambda syntax
#lambda [arg1 [,arg2,.....argn]]:expression

#lambda examples
lambda x: x*x
lambda x, y: x+y
lambda: 'Hello World'

#lambda with filter()







#lambda with no arguments
sum = lambda arg1, arg2: arg1 + arg2

#lambda with single argument
cube = lambda x: x*x*x
print(cube(7)) #343

#lambda with multiple arguments
sum = lambda arg1, arg2: arg1 + arg2
print("Value of total: ", sum(10,20)) #Value of total:  30


2. using lambda with filter()
3. using lambda with map()
4. using lambda with reduce()