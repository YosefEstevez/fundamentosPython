'''
while True:  #si se hace con boolean es infinito
  print('se ejecuto')


counter = 0

while counter < 10:  
  counter += 1
  print(counter)


counter = 0

while counter < 20:
  counter += 1
  if counter == 15:
    break
  print(counter)
'''

counter = 0

# continue solo hace el ciclo despues de que se cumpla la condicion
while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter)