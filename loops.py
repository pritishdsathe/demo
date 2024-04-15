'''
stations= ['Badnera', 'Murtizapur', 'Akola', 'Shegaon', 'Malkapur']

for station in stations:
    station = input("Enter the station you want to go to: ")
    print(f"Reached Station: {station}")
    
    if station == 'Badnera':
        print(f"You have reached your destination: {station}. {station} is a junction on central railway line. \nIt is close to Amravati city and it is the closet railway station to reach to Amravati city. You get high connectivity with other stations from Badnera.")
        break
    elif station == 'Murtizapur':
        print(f"You have reached your destination: {station}. {station} is a junction on central railway line. \nIt is close to Amravati city and it is the closet railway station to reach to Amravati city. You get high connectivity with other stations from Murtizapur.")
        break
    elif station == 'Akola':
        print(f"You have reached your destination: {station}. {station} is a junction on central railway line. \nIt is close to Amravati city and it is the closet railway station to reach to Amravati city. You get high connectivity with other stations from Akola.")
        break
    elif station == 'Shegaon':
        print(f"You have reached your destination: {station}. {station} is a junction on central railway line. \nIt is close to Amravati city and it is the closet railway station to reach to Amravati city. You get high connectivity with other stations from Shegaon.")
        break
    elif station == 'Malkapur':
        print(f"You have reached your destination: {station}. {station} is a junction on central railway line. \nIt is close to Amravati city and it is the closet railway station to reach to Amravati city. You get high connectivity with other stations from Malkapur.")
        break
    elif station == 'Jalgaon':
        print(f"You have reached {station}. The journey ends here.")
        break
else:
    print("Your journey is completed.")


'''
#------------------------------------------------------------------------------------------------------
'''

stations= ['Badnera', 'Murtizapur', 'Akola', 'Shegaon', 'Malkapur']
station = True
while station:
    station = input("Enter the station you want to go to: ")
    #print(f"Reached Station: {station}")

    if station not in stations:
        print(f"{station} is not a valid station. Please try again.")
    
    if station == 'Badnera':
        print(f"You have entered your destination: {station}. {station} is a junction on central railway line. \nIt is close to Amravati city and it is the closet railway station to reach to Amravati city. You get high connectivity with other stations from Badnera.")
        continue
    elif station == 'Murtizapur':
        print(f"You have reached your destination: {station}. {station} is a junction on central railway line. \nIt is close to Amravati city and it is the closet railway station to reach to Amravati city. You get high connectivity with other stations from Murtizapur.")
        break
    elif station == 'Akola':
        print(f"You have reached your destination: {station}. {station} is a junction on central railway line. \nIt is close to Amravati city and it is the closet railway station to reach to Amravati city. You get high connectivity with other stations from Akola.")
        break
    elif station == 'Shegaon':
        print(f"You have reached your destination: {station}. {station} is a junction on central railway line. \nIt is close to Amravati city and it is the closet railway station to reach to Amravati city. You get high connectivity with other stations from Shegaon.")
        break
    elif station == 'Malkapur':
        print(f"You have reached your destination: {station}. {station} is a junction on central railway line. \nIt is close to Amravati city and it is the closet railway station to reach to Amravati city. You get high connectivity with other stations from Malkapur.")
        break
    
else:
    print("Your journey is completed.")

'''
#------------------------------------------------------------------------------------------------------
'''

list_of_names = list()
total_names = int(input("Total names to be added to the list of names: "))
max_length = 0
string = ""

for names in range(0, total_names):
    name = input('Enter your name:')
    list_of_names = list_of_names + [name]
    if max_length < len(list_of_names[names]):
        max_length = len(list_of_names[names])
        string = list_of_names[names]
print(f"{list_of_names}")
print(f"Longest String is {string} and length of the {string} is {max_length}")

'''
#------------------------------------------------------------------------------------------------------

list_of_names = list()
total_names = int(input("Total names to be added to the list of names: "))
i = 1
iterator = 0
max_len = 0
string = ""

while i <= total_names:
    name = input('Enter your name:')
    list_of_names = list_of_names + [name]
    i = i + 1
    if max_len < len(list_of_names[iterator]):
        max_len = len(list_of_names[iterator])
        string = list_of_names[iterator]
    iterator += 1

print(f"{list_of_names}")
print(f"{string} is a longest string with the length of: {max_len}")

#------------------------------------------------------------------------------------------------------
'''
list_of_item = list()
total_items = int(input("Total items you want to add:"))
item = 1 

while item <= total_items:
    item_added = input(f"Enter the {item} item that you want to add:")
    list_of_item = list_of_item + [item_added]
    #list_of_item.append(item_added)
    print(f"Item {item} is {item_added}")
    print('----')
    item = item + 1

print(f"Items in the list are:{list_of_item} \n")

element = input("Enter the item you want to search in the list:")

if element not in list_of_item:
    print(f"{element} is not in the list.")
    print(f"Adding {element} to the list")
    list_of_item = list_of_item + [element]
    print(f"Updated list is: {list_of_item}")
else:
    print(f"{element} is in the list.")
    print(f"The list is: {list_of_item}")
'''
#------------------------------------------------------------------------------------------------------
'''
cost_of_item=[200,500,100,400]

total_cost=0

for total in cost_of_item:
    total_cost = total_cost + total
    print(f"Total cost after iteration: {total_cost}")
    print('----')
else: print(f"Total cost is: {total_cost}")

'''
#------------------------------------------------------------------------------------------------------
'''
cost_of_item=[200,500,100,400]

total_cost=0


for total in range(len(cost_of_item)):
    total_cost = total_cost + cost_of_item[total]
    
    print(f"Total cost after iteration: : {total_cost}")
    print('----')
else: print(f"Total cost is: {total_cost}")
'''
#------------------------------------------------------------------------------------------------------
'''
li = ['Pritish', 'Dinesh', 'Sathe', 27, 'M']
for i in li:
    print(i)
'''
#------------------------------------------------------------------------------------------------------
'''
scores = [100,200,300,400,500]
number = 0
cutoff = 500 
while scores[number] < cutoff:
    print(f"Cutoff not reached.{number}")
    number = number + 1
    print("--------------------------------")
else:
    print(f"Cutoff reached.{cutoff}")
'''
#------------------------------------------------------------------------------------------------------
'''
total_marks = 1000
cutoff = 400
scores = [100, 200, 300, 399, 500]

year = 0

while scores[year] < cutoff:
    print(f"your marks: {scores[year]}")
    year = year + 1
    if scores[year] > cutoff:
        print(f"You have scored: {cutoff}. Congratulations! You have passed the exam.")
'''
#------------------------------------------------------------------------------------------------------
'''
number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # Do anything else you want to do here

print('Done')

'''
#------------------------------------------------------------------------------------------------------
li = [2+3j, "Pritish", 5+6j, "Sathe", 5]


for i in li:
    if isinstance(i, (complex, str, int)):
        print(f"The element: {i} | type: {type(i)} | at Index: {li.index(i)}")

#------------------------------------------------------------------------------------------------------
'''
 li = [["item 1", 1000], ["item 2",1000], ["item 3", 3000]]
total = 0
for i in li:
    print(f"Item {i[0]} costs {i[1]}")
    total = total + i[1]

print("\nAdding total cost of the items:", total)
'''



