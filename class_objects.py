#class and objects in python
#class is a blueprint for creating instances
#instances are objects of a class that are created at runtime
#class is a logical entity while object is a physical entity
#class does not allocate memory on declaration while objects allocate memory on instantiation

#syntax for class
#class ClassName:
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

#class variables
#class variables are variables that are shared among all instances of a class

class Employee:
    #class variable
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        #instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    #method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Doe', 60000)

print(emp1.pay) #50000
emp1.apply_raise()
print(emp1.pay) #52000


#syntax for class variable
#class ClassName:
#    class_variable = value

#accessing class variable
#ClassName.class_variable

#syntax for instance variable
#class ClassName:
#    def __init__(self):
#        self.instance_variable = value

#accessing instance variable
#object_name.instance_variable

#accessing class variable using object
#object_name.class_variable

#accessing class variable using class
#ClassName.class_variable

#changing class variable using object
#object_name.class_variable = new_value

#changing class variable using class
#ClassName.class_variable = new_value

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







#Object
#Constructor
#Self
#Instance Variables
#Class Variables
#Static Methods
#Inheritance
#Overriding Methods
#Data Hiding