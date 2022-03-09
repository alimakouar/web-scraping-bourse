import requests
from bs4 import BeautifulSoup
import pandas as pd

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

indice=['MASI','MADEX','STOCKS','CASRIGHTS']
performance=['UP','DOWN','QTY','CAP']
period=['DAY_1','DAY_1_PREVIOUS','WEEK_1','MONTH_1','MONTH_3','MONTH_6','WEEK_52','YEAR']
palmareslist = []