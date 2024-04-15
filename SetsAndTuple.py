'''
a = (12,2,5,1,7,0)

b = sorted(a)
print(a)
print(type(a))

print(b)
print(type(b))

amazon_cart=[("Phone", 10000), ("Laptop", 40000)]
print(amazon_cart[0][1])
'''
#----------------------------------------------------------------

'''
amazon_cart=[("watch", 5000), ("laptop",30000), ("phone", 10000), ("shirt", 1000)]
number_of_item = int(input("Number of item you want to purchase:"))
total_amount = 0

for iterator in range(number_of_item):
    item_name = input("Item Name that you want to purchase:").lower()
    for name, price in amazon_cart:
        if name == item_name:
            total_amount = total_amount + price
            break
    else:
            print(f"{item_name} is currently not available.")

print(f"Total amount to be paid: {total_amount} Rupee.")
'''
#----------------------------------------------------------------
'''
new_set = {1,2,"Pritish", 27, "Kaloti Nagar"}
print(new_set)
print()
new_set.update([9,10,11])
print(new_set)
print()
new_set.remove("Kaloti Nagar")
print(new_set)

a = new_set
print(a)
a.update(["ABC"])
print(a)
a.remove("ABC")
print(a)
print(type(a))
'''
#----------------------------------------------------------------

'''
n=int(input("Number of"))
li = list()
newli = list()

for i in range(n):
    k = int(input())
    li.append(k)
    li.sort()

print(li)
'''
#----------------------------------------------------------------
