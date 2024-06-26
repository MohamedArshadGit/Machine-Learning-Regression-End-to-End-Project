import math as m
a=2
b=3
ans=a**b
print(ans)
c=10.6
print(m.floor(c))
print(m.ceil(c))
#To print Arshad Rocks Rocks Rocks Rocks 5 times
i=1
while i<=5:
    print("Arshad",end=" ")
    i+=1
    j=1
    while j<=4:
        print("Rocks",end=" ")
        j+=1
    print()
#Stock
stock=6
i=1
while i<=6:
    if i>6:
        break
    else:
        print(i,":Candy")
        i+=1
#return Statement
def add_sub(x,y):
    return x+y,x-y #returning multiple values in a statement
add,sub=add_sub(10,5)
print(add,"\n",sub)

def detail(name,age):
    return f"{age} \t {name}"
person=detail("alice",28) #person is called as variable of a function call
# "alice" 28 is called as attributes
print(person)

def detail(name,age=None):
    return f"{age} \t {name}"
obj=detail("alice")
print(obj)

def sum(x,*y):
    c=x
    for i in y:
        c=c+i
    return c

res=sum(5,10,15) #res is called as variable of a function call
print(res)

a=10
def func():
    a=20
    print("inside the function",a)
func()
print("global variable",a)

# To Alter the Global variable inside the function use "global"
b=10
def func1():
    global b 
    b=20
    print("inside the function",b)
func1()
print("global variable",b)
y=100
z=200
#print(globals()) #if we use globals() inside the function it will display all the global variables outside the function

zz=10001
yy=200000001

def access_globals():
    #print(f"all global variables:{globals()}")
    
    #if we need to access specific global variable
    x=globals()['yy']
    print("Accessing only specific global variable yy:",x)
    #modify using globals
    globals()['yy']=300000001
    print("Modifying global variable yy using globals():",yy) #here if we print x it will show 2000001 only

access_globals() 
    
#filter map reduce

#filter  ==>used for conditional fitering
evens =list(filter(lambda n:n%2==0,[1,2,3,4,5,6,7,8,9]))
print(evens)

#map ==>used as a iterator
squared_no = list(map(lambda n :n**2,[1,2,3,4,5]))
print(squared_no)

#reduce used for rolling computation like summation or product and returns a single value
from functools import reduce
product =reduce(lambda n,m :n*m,[1,2,4,5,6])
print(product)

doubles = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(doubles)
print()

#######################OOPS#############

##ATTRIBUTES-2 TYPES- 1)INSTANCE ATTRIBUTES-> Defined within the init method 2)CLASS ATTRIBUTES-
#Defined within the class 

# eg:

class Dog:
    species ='Shiba ' #class Attributes
    
    def __init__(self,Name,age) -> None: # -> None: this means it does not returns any value
        #Using -> None in the __init__ method (or any method)=> that "does not return a value"
        # is a way to leverage Python's type hinting for clarity and maintainability.
        # It communicates the intended use of the method more explicitly to both humans and 
        # tools that analyze the code.
        
        self.name =Name #instance Attributes
        self.age =age #instance Attributes
    
    def bark(self):
        return f"{self.name} whose age is {self.age} says woof!!!"

#Creating Instance of Dog class
Dog1 = Dog('Richie',3) # dog1 is an object of Dog class

#calling bark method

print(Dog1.bark()) #called as Method call ,# use paranthesis to call a function
print(Dog1.species) #using class Attributes
print(Dog1.name) #note this ,we are printing instance attributes 
print(Dog1.age)

class computer:
    def config(self):
        print("i7,intel")
com1=computer()
#com1 =computer #here we can create com1= computer ,without pranthetis at computer but config method
#should be used without self like def config:
com1.config()