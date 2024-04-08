'''
isClassStarted = input("Is class started?: ")
if isClassStarted == 'Y' or isClassStarted == 'y':
    print("Class started")
elif isClassStarted == 'n' or isClassStarted == 'N':
    print("Class not started")
else:
    print("Please enter Y or y or N or n")

'''
'''
classStarted= bool(input("Class started or not?[0-False/1-True]:"))

if classStarted:
    print("Class started")
else:
    print("Class not started")'''


'''vegetable = True
salt_present= False

if vegetable and salt_present:
    print("Dish is perfect")
else:
    print("Dish is not perfect")
    print(f"Because Vegetable present {vegetable}")
    print(f"Because Salt present {salt_present}")'''


'''car = False
bike = True

if car or bike:
    print("Car or bike is present, I can travel 100kms")
else:
    print("Car or bike is not present, I can't travel 100kms")'''


'''attendance = int(input("Attendance of the student: "))
assignment = int(input("Assignment of the student: "))

print(f"Attendance criteria met? : {attendance>=75}")
print(f"Assignment criteria met? : {assignment>=75}")

if attendance >= 75 and assignment >= 70:
    print("Criteria met successfully.")
    print("Student is eligible for the examination.")
else:
    print("Criteria is unfullfilled.")
    print("Student is not eligible for the examination.")'''

'''name=input("Enter the name: ")

if name == "Pritish":
    print(f"{name} is an aspiring data scienctist.")
else:
    print(f"{name} might be an engineer.")'''