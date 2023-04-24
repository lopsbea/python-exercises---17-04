# Escreva um programa que peça ao usuário para digitar um número inteiro positivo e, em seguida, exiba todos os números ímpares de 1 até esse número.

number = int(input('Digite um número inteiro positivo: '))

for i in range(1, number + 1):
  if i % 2 != 0:
    print(i)