#Programa que cria um vetor utilizando o metodo .split()
#E faz o usuario tentar adivinhar um nome da lista
import random

nomes = ''' Ana Maria Júlia Beatriz Sabrina Mirela Hedmilla Marcela Carla essica Luiza Ingrid Karol Jamille Fernanda'''.split()

nomes.sort()
print ('  '.join(nomes))
sorteado = random.choice(nomes)
chute= ' '
while chute != sorteado:
    chute = input('Chute: ')
    if chute == sorteado:
        print ('Parabéns!')
    elif chute > sorteado:
        print ('Alto')
    else:
        print ('Baixo')