import socket
import os

'''
def test():
    print("Testing.. Calling a function is successful..!")

a = test()
print(type(a))
'''
#----------------------------------------------------------------
'''
li = [2,5,1,53,0]

def sortings(newli):
    return sorted(newli)

print("List before sorting..")
print(li)
new_set = sortings(li)
print("\nList after sorting..")
print(new_set)
print(type(new_set))
'''
#----------------------------------------------------------------
'''
def func():
    return "Pritish"

print(func() + " " + "Dinesh" + " " + "Sathe")
'''
#----------------------------------------------------------------
'''
def function1():
    return 1,2, [3,4,"Pritish"], (5,6)

print(function1()[2])
'''
#----------------------------------------------------------------

'''
li = list()
n = int(input())
#for i in range(n):    
num = list(map(int, input().split()))
li.append(num)
newli = set(li)
print(newli)

#print(li)
'''
#----------------------------------------------------------------
'''
lis = [1,2,3,4,5,6,7,8,9,10,"Pritish"]
def add(pl):
    tot = 0
    for i in pl:
        if type(i) == int:
            tot = i + tot
    return tot

addition = add(lis)
print(f"Grand total is: {addition}")
'''
#----------------------------------------------------------------
'''
lim=[1,2,3,"Pritish",4,5,6,"Dinesh",7,8,9,"Sathe"]

def listing(lis):
    """This function returns a list consisting of only string datatypes."

    li = list()
    for i in lis:
        if type(i) == str:
            li.append(i)
    return li

newlist = listing(lim)
print(newlist)
'''
#----------------------------------------------------------------
'''
name = input("Enter the string you want to measure: ")
def length(para):
    """ This function returns the length of the string """
    length = 0
    for i in para:
        length = length + 1
    return length
result = length(name)
print(f"Length of the string is: {result}")
'''
#----------------------------------------------------------------
'''
li = [1,2, "Pritish", "Dinesh", "Sathe"]

def count(li):
    for item in range(len(li)):
        print(f"{li[item]} is at index {item}.")

print(count(li))
'''
#----------------------------------------------------------------

'''
def getNameandIP():
    """ This function returns the name and IP of the system.""""

    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    
    return hostname,ipaddress

host = getNameandIP()

print(f"Hostname: {host[0]}")
print(f"IP address: {host[1]}")
'''
#----------------------------------------------------------------
'''
import os

def getIP():
    print(os.system('ipconfig'))

getIP()
'''
#----------------------------------------------------------------
''''
def shutdown():
    """This function shuts down the system in /t time"""

    os.system('shutdown /s /t 1') 

shutdown()
'''
#----------------------------------------------------------------
'''
lis=[2,2,2.5,"Pritish", "Dinesh", "Sathe"]

def mul(lst):
   """This function returns the multiplication of only float and interger values from a list."

    result = 1
    for item in lst:
        if isinstance(item,int) or isinstance(item,float):
            result *= item
    return result

result = mul(lis)
print("Result is: ", result)
'''
#----------------------------------------------------------------

'''
items_list = list()

def fill():
    noi = int(input("Number of items you want to fill: "))
    for items in range(noi):
        items=input("Enter the list of items you want to add to the list:")
        items_list.append(items)
    return items_list

a = fill()
print(a)
'''
#----------------------------------------------------------------
'''
def filler(*args):
    lis = []
    for i in args:
        lis.append(i)
    return lis

print(filler(1,2,3,4,5,6))
'''
#----------------------------------------------------------------

#Wrapping arguments
'''
def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus", sep=','))
'''
#----------------------------------------------------------------

#Wrapping arguments in range
'''
lis = [1,11]
print(list(range(*lis)))
'''
#----------------------------------------------------------------
#Function inside a function as a parameter.
'''
def test1(a):
   a = a**a
   return a

def test2(func):
   return func(4)

print(test2(test1))
#print(k)
'''
#----------------------------------------------------------------
'''
def test1():
    return "Prit"

def test2(func):
    return func()

print(test2(test1))
'''
#----------------------------------------------------------------
'''
def test1(**args):
    return args

def test2(func):
    a = {"Pritish": "Sathe", "Shreya": "Koranne"}
    return func(**a)

print(type(test2(test1)))
'''
#----------------------------------------------------------------
'''
def test1(**args):
    print("I am inside test 1")

    def test2(func):
        print("I am inside test 2")
    
    def test3(func):
        print("I am inside test 3")
        
        
'''
#----------------------------------------------------------------
'''
def func(func):
    print("I am inside test")
    def func2():
        
        """This is a wrapper function. """
        
        print("I am inside func2")
        return func()
    return func2

@func       #Decorator
def test1():
    #print("I am inside test 1")
    return 5+6

a = test1() + 5
print(a)
print(type(a))
'''
#----------------------------------------------------------------
'''
def test1(func):
    """Function with *args""""

    def test2(*args):
        func(*args)
        #print(func(*args))
        print("This is function 2.")
        return func(*args)
    return test2

@test1
def test3(a, b, c):
    return a + b + c

a = test3(2,4,6)
print(a)
#print(a)
print(type(a))
#print(type(test3))
'''
#----------------------------------------------------------------
'''
def test1(func):
    def test2(*args, **kwargs):
        func(*args, **kwargs)
        #print(func(*args, *kwargs))
        print("This is function 2.")
        return func(*args, **kwargs)
    return test2

@test1
def test4(**kwargs):
    return kwargs       

b = test4(a = 5, b = 14)
print(b)
print(type(b))
'''
#----------------------------------------------------------------
'''
v = lambda *args: args
print(v(1))
print(type(v))
'''
#----------------------------------------------------------------
'''
l = [1,2,3,4,5,6,7]
li = []
for i in l:
    i = i + 10
    li.append(i)
print(li)
'''
#----------------------------------------------------------------
'''
l = [1,2,3,4,5,6,7]
def test1(a):
    return a+10

print(list(map(test1,l) ))
'''
#----------------------------------------------------------------
'''
l = [1,2,3,4,5,6,7]
print(list(map(lambda a: a+10, l)))
'''
#----------------------------------------------------------------
'''
l = ['pritish', 'dinesh', 'sathe']

def convert(l):
    return l.upper()
    

print(list(map(convert, l)))
'''
#----------------------------------------------------------------
'''
l = ['pritish', 'dinesh', 'sathe']

def cal(a):
    return len(a)

print(list(map(cal,l)))
'''
#----------------------------------------------------------------
'''
l = [1,2,3,4,5,6,7,8,9,10]

def even(a):
    l1 = []
    if type(a) == list:
        for i in a:
            if i%2==0:
                l1.append(i)
    return l1

num = even(l)
print(num)
'''
#----------------------------------------------------------------

l = [1,2,3,4,5,6,7,8,9,10]

def even(a):
    if a%2 == 0:
        return a

#Filter function. It basically returns True or False

print(list(filter(even, l)))