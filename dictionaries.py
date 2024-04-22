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
'''
data = {"name": "Pritish", "mentor":{"Python": "shreya", "AI": "advait", "Stats":"riya"}, "email_id": {"shreya": "shreya@gmail.com", "advait": "advait@gmail.com", "riya":"riya@gmail.com"}}

def get_list_detail(data):
   list_detail = []
   for item in data:
      if type(data[item]) == dict:
         list_detail.append(list(data[item].values()))
         return list_detail

result = get_list_detail(data)
print(result)
'''
#----------------------------------------------------------------
'''
data = {"name": "Pritish", "mentor":{"Python": "shreya", "AI": "advait", "Stats":"riya"}, "email_id": {"shreya": "shreya@gmail.com", "advait": "advait@gmail.com", "riya":"riya@gmail.com"}}
#data["mobile_no"] = [9975152957, 9284081490, 9298979695]
#print(data)
data["name"] = "Pritish Sathe"
print(data)
'''
#----------------------------------------------------------------
'''
def adding(**kwargs):
   return kwargs

data = {"Pritish": "Sathe", "Shreya": "Koranne", "Advait":"Deogade", "mobile": {"Pritish": '9284081490', "Shreya": '9796959493', "Advait":'9695949392'}}
detail = adding(**data)
print(detail)
'''
