import urllib.request
import json

user = 'fmasanori'
url = 'http://graph.facebook.com/' +user + 'picture?type=large'
figura = urllib.request.urlopen(url).read()

arquivo = user + '.jpg'
f = open (arquivo, 'wb')
f.write(figura)
f.close()

print (arquivo, 'gravado no seu diretório...')