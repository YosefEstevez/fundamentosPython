'''
#no pide contador inicial y cuenta desde el 0
for element in range(1, 21):
  print(element)

'''

# ciclo que va desde el primer elemento al ultimo
my_list = [23, 45, 67, 89 ,43]
for element in my_list:
  print(element)

my_tuple = ('Yosef', 'Angelica', 'Rico')
for element in my_tuple:
  print(element)


product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}

for key in product:
  print(key, '=>', product[key])
#item genera arraay de tuplas

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'Yosef',
    'age': 34
  },
  {
    'name': 'Rico',
    'age': 45
  },
  {
    'name': 'Angelica',
    'age': 4
  }
]

for person in people:
  print('name =>', person['name'])
  """print('age =>', person['age'])"""

