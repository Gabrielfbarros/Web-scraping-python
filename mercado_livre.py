
# > EXEMPLO
# - Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup
from time import sleep

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')
sleep(2)
produtos = site.find_all('div', attrs={'class': 'poly-card poly-card--list'})

for produto in produtos:
    titulo = produto.find('h3', attrs={'class': 'poly-component__title-wrapper'})
    link = produto.find('a', attrs={'class': 'poly-component__title'})
    real = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
    centavos = produto.find('span', attrs={'class': 'andes-money-amount__cents'})

    # print(produtos.prettify())
    print('Título do produto:', titulo.text)
    print('Link do produto:', link ['href'])
    
    if (centavos): 
        print('Preço do produto: R$ ', real.text + ',' + centavos.text)
    else:
        print('Preço do produto: R$ ', real.text)

    print('\n\n')

