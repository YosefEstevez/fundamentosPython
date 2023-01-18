numbers = (1, 2, 3, 5)
strings = ('Yosef', 'Angelica', 'Rico', 'Simon')
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD
# numbers.append(10)
print(numbers)
# numbers[1] = 'change'

print(strings)
print(strings.index('Angelica'))#Busca la posicion
print(strings.count('Yosef'))#cuantas veces esta repetido

my_list = list(strings)#list covierte la tupla a lista
print(my_list)
print(type(my_list))

my_list[1] = 'Victoria'
print(my_list)

my_tuple = tuple(my_list)#tuple vuelve una lista a tupla
print(my_tuple)