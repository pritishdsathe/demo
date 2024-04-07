'''
print("First line.")
print(4+2)
a= 12 
b=12
a1="Pritish"
print(a+b)
print(a*b)
print(a/b)
print(a-b)
print(a%b)
print("Hello", a1)
if(a>b):
    print("a is greater than b")
elif(a<b):
    print("b is greater than a")
else:
    print("a and b are equal")

print("""Good Morning
India""")
print("Hi my name is "+a1+" Sathe")
print(f"Hello, my name is {a1}") #Format String
print('Hi! Myself "Pritish"')
print("Hi! Myself 'Pritish Sathe'")


name = input("Enter your name:")
print(name)
print(type(name))

number = int(input("Enter a number: "))
print(number)
print(type(number))


a = 12
print(a)
print(type(a))
k=str(a)
print(k)
print(type(k))
'''

firstName = input("Enter your first name: ")
lastName= input("Last name: ")
place = input("Enter a place: ")
yob = int(input("Enter year of birth: "))
email = input("Enter your email ID: ")
age = 2024-yob
print()
print(f"""My name is {firstName}
I was born at {place},
{firstName} is currently {age} years old.
Email id of user is {lastName}.{firstName}@gmail.com""") #Format String

