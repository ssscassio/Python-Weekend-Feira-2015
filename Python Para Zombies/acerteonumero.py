#Programa que randomiza um número e faz o usuario
#tentar adivinhar o número sorteado
from random import randint
print ('Bem vindo!')
sorteado = randint(1,100)
chute = 0
tentativas = 0
while sorteado != chute:
    chute = int(input('Chute: '))
    tentativas +=1
    if chute == sorteado:
        print ('Você Venceu')
    else:

        if chute < sorteado:
            print('O seu numero é menor que o numero sorteado')
        else:
            print('O seu numero é maior que o numero sorteado')
print ('Fim do jogo! Você precisou de: ' , tentativas)


