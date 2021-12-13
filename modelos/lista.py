import requests

def obtem_lista():
    url = 'http://ime.usp.br/~pf/dicios/br-utf8.txt'
    response = requests.get(url)
    if(response.status_code == 200):
        palavras = response.text.split()
        return palavras
    else:
        print("Erro na conexão com o site!!")