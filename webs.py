from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/Users/jesi/anaconda3/chromedriver")

cars = []  #List to store name of the product
prices = []  #List to store price of the product
links = []  #List to store rating of the product
driver.get("https://www.coches.com/coches-nuevos/Renault/")

content = driver.page_source
soup = BeautifulSoup(content, features="lxml")


for r in soup.findAll(attrs={'class':'cc_new_card_result'}):
    name = r.find('span', attrs={'class':'cc_make_model'}).text
    price = r.find('span', attrs={'class':'cc_new_price'}).text

    cars.append(name)
    prices.append(price)
