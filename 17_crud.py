# CRUD Create, Read, Update & Delete

numbers = [1,2,3,4,5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700) #agrega cualquier dato al final
print(numbers)

numbers.insert(0, 'Hola')#inserta en zona especifica
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

index = new_list.index('todo 2')#Busca dentro de el Array
new_list[index] = 'todo changed'#Cambia el valor
print(new_list)

new_list.remove('todo 1') #Elimina elementos
print(new_list)

new_list.pop() #Elimina el ultimo elemento de la lista
print(new_list)

new_list.pop(0)#Elimina una posición
print(new_list)

new_list.reverse() #cambia de posicion toda la lista
print(new_list)

numbers_a = [1, 4, 6 , 3]
numbers_a.sort() #Ordena el Array
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

new_list.sort()