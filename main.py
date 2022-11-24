#Escolha das operações

operacao = input('Selecione a operação desejada: (soma, sub, div, mult):')
x = input('Digite o primeiro número: ')
y = input('Digite o segundo número: ')

#IF e ELSE

if operacao == 'soma':
  resultado = int(x) + int(y)

elif operacao == 'sub':
  resultado = int(x) - int(y)

elif operacao == 'div':
  resultado = int(x) / int(y)

elif operacao == 'mult':
  resultado = int(x) * int(y)

else:
  resultado = 'Desculpe, operação não suportada.'
  
print("O resultado da sua operação é: " + str(resultado))