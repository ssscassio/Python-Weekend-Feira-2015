#Criando uma função para verificar
#se um número é par ou não

def é_par(n):
    return n % 2 == 0

#Criando funções para transformar caracteres em valores
#e valores em caracteres respectivamente

def esconde(msg):
    resp = ' '
    for c in msg:
        resp = resp + chr(ord(c) + 3000)
    return resp

def mostra(msg):
    resp = ' '
    for c in msg:
        resp = resp + chr(ord(c) - 3000)
    return resp

