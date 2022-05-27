from asyncio import events
from contextlib import AsyncContextDecorator
from dataclasses import asdict
from email import message
from mmap import ACCESS_DEFAULT
from multiprocessing import Event
import random
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
import threading
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

driver = webdriver.Chrome(options=opt)  # create driver
url = 'http://www.eppo.go.th/epposite/templates/eppo_v15_mixed/eppo_oil/eppo_oil_gen_new.php'
driver.get(url)  # open web
page_html = driver.page_source
driver.close()


data = soup(page_html, 'html.parser')  # scan data
table = data.findAll('div', {'class': 'div_oil_price'})
todayprice = table[0].findAll('div', {'class': 'oil_price_colum'})

oilType = ('Gasoline95', 'Gasohol95', 'Gasohol91', 'GasoholE20',
        'GasoholE85', 'DieselB7', 'Diesel', 'DieselB20', 'B7PremiumDiesel', 'Date')
oilDealer = ('PTT', 'Bangchak', 'Shell', 'Esso', 'Caltrex',
        'IRPC', 'PT', 'Susco', 'Pure', 'SuscoDealer')
oilPrice = []

for ol in todayprice:
    oilPrice.append(ol.text)

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

Gasoline95 = {oilType[0]:{oilDealer[0]:oilPrice[0],oilDealer[1]:oilPrice[1],oilDealer[2]:oilPrice[2],oilDealer[3]:oilPrice[3],oilDealer[4]:oilPrice[4],oilDealer[5]:oilPrice[5]
,oilDealer[6]:oilPrice[6],oilDealer[7]:oilPrice[7],oilDealer[8]:oilPrice[8],oilDealer[9]:oilPrice[9]}}
# print(Gasoline95.copy())

        
Gasohol95 = {oilType[1]:{oilDealer[0]:oilPrice[10],oilDealer[1]:oilPrice[11],oilDealer[2]:oilPrice[12],oilDealer[3]:oilPrice[13],oilDealer[4]:oilPrice[14],oilDealer[5]:oilPrice[15]
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


name = ""
account_data = ""
petch = ""
if petch=="":
        petch = "0198435805\nkbank\nThachchai Jantarawiwat"

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

def run_continuously(interval=1):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

#Local Server or Thai time zone
#schedule.every().day.at("17:00").do(sendEachPrice)
#schedule.every().day.at("05:00").do(sendEachPrice)
#schedule.every().day.at("17:15").do(sendEachPrice)

#For Heroku Server (timezone)
# schedule.every().day.at("00:00").do(sendEachPrice)

schedule.every().day.at("10:00").do(sendEachPrice)

sendEachPrice()
# Start the background thread
stop_run_continuously = run_continuously()


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

                # typerId = payload['events'][0]['source']['userId']
                # print(typerId)
                # typerProfile = line_bot_api.get_profile(typerId)
                # typerName = typerProfile.display_name
                # print(typerName) 

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

biggroupId = "Ced6a903720e8fa345b7ca2bfa34fef09"
petchGroup = 'C9242e9cb7ca747d8e1f04a4dbf0e22db'
petchTarGroup = 'C1e51478d951eb26967b2ebc7402002fa'
#Petch's profile
#from bot's friend
profilePetch = line_bot_api.get_profile('U549838cc9a6ab9747c837176294e02c4')
petch_display_name = profilePetch.display_name

#Petch's 2 profile # for testing
profilePetch2 = line_bot_api.get_group_member_profile(petchGroup,'U0f9012096be57e23da3ebfc35d3136f9')
petch2_display_name = profilePetch2.display_name

#Tar's profile
#from group of 3 members
profileTar = line_bot_api.get_group_member_profile(biggroupId,'U29a01915d9a1ef87954b227582cd37ce')
tar_display_name = profileTar.display_name

#Fai's

#Toy's
profileToy = line_bot_api.get_group_member_profile(biggroupId,'U4d3384c0799063c9623ec368d2a0908d')
toy_display_name = profileToy.display_name

#Que's
profileQue = line_bot_api.get_group_member_profile(biggroupId,'U31c15b54f58407eb63f2ce8c508939ba')
que_display_name = profileQue.display_name

#Mon's
profileMon = line_bot_api.get_group_member_profile('Ced6a903720e8fa345b7ca2bfa34fef09','U549838cc9a6ab9747c837176294e02c4')
mon_display_name = profileMon.display_name

#Gong's 

#Jame's
profileJame = line_bot_api.get_group_member_profile(biggroupId,'U64f2a07ce60ef7e7f94056411af7237e')
jame_display_name = profileJame.display_name

#Hack's

#Poat's

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
        payload = request.json
        messageText = payload['events'][0]['message']['text']
        # typerId = payload['events'][0]['source']['userId']
        # typerProfile = line_bot_api.get_profile(typerId)
        # typerName = typerProfile.display_name

        if '!heroku' in messageText.lower():
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage('https://fathomless-garden-59642.herokuapp.com/callback'))
        elif '!date' in messageText.lower():
                jsonDate = json.dumps(Date,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonDate.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!e20' in messageText.lower() or '!gasohole20' in messageText.lower():
                jsonGasoholE20 = json.dumps(GasoholE20,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonGasoholE20.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!e85' in messageText.lower() or '!gasohole85' in messageText.lower() :
                jsonGasoholE85 = json.dumps(GasoholE85,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonGasoholE85.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!g95' in messageText.lower() or '!gas95' in messageText.lower():
                g95 = Gasoline95.copy()
                {g95.update(Gasohol95)}
                jsonG95 = json.dumps(g95,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonG95.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!g91' in messageText.lower() or '!gasohol91' in messageText.lower() or '!gas91' in messageText.lower() or '!91' in messageText.lower():
                jsonGasohol91 = json.dumps(Gasohol91,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonGasohol91.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif messageText.lower()=='!diesel' or messageText.lower()=='!d':
                jsonDiesel = json.dumps(Diesel,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonDiesel.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!dieselb7' in messageText.lower() or '!db7' in messageText.lower() or '!b7' in messageText.lower():
                jsonDieselB7 = json.dumps(DieselB7,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonDieselB7.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!dieselb20' in messageText.lower() or '!db20' in messageText.lower() or '!b20' in messageText.lower(): 
                jsonDieselB20 = json.dumps(DieselB20,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonDieselB20.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!dieselpremium' in messageText.lower() or '!dp' in messageText.lower(): 
                jsonDieselPremium = json.dumps(DieselPremium,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonDieselPremium.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))        
        elif '!e10' in messageText.lower() or 'gasohole10' in messageText.lower():
                e10 = Gasohol95.copy()
                {e10.update(Gasohol91)}
                jsonGasohol95 = json.dumps(Gasohol95,indent=1)
                jsonGasohol91 = json.dumps(Gasohol91,indent=1)
                jsonE10 = json.dumps(e10,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonE10.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
                # TextSendMessage(jsonGasohol95[1:14].replace("{","").replace("}","").replace('"',"").replace(",","").strip()+
                # "\t\t\t\t\t\t\t\t\t\t\t\t"+jsonGasohol91[1:14].replace("{","").replace("}","").replace('"',"").replace(",","").strip()+
                # "\n"+jsonGasohol95[15:33].replace("{","").replace("}","").replace('"',"").replace(",","").strip()+
                # "\t\t\t\t\t\t\t\t\t\t\t\t\t"+jsonGasohol91[15:33].replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!gasohol95' in messageText.lower() or '!95' in messageText.lower():
                jsonGasohol95 = json.dumps(Gasohol95,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonGasohol95.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!gasoline95' in messageText.lower() or '!e0' in messageText.lower():
                jsonGasoline95 = json.dumps(Gasoline95,indent=1)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(jsonGasoline95.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!getall' in messageText.lower():
                getAll = Gasoline95.copy()
                {getAll.update(Gasohol95)}
                getAll = getAll.copy()
                {getAll.update(Gasohol91)}
                getAll = getAll.copy()
                {getAll.update(GasoholE20)}
                getAll = getAll.copy()
                {getAll.update(GasoholE85)}
                getAll = getAll.copy()
                {getAll.update(Diesel)}
                getAll = getAll.copy()
                {getAll.update(DieselB7)}
                getAll = getAll.copy()
                {getAll.update(DieselB20)}
                getAll = getAll.copy()
                {getAll.update(DieselPremium)}
                getAll = getAll.copy()
                {getAll.update(Date)}
                jsonGetAll = json.dumps(getAll,indent=1)
                line_bot_api.reply_message(event.reply_token,TextSendMessage(jsonGetAll.replace("{","").replace("}","").replace('"',"").replace(",","").strip()))
        elif '!petch' in messageText.lower() or '!เพชร' in messageText or '@'+petch_display_name+' ขอเลข' in messageText or '@'+petch2_display_name+' ขอเลข':                
                line_bot_api.reply_message(event.reply_token,TextSendMessage(petch))
        elif '!ton' in messageText.lower() or '!ต้น' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("0922616652\npromptpay\nSarannon Srinarongsuk"))
        elif '!toy' in messageText.lower() or '!ทอย' in messageText or '@'+toy_display_name+' ขอเลข' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("2242567291\nTTB\nChutikarn Khampee"))
        elif '!jame' in messageText.lower() or '!เจม' in messageText or '@'+jame_display_name+' ขอเลข' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("0273461043\nkbank\nChaiyanat Noodang"))
        elif '!poat' in messageText.lower() or '!โป๊ต' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("0018398265\nkbank\nNarathip Thongprathun"))
        elif '!bell' in messageText.lower() or '!เบล' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("4300831278\nSCB\nNoppon Meta-awirutruedee"))
        elif '!mon' in messageText.lower() or '!มน' in messageText or '@'+mon_display_name+' ขอเลข' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("0880203451\npromptpay\nPongsakorn Isarapatthanakul"))
        elif '!tar' in messageText.lower() or '!ต้า' in messageText or '@'+tar_display_name+' ขอเลข' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("0802805977\npromptpay\nPatchamon Monwimonporn"))
        elif '!fai' in messageText.lower() or '!ฝ้าย' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("0658068512\nkbank\nNalinee Boonrueng"))
        elif '!que' in messageText.lower() or '!คิว' in messageText or '@'+que_display_name+' ขอเลข' in messageText:
                line_bot_api.reply_message(event.reply_token,TextSendMessage("0944412122\npromptpay\nChanin Taweeluthikunchai"))
        elif '!help' in messageText.lower():
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage("!account_help\n!gas_help"))     
        elif '!account_help' in messageText.lower():
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage("พิมพ์ '!<ชื่อคน>' ที่ต้องการเพื่อแสดงเลขบัญชี เช่น !มน หรือ !petch"))
        elif '!gas_help' in messageText.lower():
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage("พิมพ์ '!<ชื่อน้ำมัน>' ที่ต้องการเพื่อแสดงราคาของแต่ละปั๊ม เช่น !e20 หรือ !91 หรือ !diesel"))
        elif '!edit_help' in messageText.lower():
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage("พิมพ์ '!edit_<ชื่อคน>_<ข้อมูล>' ที่ต้องการเพื่อทำการแก้ไขข้อมูลที่จะแสดง เช่น !edit_มน_0880203451 หรือ !petch"))
        # elif '!edit_petch_' in messageText.lower() or '!edit_เพชร_' in messageText.lower():
        #         edit_petch()
        #         line_bot_api.reply_message(event.reply_token,
        #         TextSendMessage(editObject))
        elif '!edit_'+name+'_' in messageText.lower():
                edit_data(name)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(editResponse))
        elif '!add_' in messageText.lower():
                add_name()
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(addResponse))
        elif '!remove_'+name in messageText.lower():
                remove_name(name)
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(removeResponse))
        elif '!'+name in messageText.lower():
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(editObject))
        elif '!print_name' in messageText.lower():
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(name))
        elif 'มีซีค' in messageText:
                meeseekAns =  ["ครับ","ว่าไง","อะไร","เรียกไมครับ","เรียกหาแม่"]
                meeseekResponse = random.choices(meeseekAns, weights = [1,1,1,1,0.5])
                line_bot_api.reply_message(event.reply_token,
                TextSendMessage(meeseekResponse[0]))

