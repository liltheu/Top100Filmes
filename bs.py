from bs4 import BeautifulSoup
import requests, json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
path = './'
fileName = 'dados'

url = requests.get('https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating')

soup = BeautifulSoup(url.content, 'html.parser')

filmes = soup.findAll('div', {'class':'lister-item mode-advanced'})

dados = []
for filme in filmes:
    titulo = (filme.h3.a.text)
    ano = (filme.find('span', {'class':'lister-item-year text-muted unbold'}).text[1:5])
    nota = (filme.find('div', {'class':'inline-block ratings-imdb-rating'})['data-value'])
    imagem = (filme.find('img', {'class':'loadlate'})['loadlate'])

    dados.append({
      'titulo': titulo,
      'imagem': imagem,
      'ano': ano,
      'nota': nota
    })
writeToJSONFile(path, fileName, dados)