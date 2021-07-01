from os import link
import requests
from bs4 import BeautifulSoup
import funcoes
import json
from informacoes import links, t



data = {}
for y in range(0, len(links)):
    response = requests.get(url=links[y])
    soup = BeautifulSoup(response.text, 'html.parser')
    titulos = soup.find_all("h2", {'class':'box-produto__desc-prod'})
    reais = soup.find_all("span", {'class':'box-produto__preco__valor'})
    centavos = soup.find_all("span", {'class':'box-produto__preco__centavos'})
    precos = funcoes.str_to_float(reais, centavos)

    result = []
    for x in range(0, len(titulos)):
        d = {}
        d["titulo"] = titulos[x].text
        try:
            d['valor'] = precos[x]
        except:
            print(precos)
            print(titulos)
        result.append(d)

    data[t[y]] = result

obj = open('data.json', 'w+')
obj.write(json.dumps(data))
obj.close

