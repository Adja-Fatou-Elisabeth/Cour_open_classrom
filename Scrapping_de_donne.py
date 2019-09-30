from  bs4 import BeautifulSoup
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
import requests
import re

requete = requests.get(url=" ")
page = requete.content
soup = BeautifulSoup(page, "html.parser" )
regex = re.compile(r'[\n\r\t]')

recepette= soup.find("h1", {"class": "main-title"}).string
personne = soup.find("span", {"class": "title-2 recipe-infos__quantity__value"}).string
temp_preparation = soup.find("span", {"class": "recipe-infos__timmings__value"}).get_text()
temp_cuisson = soup.find("span", {"class": "recipe-infos__timmings__value"}).get_text()
list_ingredient = soup.find_all("span", attrs={"class": "ingredient"})
list_utensil= soup.find_all("span", attrs={"class": "recipe-utensil__name"})
etapes_preparation = soup.find_all("li", attrs={"class": "recipe-preparation__list__item"})

def liste_utensil(list_utensil):
    liste=[]
    for i in list_utensil:
        liste.append(str(i.get_text()).strip())
    return liste

def liste_ingredient(list_ingredient):
    liste=[]
    for i in list_ingredient:
        liste.append(i.string)
    return liste

def listes_etapes(etapes_preparation):
    liste=[]
    for e in etapes_preparation:
        r=(e.get_text()).split('		')
        liste.append({"index":r[0][7:],"description":regex.sub("",r[1])})
    return liste


dictionnaire ={
    "nom_recette" :recepette,
    "nombre_personnes" :personne,
    "temps_preparation" :regex.sub(" ",temp_preparation).strip(),
    "temps_cuisson" : regex.sub(" ",temp_cuisson).strip(),
    "list_ingredient" :liste_ingredient(list_ingredient),
    "list_ustensiles" : liste_utensil(list_utensil),
    "etapes_preparation" : listes_etapes(etapes_preparation)
}
print( dictionnaire)
