 #print hello world
print("Hello World")

#declare variable  of each type
x = 1
y = 1.0
z = "1.0"
a = True

#check type of each variable
print(type(x))
print(type(y))
print(type(z))
print(type(a))


#convert variable to other type
print(float(x))
print(int(y))
print(int(z))
print(str(x))
print(bool(x))

#print statement using format{}
print("x is {} and y is {}".format(x,y))

#print statement using f-string
print(f"x is {x} and y is {y}")

#print statement using % operator
print("x is %d and y is %f"%(x,y))

#print statement with multiple lines
print("""this is a
multiline
statement""")
print("this is a \nmultiline \nstatement")

#print statement with end
print("this is a", end=" ")

print("single line statement")


#take a inout from the user and print it
x = input("Enter a number: ")
print(x)

#decalre a funtion to find whether a number is pallindrome or not
def is_pallindrome(x):
    return str(x) == str(x)[::-1]

print(is_pallindrome(121))