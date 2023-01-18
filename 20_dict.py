person = {
  'name': 'Yosef',
  'last_name': 'Estevez',
  'langs': ['python', 'javascript'],
  'age': 79
}

print(person)

person['name'] = 'Yusepe'
person['age'] -= 52
person['langs'].append('rust')
print(person)

del person['last_name'] #del elimina atributos
person.pop('age')#del elimina atributos

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())