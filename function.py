import socket

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
        """ This function returns the length of the string""""
    
    length = 0
    for i in range(len(para)):
        length = length + 1
    return length
result = length(name)
print(f"Length of the string is: {result}")
'''
#----------------------------------------------------------------
'''
li = ["Shree", "Pritish", "Dinesh", "Sathe"]
element = input("Enter the element you wish to search:")

def index(name, ele):
    """ This function returns the index of the string.""""
    
    for i in range(len(li)):
        if element == li[i]:
            #print("Hi!")
            return i
        
result = index(li,element)
print(f"{element} is found at index {result}")
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

