my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "y se marcho",
  'name': 'Yosef',
  'last_name': 'Estevez',
  'age': 27
}

print(my_dict)
print(len(my_dict))#cuenta los elementos

print(my_dict['age'])#buscar por key
print(my_dict['last_name'])
print(my_dict.get('age'))#tambien busca la key y da el none si no existe

print('avion' in my_dict)
print('estenota' in my_dict)