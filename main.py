import os
import time
import requests
from urllib.request import Request, urlopen
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup as bsp

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
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
        session.headers['User-Agent'] = headers['User-Agent']
        session.trust_env = False
        
        responses = session.get(link.strip(), allow_redirects=False)
        responses.raise_for_status()
        response = responses.text
        
        soup = bsp(response, "html.parser")
        
        print(responses.status_code)
        
        if count == 0:
          price = soup.select_one('.preco_desconto strong')
          
          print(price.text)
          
        elif count == 1:          
          
          price = soup.select_one('#valVista')

          print(price.text)
          
          parse = soup.select_one('.val-parc #valParc')          

          print(parse.text)
          
        elif count == 2:
          
          price = soup.select_one('#priceblock_ourprice')

          print(price.text)
          
        elif count == 3:
          
          price = soup.select_one('.price-boleto span')

          print(price.text)
          
          parse = soup.select_one('#product-price-19108 span')

          print(parse.text)
          
      
      except Exception as e:
        
        print(e)
      
      time.sleep(5)
        