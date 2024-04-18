''' 
data = {"car1": "Audi", "car2": "BMW", "car3": "Mini Cooper", "car4": "Mercedes"}
'''
#----------------------------------------------------------------
'''
for item in data:
    print(item)
'''
#----------------------------------------------------------------
'''
for item in data.values():
   print(item)
'''
#----------------------------------------------------------------
'''
for names in data.keys():
   print(names)

print(data)
'''
#----------------------------------------------------------------
'''
keys = ["Pritish", "Dinesh", 'Sathe']
values = ["Python", "Java", "C"]

data = dict(zip(keys, values))
#print(data)
print(data.values())
'''
#----------------------------------------------------------------
'''
data = {"Candidate_1": "Pritish",
        "Candidate_2": "Advait",
        "Candidate_3": "Shreya",
        "Candidate_4": "Riya"}

print(data)
'''
#----------------------------------------------------------------
'''
data = {"name": "Pritish", "mentor":{"Python": "Shreya", "AI": "Advait", "Stats":"Riya"}}
list_mentors = list()

print(data["mentor"]["Stats"])
print(list(data.keys()))
print(list(data.values()))
print(data.items())
print(list((data["mentor"].values())))

for item in data.keys():
   if type(data[item]) == dict:
      list_mentors.append(list(data[item].values()))

print(list_mentors)
'''
#----------------------------------------------------------------

data = {"name": "Pritish", "mentor":{"Python": "Shreya", "AI": "Advait", "Stats":"Riya"}}

for item in data:
   print(data[item])