import json
import urllib

url ="https://jsonplaceholder.typicode.com/users"
resp = urllib.urlopen(url)
text = json.loads(resp.read())
nome = "Samantha"
cont=0
i=0

for d in text:
    if nome in d['username']:
        print('E-mail, Samantha username: ', d['email'])


for d in text:
    print(d['username'], ' -> ',d['website'] , '\n')


while i <= 10:
    for d in text:
         if d['address']['geo']['lat'] < '0':
            cont = cont + 1

    break

print('Numero de moradores do Hemiserio Norte: ', cont)