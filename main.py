user_option = input('Piedra, Papel o Tijera =>')
computer_option = 'papel'

if user_option == computer_option:
  print('Empate!')
elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('Piedra gana a tijera')
    print('user gano!')
  else:
    print('papel gana a piedra')
    print('computer gano!')
elif user_option == 'papel':
  if computer_option == 'piedra':
    print('papel gana a piedra')
    print('user gano!')
  else:
    print('tijera gana a papel')
    print('Computer gano')
elif user_option == 'tijera':
  if computer_option == 'papel':
    print('tijera ganan a papel')
    print('user gano')
  else:
    print('piedra gana a tijera')
    print('computer gano!')
