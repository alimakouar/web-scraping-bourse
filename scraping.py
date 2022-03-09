import requests
from bs4 import BeautifulSoup
import pandas as pd

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

indice=['MASI','MADEX','STOCKS','CASRIGHTS']
performance=['UP','DOWN','QTY','CAP']
period=['DAY_1','DAY_1_PREVIOUS','WEEK_1','MONTH_1','MONTH_3','MONTH_6','WEEK_52','YEAR']
palmareslist = []

def getinfo(indice,performance,period):
    url=f'https://www.cdgcapitalbourse.ma/bourse/palmaresaction/{indice}/{performance}/{period}'
    print('l\'url est',url)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser" )
    try:
        palmares = soup.find('table',{'class':'t-data-grid'}).find('tbody').find_all('tr')
        for item in palmares:
            palmare = {
            'Libellé' : item.find('td',{'class':'longName'}).text,
            'Type' : item.find('td',{'class':'instrumentType'}).text,
            'État' : item.find('td',{'class':'quotationState'}).text,
            'Cours' : item.find('td',{'class':'lastPrice'}).text,
            'Qté cumulée' : item.find('td',{'class':'rankingCumulatedVolume'}).text,
            'Volume cumulé' : item.find('td',{'class':'rankingTurnOver'}).text,
            'Capitalisation' : item.find('td',{'class':'capitalisation'}).text,
            'Var.(%)' : item.find('td',{'class':'rankingVariation'}).text,
            'Date' : item.find('td',{'class':'lastPriceDateTime'}).text,
            'indice': soup.find('option',{'value':indice}).text,
            'performance': soup.find('option',{'value':performance}).text,
            'period': soup.find('option',{'value':period}).text,
            }
            palmareslist.append(palmare)
        df = pd.DataFrame(palmareslist)
        print(df.head())
        df.to_excel('bourse.xlsx', index=False)
    except:
        print('la page est vide')

getinfo('MASI','UP','DAY_1')
getinfo('MADEX','DOWN','WEEK_1')

print('finished')