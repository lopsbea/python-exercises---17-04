# Escreva um programa que simule o jogo da "adivinhação" em que o computador escolhe um número aleatório e o usuário tem que tentar adivinhar o número. O programa deve continuar pedindo ao usuário para adivinhar até que ele acerte o número.

import random

a = random.randint(1, 10)

b = int(input('Adivinhe o número que estou pensando: ')) 

while b != a:
  print('Errou! tente novamente.')
  b = int(input('Adivinhe o número que estou pensando: ')) 
  
print('Parabéns, você acertou!')
  