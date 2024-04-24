"""
1. Print the first 5 positive integers in ascending order with one number 
in each line

for i in range(1,6):
    print(i)
"""

#-------------------------------------------------------------------------

"""
2. Print the following pattern
*
**
***
****
*****
There are no spaces between consecutive stars. There are no spaces 
at the end of each line.


for i in range(1,6):
    print('*'*i)
"""

#-------------------------------------------------------------------------

"""
3. Accept an integer as input and print its square as output.

number = int(input("Enter the number:"))
print(number**2)

"""

#-------------------------------------------------------------------------

"""
4.Accept two integers as input and print their sum as output.

num1 = int(input("Enter num 1:"))
num2 = int(input("Enter num 2:"))

print(num1 + num2)

"""

#-------------------------------------------------------------------------

"""
5. Accept two words as input and print the two words after adding a 
space between them 

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

print(word1 + " " + word2)

"""

#-------------------------------------------------------------------------

"""
6. Accept the registration number of a vehicle as input and print its 
state-code as output.


number= input("Enter the Vehicle Number: ").upper()
print(number, sep=" ")
print("State code of the vehicle is: ", number[0:2])

"""
#-------------------------------------------------------------------------

"""
7.Accept a five-digit number as input and print the sum of its digits as 
output.

num = input("Enter a number:")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)

"""
#-------------------------------------------------------------------------

"""
8.Accept five words as input and print the sentence formed by these 
words after adding a space between consecutive words and a full stop 
at the end.



words = input(" "), input(" "), input(" "), input(" "), input(" ")
add = words[0] +" " + words [1] + " " + words [2] + " " + words [3] + " " + words [4] 
print(add)
print(type(add))

"""

#-------------------------------------------------------------------------
"""
9.Accept the date in DD-MM-YYYY format as input and print the 
year as output.

dob = input("Enter your dob in (DD-MM-YYYY) format: ").split('-')
#date = input("Enter your date of birth: ")
#month = input("Enter your month of birth: ")
#year = input("Enter your year of birth: ")
#print(f"{date}-{month}-{year}")
#print(year)
#print(dob)
print(dob[2])

"""

#-------------------------------------------------------------------------

"""
10.Accept a sequence of five single digit numbers separated by commas 
as input. Print the product of all five numbers.
 
num = input("Enter the numbers: ").split(',')
prod = 1

for i in range(min(5, len(num))):  
    prod *= int(num[i])

print(f"Product value is: {prod}")

"""

#-------------------------------------------------------------------------

"""
11. Accept two positive integers x and y as input. Print the number of 
digits in xy

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

result = num1**num2
print(result)


"""

#-------------------------------------------------------------------------
"""
12. Accept a string as input. If the input string is of odd length, then 
continue with it. If the input string is of even length, make the 
string of odd length as below:
• If the last character is a period (.), then remove it 
• If the last character is not a period, then add a period (.) to the 
end of the string
Call this string of odd length word. Select a substring made up of 
three consecutive characters from word such that there are an 
equal number of characters to the left and right of this substring. 
Print this substring as output. You can assume that all input 
strings will be in lower case and will have a length of at least four



input_string = input("Enter a string: ")
if len(input_string) % 2 != 0:
    result = input_string
else:
    if input_string[-1] == ".":
        result=input_string[:-1]
    else:
        result = input_string + "."

for i in range(1, len(input_string) - 1):
    substring = input_string[i-1:i+2]  # Get a substring of three consecutive characters
    
    # Check if the substring has an equal number of characters to the left and right
    if input_string[:i].count(substring[0]) == input_string[i+1:].count(substring[-1]):
        print("Output:", substring)
        break
#print(result)
"""

#-------------------------------------------------------------------------
"""
34.Program to Get Data Items From a List Appearing Odd Number of Times
"""
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#-------------------------------------------------------------------------

"""
36. remove items from a list while iterating but without creating a different copy of a list.
Remove numbers greater than 50
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected Output: [10, 20, 30, 40, 50]

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
number_list = [x for x in number_list if x < 50]

print(number_list)
"""

#-------------------------------------------------------------------------

"""
37.  Display all duplicate items from a list
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
Expected Output: [20, 60, 30]


sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
newlist = list()

for item in range(len(sample_list)):
    for item2 in range(item + 1, len(sample_list)):
        if sample_list[item] == sample_list[item2]:
            newlist.append(sample_list[item2])
print(newlist)
"""    
#-------------------------------------------------------------------------

"""

38. Create an outer function that will accept two strings, x and y. (x= 'Emma' and y = 'Kelly'.
Create an inner function inside an outer function that will concatenate x and y.
At last, an outer function will join the word 'developer' to it.

def outer(x,y):
    def inner():
        return x + y
    
    functionString = inner()
    concate_string = functionString + 'developer'
    return concate_string


x = input()
y = input()

result = outer(x,y)
print(result)
"""
#-------------------------------------------------------------------------

"""
39. Modify the element of a nested list inside the following list
Change the element 35 to 3500

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]

list1[1][2][2][1]=3500
print(list1)
"""
#-------------------------------------------------------------------------
"""
40. Access the nested key increment from the following dictionary
Access 12
emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}


emp_dict = { "company":{ "employee": { "name": "Jess", "payable": { "salary": 9000, "increment": 12}}}}
current_dict = emp_dict["company"]["employee"]["payable"]["increment"]
print(current_dict)
"""
#-------------------------------------------------------------------------

"""
41. Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17
prev = 0

for i in range(10):
    add = prev + i
    print(f"Current Number {i} Previous Number  {prev}  Sum:  {add}")

    prev = i
"""

#-------------------------------------------------------------------------

"""
42. Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "ineuron" so you should display ‘i’, ‘e’, ‘r’, ‘n’.

string = input("Enter yours string: ")
for iterate in range(len(string)):
    if iterate %2 == 0:
        print(string[iterate] , end = "")

"""
#-------------------------------------------------------------------------
"""
43. Print multiplication table form 1 to 10

for i in range(1,11):
    #print(i, end=" ")
    for j in range(1, 11):
        print(i * j, end=" ")
    print()

"""
#-------------------------------------------------------------------------
