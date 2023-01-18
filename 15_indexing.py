text = "Ella sabe Python"
print(text[0])
print(text[1])
#print(text[999]) error
size = len(text) #conteo de caracteres
print('size => ',size)
print(text[size - 1]) #-1 para identificar el ultimo
print(text[-1])

# slicing

print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:-1])
print(text[5:])
print(text[:]) #sustraer completo
print(text[10:16:1]) #sustraer con saltos
print(text[10:16:2])
print(text[::2])
