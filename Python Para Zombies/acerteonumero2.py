#Programa simplificado que randomiza um número
#e faz o usuario tentar adivinhar o número sorteado

from random import randint
secreta =  randint(1, 100)
while True:
    chute = int(input('Chute: '))
    if chute == secreta:
        print ('Parabéns!')
        break
    else:
        print ('Seu chute é mais alto' if chute> secreta else 'Seu chute é mais baixo')
print ('Fim de jogo')