# def edit_petch():
#         payload = request.json
#         messageText = payload['events'][0]['message']['text']
#         global petch
#         global editObject
#         petch = messageText.replace("!edit_petch_","")
#         editObject = "edit successfully!"
#         return petch,editObject
        
def add_name():
        payload = request.json
        messageText = payload['events'][0]['message']['text']
        global addResponse
        global name
        name = messageText.replace("!add_","")
        addResponse = "add "+name+" successfully!"
        print(name)
        return name,addResponse

def edit_data(name):
        payload = request.json
        messageText = payload['events'][0]['message']['text']
        global editObject
        global editResponse
        editObject = "No data found"
        if name=="":
                editResponse = "No name found"                
                return editResponse,editObject
        else:
                editObject = messageText.replace("!edit_"+name+'_',"")
                editResponse = "edit successfully!"
                return editObject,editResponse

def remove_name(name):
        payload = request.json
        messageText = payload['events'][0]['message']['text']
        global removeResponse
        removeResponse = "remove "+name+" successfully!"
        name = ""
        editObject = ""
        return name,removeResponse,editObject

@app.route('/',methods = ['GET'])
def hello():
    return 'hello world',200

# while 1:
        # schedule.run_pending()
        # time.sleep(1500)
        

if __name__ == "__main__":
    app.run()

driver.quit()  # turn off chomedriver console
# os.system("taskkill /im chromedriver.exe") #kill chromedriver process to regain memory
