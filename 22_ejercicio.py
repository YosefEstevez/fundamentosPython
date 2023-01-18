# Agrega solo los números positivos de una lista

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇

for number in my_list:
    if not number <=0:
        new_list.append(number)
print(new_list)