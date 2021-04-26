import os
import time
import requests
from urllib.request import Request, urlopen
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup as bsp

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

if 'links.txt' in os.listdir(ROOT_DIR):
  with open(f'{ROOT_DIR}/links.txt') as f:
    
    links = f.readlines()
    
    for link, count in zip(links, range(len(links))):

      print('\n============================================================\nLink -> %s' % link)
      
      try:
        
        session = requests.Session()
        session.headers = CaseInsensitiveDict(headers)
        # session.max_redirects = 130

        
        if count != 1:
          response = session.get(link, allow_redirects=False)
          response = response.content
          
        else:
          response = urlopen(Request(link, None, headers=headers))
        
        soup = bsp(response, "html.parser")
        
        if count == 0:
          print(soup)
          price = soup.find(class_='preco_desconto')

          print(price.strong.text)
          
        elif count == 1:
          
          price = soup.find(id='valVista')

          print(price.text)
          
          parse = soup.find(class_='val-parc')
          
          parse = parse.find(id='valParc')

          print(parse.text)
          
        elif count == 2:
          
          price = soup.find(id='priceblock_ourprice')

          print(price.text)
          
        elif count == 3:
          
          price = soup.find(class_='price-boleto')

          print(price.span.text)
          
          parse = soup.find(id='product-price-19108')

          print(parse.span.text)
          
      
      except Exception as e:
        
        print(e)
      
      time.sleep(10)
        