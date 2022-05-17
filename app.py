from asyncio import events
from contextlib import AsyncContextDecorator
from dataclasses import asdict
from email import message
from mmap import ACCESS_DEFAULT
from multiprocessing import Event
from telnetlib import GA
from unicodedata import decomposition
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
from bs4 import BeautifulSoup as soup
import os
from collections import defaultdict
from flask import Flask, request, abort
import requests
import json
import errno
import os
import sys
import tempfile
from argparse import ArgumentParser
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler,WebhookPayload
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,)
    



opt = webdriver.ChromeOptions()
opt.add_argument('headless')
# opt.add_experimental_option('excludeSwitches',['enable-logging'])

driver = webdriver.Chrome(options=opt)  # create driver
url = 'http://www.eppo.go.th/epposite/templates/eppo_v15_mixed/eppo_oil/eppo_oil_gen_new.php'
driver.get(url)  # open web
# time.sleep(3)
page_html = driver.page_source
driver.close()


data = soup(page_html, 'html.parser')  # scan data
table = data.findAll('div', {'class': 'div_oil_price'})
todayprice = table[0].findAll('div', {'class': 'oil_price_colum'})
#table2 = table[0].findAll('div')
#row = table2[0].findAll('div',{'class':'oil_price_colum_name_odd'})
# print(todayprice)

oilType = ('Gasoline95', 'Gasohol95', 'Gasohol91', 'GasoholE20',
        'GasoholE85', 'DieselB7', 'Diesel', 'DieselB20', 'B7PremiumDiesel', 'Date')
oilType2 = ['Gasoline95', 'Gasohol95', 'Gasohol91', 'GasoholE20',
        'GasoholE85', 'DieselB7', 'Diesel', 'DieselB20', 'B7PremiumDiesel', 'Date']
oilDealer = ('PTT', 'Bangchak', 'Shell', 'Esso', 'Caltrex',
        'IRPC', 'PT', 'Susco', 'Pure', 'SuscoDealer')
oilPrice = []

for ol in todayprice:
    oilPrice.append(ol.text)

# print("Oil Price\t\t: ",oilPrice)
# print("Oil Dealer\t: ",oilDealer)
# print("Oil Type\t\t: ",oilType)
# print(type(oilPrice))
# print(type('Bangchak'))
# print(oilDealer)

# print(oilType[0])


# result = {}

