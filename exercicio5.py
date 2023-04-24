# Escreva um programa que gere a sequência de Fibonacci até um determinado limite fornecido pelo usuário. A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma dos dois números anteriores.

fibonacci = [1, 1]

limit = int(input('Digite a posição final: '))

for i in range(2, limit):
  num = fibonacci[i - 1] + fibonacci[i - 2]
  fibonacci.append(num)


for i in fibonacci:
  print(i, end=' ')