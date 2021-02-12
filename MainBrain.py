import LocationFinder
import time
import requests
import random
import json
import smtplib
import sys
import os
import ValueCheacker
from os import system, name
import glob
import Profile

def mainBrain():
     
     print("""    Welcome to BestBuy Product Checker
              Version: 1.01
  --------------------------------------
               """)
     
     print('Profiles\n________\n')
     userProfile = Profile.check_If_Files_Exist()
     print(userProfile)
     clear()
     userStoreList = LocationFinder.mainBrain()
     
     storeNums = []
     try:
          for stores in userStoreList:
               for store in stores:
                    
                    storeNum = store.split("-")[1].replace(" ",'').replace(")",'')
                    storeNums.append(storeNum)
                    
          LoopRunner(storeNums,userProfile)
     except:
          for store in userStoreList:
               storeNum = store.split("-")[1].replace(" ",'').replace(")",'')
               storeNums.append(storeNum)
           
          LoopRunner(storeNums,userProfile)               

     print('Profile file was not setup correctly')
     mainBrain()
     
#productName[0], productURL[0], productSKU[1], userEmail[2], numEmailToSend[3], stopLoop[4]            

def LoopRunner(storeNums,userProfile):
 
     loopBreaker = 0
     loopCounter = 1
     
     while loopBreaker < 1:
          clear()
          print('Product --> ' + userProfile[0])
          print('\nChecker counter: ' + str(loopCounter) +'\n')
          
          for storeID in storeNums:
               status = GetStatus(setUserAngent(),userProfile[1],userProfile[2],storeID)
               if status == None:
                    pass
               else:
                  num = sendEmail(status,userProfile[1],userProfile[3],userProfile[4],userProfile[5])
                  loopBreaker = loopBreaker + num
                  
          time.sleep(0.05)
          loopCounter = loopCounter + 1
          
def GetStatus(user_agent,productURL,productSKU,storeNums):

  with requests.Session() as Product:
      headers = {
            'Host': 'www.bestbuy.com',
            'user-agent': user_agent,
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': productURL,
            'accept-language': 'en-US,en;q=0.9',
        }
      params = (
            ('paths', '[["shop","magellan","v2","storeId","stores",'+storeNums+',["displayName","status","storeType","zipCode"]],["shop","ispu","v1","onShelfDisplay","skus",'+productSKU+',"locationId",'+storeNums+',"nearby"],["shop","ispu","v1","onShelfDisplay","skus",'+productSKU+',"locationId",'+storeNums+',["locationDetail","onShelfDisplay"],["city","id","locationFormat","name","zipCode"]],["shop","buttonstate","v5","item","skus",'+productSKU+',"conditions","NONE","destinationZipCode","%20","storeId","%20","context","cyp","addAll","false"],["shop","buttonstate","v5","item","optional","skus",'+productSKU+',"conditions","NONE","destinationZipCode",11214,"storeId",'+storeNums+',"storeZipCode","%20","context","pdp","addAll","false","consolidated","false","source","buttonView","xboxAllAccess","false","buttonStateResponseInfos",0,["buttonState","displayText","hyperlinkUrl","planButtonState","planDisplayText"]]]'),
            ('method', 'get'),
        )

      try:
           proxies = {'https': 'http://127.0.0.1:8888'}
           response = Product.get('https://www.bestbuy.com/api/tcfb/model.json',headers=headers, params=params )
           ProductSatus = response.content
           jsonData = json.loads(ProductSatus)
           status = jsonData['jsonGraph']['shop']['buttonstate']['v5']['item']['optional']['skus'][productSKU]['conditions']['NONE']['destinationZipCode']['11214']['storeId'][storeNums]['storeZipCode']['%20']['context']['pdp']['addAll']['false']['consolidated']['false']['source']['buttonView']['xboxAllAccess']['false']['buttonStateResponseInfos']['0']['buttonState']['value']
      except:
           time.sleep(5)
           GetStatus(user_agent,productURL,productSKU,storeNums)
      print("Checking: "+productSKU+" at " + storeNums +" Store  --> "+status) 
      

      if (status == 'COMING_SOON' or status == 'SOLD_OUT' or status == 'CHECK_STORES'):
         return None
      else:
         return status
     
def sendEmail(status,productURL,userEmail,emailSend,stopLoop):
     for x in range(int(emailSend)):
        email = userEmail
        passwd = 'QwertyuioP11$'
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
          smtp.ehlo()
          smtp.starttls()
          smtp.ehlo()
          smtp.login("vuktor1889@gmail.com","QwertyuioP11$")
          msg = status+"\n"+productURL
          smtp.sendmail('vuktor1889@gmail.com', userEmail, msg)
     print('Email was send!')     
     if (stopLoop.lower() == 'y'):
          return 1
     else:
          return 0

     
def clear(): 

    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
def setUserAngent():
     user_agents=[
                     'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                     'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                     'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko)',
                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                     'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
                     'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
                 ]
     return random.choice(user_agents)        
mainBrain()
