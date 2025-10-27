person = {"name" : "Alice",
          "age" : 24,
          "address" : "7th Street Monrovia",
          "status" : "Single",
           "friends" : ['Kate', 'George']}

print(person)
print(type(person))

#bracket notation
print(person["name"])

#get
print(person.get('address'))

#add a new key-value pair
person['id'] = 34678
person['dob'] = '12/12/2005'
print(person)

#update key-value pairs
person['name'] = 'Jack'
print(person)

#update multiple keys
person.update({'name': 'ALICE', 'age': 30, 'status': 'Married'})
print(person)

#pop
person.pop('age')
print(person)

#popitem
person.popitem() #removes the last item
print(person)

#keys, values and items
print(person.keys())
print(person.values())
print(person.items())