# result = {oilType[0]: {oilDealer[0]: oilPrice[0], oilDealer[1]: oilPrice[1], oilDealer[2]: oilPrice[2], oilDealer[3]: oilPrice[3], oilDealer[4]: oilPrice[4], 
#         oilDealer[5]: oilPrice[5], oilDealer[6]: oilPrice[6], oilDealer[7]: oilPrice[7], oilDealer[8]: oilPrice[8], oilDealer[9]: oilPrice[9]},
#         oilType[1]: {oilDealer[0]: oilPrice[10], oilDealer[1]: oilPrice[11], oilDealer[2]: oilPrice[12], oilDealer[3]: oilPrice[13], oilDealer[4]: oilPrice[14],
#         oilDealer[5]: oilPrice[15], oilDealer[6]: oilPrice[16], oilDealer[7]: oilPrice[17], oilDealer[8]: oilPrice[18], oilDealer[9]: oilPrice[19]},
#         oilType[2]: {oilDealer[0]: oilPrice[20], oilDealer[1]: oilPrice[21], oilDealer[2]: oilPrice[22], oilDealer[3]: oilPrice[23], oilDealer[4]: oilPrice[24],
#         oilDealer[5]: oilPrice[25], oilDealer[6]: oilPrice[26], oilDealer[7]: oilPrice[27], oilDealer[8]: oilPrice[28], oilDealer[9]: oilPrice[29]},
#         oilType[3]: {oilDealer[0]: oilPrice[30], oilDealer[1]: oilPrice[31], oilDealer[2]: oilPrice[32], oilDealer[3]: oilPrice[33], oilDealer[4]: oilPrice[34],
#         oilDealer[5]: oilPrice[35], oilDealer[6]: oilPrice[36], oilDealer[7]: oilPrice[37], oilDealer[8]: oilPrice[38], oilDealer[9]: oilPrice[39]},
#         oilType[4]: {oilDealer[0]: oilPrice[40], oilDealer[1]: oilPrice[41], oilDealer[2]: oilPrice[42], oilDealer[3]: oilPrice[43], oilDealer[4]: oilPrice[44],
#         oilDealer[5]: oilPrice[45], oilDealer[6]: oilPrice[46], oilDealer[7]: oilPrice[47], oilDealer[8]: oilPrice[48], oilDealer[9]: oilPrice[49]},
#         oilType[5]: {oilDealer[0]: oilPrice[50], oilDealer[1]: oilPrice[51], oilDealer[2]: oilPrice[52], oilDealer[3]: oilPrice[53], oilDealer[4]: oilPrice[54],
#         oilDealer[5]: oilPrice[55], oilDealer[6]: oilPrice[56], oilDealer[7]: oilPrice[57], oilDealer[8]: oilPrice[58], oilDealer[9]: oilPrice[59]},
#         oilType[6]: {oilDealer[0]: oilPrice[60], oilDealer[1]: oilPrice[61], oilDealer[2]: oilPrice[62], oilDealer[3]: oilPrice[63], oilDealer[4]: oilPrice[64],
#         oilDealer[5]: oilPrice[65], oilDealer[6]: oilPrice[66], oilDealer[7]: oilPrice[67], oilDealer[8]: oilPrice[68], oilDealer[9]: oilPrice[69]},
#         oilType[7]: {oilDealer[0]: oilPrice[70], oilDealer[1]: oilPrice[71], oilDealer[2]: oilPrice[72], oilDealer[3]: oilPrice[73], oilDealer[4]: oilPrice[74],
#         oilDealer[5]: oilPrice[75], oilDealer[6]: oilPrice[76], oilDealer[7]: oilPrice[77], oilDealer[8]: oilPrice[78], oilDealer[9]: oilPrice[79]},
#         oilType[8]: {oilDealer[0]: oilPrice[80], oilDealer[1]: oilPrice[81], oilDealer[2]: oilPrice[82], oilDealer[3]: oilPrice[83], oilDealer[4]: oilPrice[84],
#         oilDealer[5]: oilPrice[85], oilDealer[6]: oilPrice[86], oilDealer[7]: oilPrice[87], oilDealer[8]: oilPrice[88], oilDealer[9]: oilPrice[89]},
#         oilType[9]: {oilDealer[0]: oilPrice[90], oilDealer[1]: oilPrice[91], oilDealer[2]: oilPrice[92], oilDealer[3]: oilPrice[93], oilDealer[4]: oilPrice[94],
#         oilDealer[5]: oilPrice[95], oilDealer[6]: oilPrice[96], oilDealer[7]: oilPrice[97], oilDealer[8]: oilPrice[98], oilDealer[9]: oilPrice[99]}}

# print(result.get("GasoholE20"))
# print(result.items())
# print(result.values())

# result2={}
# result2 = {oilType[0]:{oilDealer[0]:oilPrice[0]}}

# print(result2)

Gasoline95 = {}
Gasohol95 = {}
Gasohol91 = {}
GasoholE20 = {}
GasoholE85 = {}
DieselB7 = {}
Diesel = {}
DieselB20 = {}
DieselPremium = {}
Date = {}

Gasoline95 = {oilType2[0]:{oilDealer[0]:oilPrice[0],oilDealer[1]:oilPrice[1],oilDealer[2]:oilPrice[2],oilDealer[3]:oilPrice[3],oilDealer[4]:oilPrice[4],oilDealer[5]:oilPrice[5]
,oilDealer[6]:oilPrice[6],oilDealer[7]:oilPrice[7],oilDealer[8]:oilPrice[8],oilDealer[9]:oilPrice[9]}}
# print(Gasoline95.copy())

        
Gasohol95 = {oilType2[1]:{oilDealer[0]:oilPrice[10],oilDealer[1]:oilPrice[11],oilDealer[2]:oilPrice[12],oilDealer[3]:oilPrice[13],oilDealer[4]:oilPrice[14],oilDealer[5]:oilPrice[15]
,oilDealer[6]:oilPrice[16],oilDealer[7]:oilPrice[17],oilDealer[8]:oilPrice[18],oilDealer[9]:oilPrice[19]}}
# print(Gasohol95.copy())

