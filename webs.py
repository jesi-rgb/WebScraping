from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import pandas as pd

chrome_options = Options()
chrome_options.set_headless(headless=True)

driver = webdriver.Chrome("/Users/jesi/anaconda3/chromedriver",
                          options=chrome_options)

marcas = ['Renault/', 'Seat/', 'Toyota/', 'Volkswagen/', 'Ford/']

cars = []
prices = []
links = []
full_links = []

for m in marcas:
    driver.get("https://www.coches.com/coches-nuevos/" + m)
    content = driver.page_source

    soup = BeautifulSoup(content, features="lxml")

    for r in soup.find_all(attrs={'class': 'cc_new_card_result'}):
        link = r.find('a', attrs={'class': 'cc_icon_link'})['href']
        links.append(link)

for l in links:
    driver = webdriver.Chrome("/Users/jesi/anaconda3/chromedriver",
                              options=chrome_options)
    driver.get(l)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")

    price_list = soup.find_all('div', attrs={'class': 'cc_prices_list'})

    for p in price_list:
        link_list = p.find_all('td', attrs={'class': 'cc_col col_6'})
        for e in link_list:
            link = e.find('a')['href']
            full_links.append(link)

for l in full_links:
    driver = webdriver.Chrome("/Users/jesi/anaconda3/chromedriver",
                              options=chrome_options)
    driver.get(l)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")

    nombre = soup.find('span', attrs={'class': 'cc_principal'}).text
    precio = soup.find('div', attrs={'class': 'cc_coches_price'}).text

    cars.append(nombre)
    prices.append(precio)

    div_prestaciones = soup.find('div', attrs={'class': 'cc_performance'})

    lista_prestaciones = div_prestaciones.find_all('span',
                                                   attrs={'class': 'cc_data'})

    for p in lista_prestaciones:
        categoria = p.find_all('span', attrs={'class': 'cc_label'})
        valor = p.find_all('strong')
        for elem in categoria:
            print(elem.text)
        for elem in valor:
            print(elem.text)
