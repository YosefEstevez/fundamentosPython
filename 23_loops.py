matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
# se pone como en coordenadas
print(matriz[0][1])

#row = fila colum = columnas
for row in matriz:
  print(row)
  for column in row:
    print(column)