#class and objects in python
#class is a blueprint for creating instances
#instances are objects of a class that are created at runtime
#class is a logical entity while object is a physical entity
#class does not allocate memory on declaration while objects allocate memory on instantiation

#syntax for class
#class Class_Name:
#    Initializer
#    attributes
#    methods   
#    <statement-1>
#    .
#    .
#    .
#    <statement-N>

#syntax for object
#object_name = ClassName()

#example
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

print(emp1) #<__main__.Employee object at 0x0000020F4F6F4E80>
print(emp2) #<__main__.Employee object at 0x0000020F4F6F4F10>

#each object has a unique address in memory

#class variables or attributes
#class variables are variables that are shared among all instances of a class

#syntax for class variable
#class ClassName:
#    class_variable = value

class Rectangle:
    length=0
    breadth=0
    pass
R1=Rectangle()

#accessing class variable
#ClassName.class_variable

print(R1.length)
print(R1.breadth)

#changing class variable using object
#object_name.class_variable = new_value
R1.length=20
R1.breadth=30
print(R1.length)
print(R1.breadth)

#Adding methods to a class
#class Class_Name:
#    instance variable
#    def method_name(self):
#        method body

#Self parameter
class MethodDemo:
    def Display_Message(self):
        print('Welcome')
ob1 = MethodDemo()
ob1.Display_Message() #Welcome

#self parameter and other parameters
class Rectangle2:
    def Calc_Area_Rect(self,length,breadth):
        return length * breadth
ob1 = Rectangle2()
print(ob1.Calc_Area_Rect(10,20)) #200

#syntax for instance variable
#class ClassName:
#    def __init__(self):
#        self.instance_variable = value

#accessing instance variable
#object_name.instance_variable

class Prac:
    x=5
    def disp(self,x):
        x=30
        print(x)
        print(self.x)
ob1 = Prac()
ob1.disp(10) #30 5

#self parameter with methods

class Self_Demo:
    def Method_A(self):
        print('In Method A')
        print('wow got a called from A!!!')
    def Method_B(self):
        print('In Method B calling Method A')
        self.Method_A()
Q=Self_Demo()
Q.Method_B() #In Method B calling Method A 
# In Method A 
# wow got a called from A!!!

#changing class variable using class
#ClassName.class_variable = new_value

#Display Class attributes and Methods
#dir(name_of_class) or dir(object_name)
print(dir(Prac)) #['x', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',

#Class_name.__dict__ or object_name.__dict__
print(Prac.__dict__) #{'__module__': '__main__', 'x': 5, 'disp': <function Prac.disp at 0x0000020F4F6F1CA0>, '__dict__': <attribute '__dict__' of 'Prac' objects>, '__weakref__': <attribute '__weakref__' of 'Prac' objects>, '__doc__': None}

#Special Class Attributes
Prac.__class__ #<class 'type'>
Prac.__name__ #'Prac'
Prac.__module__ #'__main__'
Prac.__bases__ #(<class 'object'>,)
Prac.__dict__ #{'__module__': '__main__', 'x': 5, 'disp': <function Prac.disp at 0x0000020F4F6F1CA0>, '__dict__': <attribute '__dict__' of 'Prac' objects>, '__weakref__': <attribute '__weakref__' of 'Prac' objects>, '__doc__': None}
Prac.__doc__ #None

#changing class variable using class method
#class ClassName:
#    @classmethod
#    def class_method(cls):
#        cls.class_variable = new_value

#changing class variable using constructor
#class ClassName:
#    def __init__(self):
#        ClassName.class_variable = new_value

#changing class variable using instance method
#class ClassName:
#    def instance_method(self):
#        ClassName.class_variable = new_value

# __init__ method (constructor)
# __init__ method is used to initialize the instance variables of a class
# __init__ method is called automatically when an object is created

#syntax for __init__ method
#class ClassName:
#    def __init__(self):
#        self.instance_variable = value

#accessing instance variable
#object_name.instance_variable

