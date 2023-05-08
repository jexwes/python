import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://letterboxd.com/films/popular/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

filmes = []
for filme in soup.find_all("li", class_="listitem"):
    titulo = filme.find("h3", class_="popover-trigger").text.strip()
    ano = filme.find("span", class_="year").text.strip()
    diretor = filme.find("p", class_="text-sluglist").text.strip()
    avaliacao = filme.find("span", class_="rating").text.strip()
    filmes.append({"titulo": titulo, "ano": ano, "diretor": diretor, "avaliacao": avaliacao})

df = pd.DataFrame(filmes)
print(df.head())

