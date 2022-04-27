from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as soup

opt = webdriver.ChromeOptions()
opt.add_argument('headless')

driver = webdriver.Chrome() #create driver
url = 'http://www.eppo.go.th/epposite/templates/eppo_v15_mixed/eppo_oil/eppo_oil_gen_new.php'
driver.get(url) #open web
#time.sleep(3)
page_html = driver.page_source
driver.close()
data = soup(page_html,'html.parser') #scan data
table = data.findAll('div',{'class':'div_oil_price'})
todayprice = table[0].findAll('div',{'class':'oil_price_colum'})
#table2 = table[0].findAll('div')
#row = table2[0].findAll('div',{'class':'oil_price_colum_name_odd'})
#print(todayprice)

oilTitle = ['PPT','Bangchak','Shell','Esso','Caltrex','IRPC','PT'
            ,'Susco','Pure','SuscoDealer']
oilprice = []
for ol in todayprice:
    oilprice.append(ol.text)

#print(oilprice)

result = {}
for t,o in zip(oilTitle,oilprice):
    result[t] = o


print('Gasoline95 : ', result)

