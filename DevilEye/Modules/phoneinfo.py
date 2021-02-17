import requests , bs4
import terminaltables
import colorama
from colorama import *
from terminaltables import SingleTable
from bs4 import BeautifulSoup
def phone():
    number=input('Numbers : ')
    url=('https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui={}&univers=annuaireinverse&idOu='.format(number))
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
    number=soup.find_all('div', {'class':'tel-zone noTrad'})
    name=soup.find_all('a',{'class':'denomination-links pj-lb pj-link'})
    address=soup.find_all('div',{'class':'adresse-container noTrad'})

    number2   = []
    name2     = []
    address2  = []
    if number is not None:
        for nnumber in number:
            number2.append(nnumber.text.strip())
    if name is not None:
        for nname in name:
            name2.append(nname.text.strip())
    if address is not None:
        for naddress in address:
            address2.append(naddress.text.strip())
    regroup = zip(number2,name2,address2)
    TABLE_DATA = [('Number(s)','Name(s)','Addresse(s)')]
    table = SingleTable(TABLE_DATA, title=f"{Fore.YELLOW}Numbers/Names/Adresses {Fore.RESET}")

    listeInfos = []

    for infos in regroup:
        try:
            TABLE_DATA.append(infos)
        except AttributeError:
            pass
    print("\r")
    print(table.table)
