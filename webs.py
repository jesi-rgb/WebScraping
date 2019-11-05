from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/Users/jesi/anaconda3/chromedriver")

marcas = ['Renault/', 'Seat/', 'Toyota/', 'Volkswagen/', 'Ford/']

cars = []  #List to store name of the product
prices = []  #List to store price of the product
links = []  #List to store rating of the product

for m in marcas:
    driver.get("https://www.coches.com/coches-nuevos/"+m)
    content = driver.page_source

    soup = BeautifulSoup(content, features="lxml")

    for r in soup.findAll(attrs={'class':'cc_new_card_result'}):
        name = r.find('span', attrs={'class':'cc_make_model'}).text
        price = r.find('span', attrs={'class':'cc_new_price'}).text
        link = r.find('a', attrs={'class':'cc_icon_link'}).href

        cars.append(name)
        prices.append(price)
        links.append(link)

links
