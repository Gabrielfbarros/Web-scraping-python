# 🕷️ Web Scraping com Python: G1 e Mercado Livre

Este repositório contém scripts de **Web Scraping** desenvolvidos em Python para extrair dados de portais de notícias e e-commerce de forma automatizada.

O projeto demonstra como realizar requisições HTTP, analisar o HTML (parsing), manipular dados com Pandas e interagir com o usuário via terminal.

## 🚀 Funcionalidades

O projeto é dividido em dois módulos principais:

### 1. Extrator de Notícias (G1)
Arquivo: `requisicoes.py`
* Conecta-se à página inicial do portal G1.
* Extrai as manchetes principais (**Título**, **Subtítulo** e **Link**).
* Trata casos onde o subtítulo não existe.
* **Exportação:** Salva os dados organizados automaticamente em um arquivo Excel (`noticias.xlsx`).

### 2. Buscador de Produtos (Mercado Livre)
Arquivo: `mercado_livre.py`
* Solicita ao usuário qual produto deseja buscar.
* Realiza a busca na URL do Mercado Livre.
* Extrai informações dos cards de produtos:
    * Título do anúncio.
    * Link direto.
    * Preço (tratando separação de reais e centavos).
* **Output:** Exibe os resultados formatados diretamente no terminal.

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/)**
* **[Requests](https://pypi.org/project/requests/)**: Para realizar as chamadas HTTP.
* **[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)**: Para fazer o parsing do HTML e navegar pela árvore do DOM.
* **[Pandas](https://pandas.pydata.org/)**: Para estruturação dos dados e exportação para Excel.

## 📦 Pré-requisitos e Instalação

Para rodar este projeto, você precisará ter o Python instalado. Recomenda-se também instalar as bibliotecas necessárias.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Gabrielfbarros/web-scraping-python.git](https://github.com/Gabrielfbarros/web-scraping-python.git)
   cd nome-do-repo

## 🚀 Melhorias Futuras

* [ ] Adicionar tratamento de erros (Try/Except) caso o site mude a estrutura ou fique offline.
* [ ] Exportar os dados do Mercado Livre também para Excel/CSV.
* [ ] Criar uma interface gráfica simples com Tkinter ou Streamlit.
* [ ] Implementar paginação (buscar produtos em mais de uma página).

## 🤝 Autor

Desenvolvido por **Gabriel Barros**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabrielfonsecab/)