y=0
z=20        
Gasohol91 = {oilDealer[y]:oilPrice[z]}
while(z<30):
        Gasohol91.update({oilDealer[y]:oilPrice[z]})  
        z += 1        
        y += 1        
Gasohol91 = {"Gasohol91":Gasohol91}
# print(Gasohol91.copy())

y=0
z=30        
GasoholE20 = {oilDealer[y]:oilPrice[z]}
while(z<40):
        GasoholE20.update({oilDealer[y]:oilPrice[z]})
        z += 1
        y += 1
GasoholE20 = {"GasoholE20":GasoholE20}
# print(GasoholE20.copy())

y=0
z=40        
while(z<50):
        GasoholE85.update({oilDealer[y]:oilPrice[z]})
        y += 1
        z += 1
GasoholE85 = {"GasoholE85":GasoholE85}
# print(GasoholE85.copy())

y=0
z=50        
while(z<60):
        DieselB7.update({oilDealer[y]:oilPrice[z]})
        y += 1
        z += 1
DieselB7={"DieselB7":DieselB7}
# print(DieselB7.copy())

y=0
z=60        
while(z<70):
        Diesel.update({oilDealer[y]:oilPrice[z]})
        y += 1
        z += 1
Diesel = {"Diesel":Diesel}
# print(Diesel.copy())

y=0
z=70        
while(z<80):
        DieselB20.update({oilDealer[y]:oilPrice[z]})
        y += 1
        z += 1
DieselB20={"DieselB20":DieselB20}
# print(DieselB20.copy())

y=0
z=80        
while(z<90):
        DieselPremium.update({oilDealer[y]:oilPrice[z]})
        y += 1
        z += 1
DieselPremium={"DieselPremium":DieselPremium}
# print(DieselPremium.copy())


y=0
z=90        
while(z<100):
        Date.update({oilDealer[y]:oilPrice[z]})
        y += 1
        z += 1
Date={"Date":Date}
# print(Date.copy())

# g95 = {}
# g95 = Gasoline95.copy()
# g95.update(Gasohol95)
# print(Gasoline95)
# print(g95)


from songline import Sendline

# line_notify_token
token = 'gcRCdottKStR05Fat7hNJBPNa4NniPK2Prw5NUoBM9q'

messenger = Sendline(token)

# messenger.sendtext(result.items())

def sendEachPrice():
        messenger.sendtext(Date.items())
        messenger.sendtext(Gasoline95.items())
        messenger.sendtext(Gasohol95.items())
        messenger.sendtext(Gasohol91.items())
        messenger.sendtext(GasoholE20.items())
        messenger.sendtext(GasoholE85.items())
        messenger.sendtext(DieselB7.items())
        messenger.sendtext(Diesel.items())
        messenger.sendtext(DieselB20.items())
        messenger.sendtext(DieselPremium.items())

# line_bot_token
lineBotApi = 'PTbNtC5m+gVfsYzvhp8dBtjkUiwd8jxyv7kxS4RlJpNIunDdedUN0sNXZFtVIB9p0TdLZ5hc50Ax8WskZo3DTceVUBKmRZvVfgK7lR6GmDPDy194G+bjvSWhFru0j4qzC1yc0PK7DaLnPbT75oxR6gdB04t89/1O/w1cDnyilFU='
lineBotSecret = '15a350c50da2fc05413dda6fd9eff8f9'

line_bot_api = LineBotApi(lineBotApi)
handler = WebhookHandler(lineBotSecret)

# sendEachPrice()
# def job():
#     print("I'm working...")

# schedule.every(3).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)


