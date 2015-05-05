#faça uma funçãoo que dada uma palavra pule uma letra e devolva
# uma palavra sem a letra na posilção dada
#Exemplo.: come('Python' , 3) retorna 'Pyton'

def come(s,n):
    resp = s[:n] + s[n+1:]
    return resp


print(come('Python', 3))