class Rectangle3:
    def __init__(self):
        self.length=0
        self.breadth=0
    def Calc_Area(self):
        return self.length * self.breadth
ob1 = Rectangle3()
ob1.length=10
ob1.breadth=20
print(ob1.Calc_Area()) #200

class Circle:
    pi=0
    radius=0
    def __init__(self):
        self.pi=3.14
        self.radius=5
    def Calc_Area(self):
        print('Radius of circle is',self.radius)
        return self.pi * self.radius ** 2
ob1 = Circle()
print('Area of Circle :',ob1.Calc_Area()) #Area of Circle : 78.5

#Accessibility

#no keyword for public, private, protected
#public - accessible from anywhere
#private - accessible only from within the class
#protected - accessible only from within the class and its subclasses

#private
#class ClassName:
#    def __init__(self):
#        self.__instance_variable = value

#accessing private variable
#object_name._ClassName__instance_variable

class Private:
    def __init__(self):
        self.__x=10
    def display(self):
        print(self.__x)
ob1 = Private()
ob1.display() #10
print(ob1._Private__x) #10

#protected
#class ClassName:
#    def __init__(self):
#        self._instance_variable = value

#accessing protected variable
#object_name._instance_variable

class Protected:
    def __init__(self):
        self._x=10
    def display(self):
        print(self._x)
ob1 = Protected()
ob1.display() #10
print(ob1._x) #10

#Passing an object as an argument to a method

class Test:
    a=0
    b=0
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def equals(self,obj):
        if self.a == obj.a and self.b == obj.b:
            return True
        else:
            return False
ob1 = Test(10,20)
ob2 = Test(10,20)
ob3 = Test(30,40)
print(ob1.equals(ob2)) #True


#__del__ method (destructor)

#syntax for __del__ method
#class ClassName:
#    def __del__(self):
#        body of destructor

class Desctructor_Demo:
    def __init__(self):
        print('Welcome')
    def __del__(self):
        print('Destructor Executed Successfully')
ob1 = Desctructor_Demo() #Welcome
ob2 = ob1
ob3 = ob1
print('ID of Ob1',id(ob1)) #ID of Ob1 2299730286928
print('ID of Ob2',id(ob2)) #ID of Ob2 2299730286928
print('ID of Ob3',id(ob3)) #ID of Ob3 2299730286928
del ob2
del ob1
del ob3

#class memebeship test

#syntax for class membership test
#class ClassName:
#    body of class
#    if 'attribute_name' in ClassName:
#        body of if

class Class_Membership_Test:
    x=10
    y=20
    def display(self):
        print('In display')
ob1 = Class_Membership_Test()
print('x' in Class_Membership_Test.__dict__) #True
print('y' in Class_Membership_Test.__dict__) #True
print('display' in Class_Membership_Test.__dict__) #True
print('z' in Class_Membership_Test.__dict__) #False

#isInstance() function

#syntax for isinstance() function
#isinstance(object_name, class_name)

class A:
    pass
class B:
    pass
class C:
    pass
ob1 = A()
ob2 = B()
ob3 = C()

print(isinstance(ob1,A)) #True
print(isinstance(ob2,B)) #True
print(isinstance(ob3,B)) #False
print(isinstance(ob3,B)) #False
print(isinstance(ob1,(A,B,C))) #True
print(isinstance(ob3,C)) #True

#Method Overloading

#Method Overloading is not supported in Python
#Method Overloading is the ability to define more than one method with the same name in a class
#Method Overloading is achieved by using default arguments

#isinatnceof - to check whether an object is an instance of a particular class or not

class Demo1:
    result=0
    def add(self, instanceOf=None, *args):
        if instanceOf =='init':
            self.result=0
        if instanceOf =='str':
            self.result=''
        for x in args:
            self.result += x
        return self.result
ob1 = Demo1()
print(ob1.add('init',10,20,30)) #60
print(ob1.add('str','Hello','World')) #HelloWorld
