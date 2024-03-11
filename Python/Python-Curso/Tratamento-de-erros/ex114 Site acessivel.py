import urllib.request
try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.HTTPError:
    print('O site pudim não está acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso')