import urllib.request
import json

def save_image(friend) :
    size = 'picture?width=200&height=200'
    url = 'https://graph.facebook.com/' + friend('id') +size
    image = urllib.request.urlopen (url).read()
    f = open (friend['name']) +'.jpg', 'wb'
    f.write(image)
    f.close
    print (friend['name'] + '.jpg impresso')
#get the token https
url = 'https://graph.facebook.com/me/friends?access_token-<CAACEdEose0cBAG7MPZBuZCq3wZAW6lNzkkjWUFzUZBieBvb30LtNUJh0O8iMJ96RI3TcHVUA5ofMkQLDdFfOnDv9Nj16fHP7a0HnPK9VznXZAtvtDywE7zTkK03v2wlUA7OjZCqJ3MUhiHBDJloT6PTOVXAwCZBZBH9TvYSWE0ImyyS6QbKgKykCBNmyNtygmoTzpX0ehUpKOeLKZCBSSgrwS>'
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

for friend in dadta['data']:
    save_image (friend)