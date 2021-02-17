import requests , bs4
import terminaltables
import colorama
from colorama import *
from terminaltables import SingleTable
from bs4 import BeautifulSoup
def name_search():
    Prénom=input('Prénom : ')
    Nom=input('Nom : ')
    localisation=input('Code Postal :')
    url=("https://www.118000.fr/search?label={}&who={}+{}".format(localisation,Prénom,Nom))
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'referrer': 'https://google.com/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8',
    'Accept-Encoding': 'utf-8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache'
    }
    request=requests.get(url,headers=headers)
    page=request.content
    soup=BeautifulSoup(page,'lxml')
    adresse=soup.find_all('div',{'class':"h4 address mtreset"})
    phone=soup.find_all('a',{'class':"clickable atel"})
    name=soup.find_all('h2',{'class':"name title inbl"})

    name2     = []
    adresse2  = []
    phonee2   = []
    if name is not None:
        for nname in name:
            name2.append(nname.text.strip())
    if adresse is not None:
        for nadresse in adresse:
            adresse2.append(nadresse.text.strip())
    if phone is not None:
        for nphone in phone:
            phonee2.append(nphone.text.strip())
    regroup = zip(name2, adresse2,phonee2)
    TABLE_DATA = [('Nom(s)','Adresse(s)','Numero(s)')]
    table = SingleTable(TABLE_DATA, title=f"{Fore.YELLOW}Noms/Adresses/Numeros {Fore.RESET}")

    listeInfos = []

    for infos in regroup:
        try:
            TABLE_DATA.append(infos)
        except AttributeError:
            pass
    print("\r")
    print(table.table)
