#Programa que converte o formato da data
#Utilizando o split() juntamente com vetores
meses = 'Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'.split()

d,m,a = input('Data: ').split('/')

print (d, " de ", meses[int(m) - 1], " de ", a)