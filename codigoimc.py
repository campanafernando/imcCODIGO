nome=input('Qual seu nome?\n\n')
altura=float(input(f'Qual sua altura {nome}?\n\n'))
peso=int(input('Qual o seu peso?\n\n'))
imc=round(peso/(altura*altura),2)
print(f'O seu imc é:{imc}')
if imc>25 and imc<29.9:
  print('Você está acima do peso :(')  
if imc>18.5 and imc<24.9:
  print('Você está no peso ideal!')
if imc<18.5:
  print('Você está abaixo do peso ideal.')
if imc>30:
  print('Você está obeso.')
