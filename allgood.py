from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as soup
import os

opt = webdriver.ChromeOptions()
opt.add_argument('headless')
# opt.add_experimental_option('excludeSwitches',['enable-logging'])

driver = webdriver.Chrome(options=opt)  # create driver
url = 'http://www.eppo.go.th/epposite/templates/eppo_v15_mixed/eppo_oil/eppo_oil_gen_new.php'
driver.get(url)  # open web
# time.sleep(3)
page_html = driver.page_source
driver.close()
driver.quit()  # turn off chomedriver console

data = soup(page_html, 'html.parser')  # scan data
table = data.findAll('div', {'class': 'div_oil_price'})
todayprice = table[0].findAll('div', {'class': 'oil_price_colum'})
#table2 = table[0].findAll('div')
#row = table2[0].findAll('div',{'class':'oil_price_colum_name_odd'})
# print(todayprice)

oilType = ['Gasoline95', 'Gasohol95', 'Gasohol91', 'GasoholE20',
           'GasoholE85', 'Disel B7', 'Diesel', 'Disel B20', 'B7PremiumDiesel', 'Date']
oilDealer = ['PTT', 'Bangchak', 'Shell', 'Esso', 'Caltrex',
             'IRPC', 'PT', 'Susco', 'Pure', 'SuscoDealer']
# ,'PTT','Bangchak','Shell','Esso','Caltrex','IRPC','PT','Susco','Pure','SuscoDealer'
# ,'PTT','Bangchak','Shell','Esso','Caltrex','IRPC','PT','Susco','Pure','SuscoDealer'
# ,'PTT','Bangchak','Shell','Esso','Caltrex','IRPC','PT','Susco','Pure','SuscoDealer'
# ,'PTT','Bangchak','Shell','Esso','Caltrex','IRPC','PT','Susco','Pure','SuscoDealer'
# ,'PTT','Bangchak','Shell','Esso','Caltrex','IRPC','PT','Susco','Pure','SuscoDealer'
# ,'PTT','Bangchak','Shell','Esso','Caltrex','IRPC','PT','Susco','Pure','SuscoDealer'
# ,'PTT','Bangchak','Shell','Esso','Caltrex','IRPC','PT','Susco','Pure','SuscoDealer'
# ,'PTT','Bangchak','Shell','Esso','Caltrex','IRPC','PT','Susco','Pure','SuscoDealer'
# ,'PTT','Bangchak','Shell','Esso','Caltrex','IRPC','PT','Susco','Pure','SuscoDealer')
oilPrice = []

for ol in todayprice:
    oilPrice.append(ol.text)

# print(oilPrice)
# print(type(oilDealer[1]))
# print(type('Bangchak'))
# print(oilDealer)

# result = {}
# for t,o in zip(oilDealer,oilPrice):
#     result[t] = o
# print(result)


result = {}
t = 0
d = 0
p = 0

result = {oilType[0]: {oilDealer[0]: oilPrice[0], d[1]: p[1], d[2]: p[2], d[3]: p[3], d[4]: p[4], d[5]: p[5], d[6]: p[6], d[7]: p[7], d[8]: p[8], d[9]: p[9]},
          oilType[1]: {oilDealer[0]: oilPrice[10], d[1]: p[11], d[2]: p[12], d[3]: p[13], d[4]: p[14], d[5]: p[15], d[6]: p[16], d[7]: p[17], d[8]: p[18], d[9]: p[19]},}
print(result)



# os.system("taskkill /im chromedriver.exe") #kill chromedriver process to regain memory
