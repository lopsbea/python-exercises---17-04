# Utilizando a estrutura de repetição for, faça um programa em C que receba 10 números e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas informações.

numbersInInterval = 0

numbersOutOfInterval = 0

for i in range(10):
  num = int(input(f'Digite o número {i + 1}: '))
  
  if 10 <= num <= 20:
    numbersInInterval += 1
  else:
    numbersOutOfInterval += 1
    
print(f'Quantidade de números entre 10 e 20: {numbersInInterval}')
print(f'Quantidade de números fora do intervalo de 10 e 20: {numbersOutOfInterval}')