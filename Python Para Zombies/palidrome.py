#Verifique se uma palavra lida é palíndrome

palavra = input('Palavra: ')
if palavra == palavra[::-1]:
    print ('É palíndrome')
else
    print ('Não é palíndrome')