app = Flask(__name__)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    payload = request.json
    print(payload)

    # make verification on LineDev to success when there is no event(verifying will send an empty event)
    if (payload['events'])!=([]):
        if(payload['events'][0]['message']['type']=='text'):
                messageText = payload['events'][0]['message']['text'] 
                print(messageText) 
                print(payload['events'][0]['message']['type'])
                print(type(payload['events'][0]['message']['type']))

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
        payload = request.json
        messageText = payload['events'][0]['message']['text']    
        if '!e20' in messageText.lower() or '!gasohole20' in messageText.lower():
                jsonGasoholE20 = json.dumps(GasoholE20)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonGasoholE20))
        elif '!e85' in messageText.lower() or '!gasohole85' in messageText.lower() :
                jsonGasoholE85 = json.dumps(GasoholE85)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonGasoholE85))
        elif '!g95' in messageText.lower() or '!gas95' in messageText.lower():
                g95 = Gasoline95.copy()
                {g95.update(Gasohol95)}
                jsonG95 = json.dumps(g95)
                line_bot_api.reply_message(event.reply_token,TextSendMessage(jsonG95))
        elif '!g91' in messageText.lower() or '!gasohol91' in messageText.lower() or '!gas91' in messageText.lower() or '!91' in messageText.lower():
                jsonGasohol91 = json.dumps(Gasohol91)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonGasohol91))
        elif messageText.lower()=='!diesel' or messageText.lower()=='!d':
                jsonDiesel = json.dumps(Diesel)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonDiesel))
        elif '!dieselb7' in messageText.lower() or '!db7' in messageText.lower():
                jsonDieselB7 = json.dumps(DieselB7)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonDieselB7))
        elif '!dieselb20' in messageText.lower() or '!db20' in messageText.lower():
                jsonDieselB20 = json.dumps(DieselB20)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonDieselB20))
        elif '!dieselpremium' in messageText.lower() or '!dpremium' in messageText.lower():
                jsonDieselPremium = json.dumps(DieselPremium)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonDieselPremium))        
        elif '!e10' in messageText.lower() or 'gasohole10' in messageText.lower():
                e10 = Gasohol95.copy()
                {e10.update(Gasohol91)}
                jsonE10 = json.dumps(e10)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonE10))
        elif '!gasohol95' in messageText.lower() or '!95' in messageText.lower():
                jsonGasohol95 = json.dumps(Gasohol95)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonGasohol95))
        elif '!gasoline95' in messageText.lower() or '!e0' in messageText.lower():
                jsonGasoline95 = json.dumps(Gasoline95)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonGasoline95))
        elif '!petch' in messageText.lower() or '!เพชร' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("0198435805\nkbank\nThachchai Jantarawiwat"))
        elif '!ton' in messageText.lower() or '!ต้น' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("0922616652\npromptpay\nSarannon Srinarongsuk"))
        

@app.route('/',methods = ['GET'])
def hello():
    return 'hello world',200

def ReplyMessage(Reply_token, TextMessage, Line_Access_Token):
        LINE_API = 'https://api.line.me/v2/bot/messsage/reply'

        Authorization = 'Bearer {}'.format(lineBotApi)
        print(Authorization)
        headers = {
                'Content-Type': 'application/json; charset=UTF-8',
                'Authorization':Authorization
        }

        data = {
                "replyToken":Reply_token,
                "messages":[{
                        "type":"text",
                        "text":TextMessage
                }]
        }

        data = json.dumps(data) ## dump dict >> Json Object
        r = requests.post(LINE_API, headers=headers, data=data)
        return 200


# messenger.sendtext(result.get("GasoholE20").items())
# i=0
# while(i<10):
#     messenger.sendtext(oilType[i])
#     messenger.sendtext(result.get(oilType[i],{}).items())
#     i += 1

# messenger.sticker(12,1)

# bot_info = line_bot_api.get_bot_info()
# print(bot_info.user_id)


schedule.every().day.at("17:00").do(sendEachPrice)
schedule.every().day.at("05:00").do(sendEachPrice)
schedule.every().day.at("17:15").do(sendEachPrice)
# line_bot_api.push_message('',TextSendMessage(sendEachPrice()))

while 1:
     schedule.run_pending()
     time.sleep(1)

if __name__ == "__main__":
    app.run()

driver.quit()  # turn off chomedriver console
# os.system("taskkill /im chromedriver.exe") #kill chromedriver process to regain memory
