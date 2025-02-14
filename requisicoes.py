import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias=[]

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#HTML da noticia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    #titulo da noticia
    título = noticia.find('a', attrs={'class': 'feed-post-link'})

    subtítulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})



    #subtitulo span class="feed-post-metadata-section"
    if (subtítulo):
        lista_noticias.append([título.text, subtítulo.text, título['href']])

    else:
        lista_noticias.append([título.text, '', título['href']])

news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

news.to_excel('noticias.xlsx', index=False)
