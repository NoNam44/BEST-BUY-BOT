from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests
from os import system, name
import ValueCheacker
proxies = {'https': 'http://127.0.0.1:8888'}
def locationID_Getter():
     headers = {
    'Host': 'www.bestbuy.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.bestbuy.com/site/store-locator/',
    'accept-language': 'en-US,en;q=0.9',
     }

     #content = requests.get('https://www.bestbuy.com/site/store-locator/',verify=False ,headers=headers, proxies=proxies)
     content = requests.get('https://www.bestbuy.com/site/store-locator/',headers=headers)
     
     return content

def id_Filter(content):
     clear()

     print('            Store List')
     print('          _______________\n')
     storeList=[]
     soup = BeautifulSoup(content.text, 'html.parser')
     print('   Here choose a store to watch')
     print('-----------------------------------')
     for storeData in soup.findAll("li", class_="store"):
          storeNum = storeData['data-store-id']
          storeName = storeData.find(class_="btn-unstyled").text
          storeList.append(storeName+" ( Store ID - "+storeNum+")")
     
     return storeList
     
def userStores(storeList):
     
     listNum = 1     
     for store in storeList:         
          print(str(listNum) + ". "+ store)
          listNum = listNum + 1
          
     userStores = []
     print("---------------------------------------------")
     while True:
          userStore = input("Enter store to watch or type ' all ' to choose all of them. To countiune type ' 0 ': ")
          
          if  userStore.lower() == 'all' :
               userStores.append(storeList)
               break
          elif userStore == '0':
               if not userStores:
                    print('Nothing was choose')
               else:
                    break
          
          elif True == ValueCheacker.checkValueInt(userStore):
               try:
                    userStores.append(storeList[int(userStore)-1])
               except:
                    print("Out of list")
          else:
               pass
              
     return userStores
          
def mainBrain():          
     content = locationID_Getter()
     storeList = id_Filter(content)
     return userStores(storeList)
      

def clear(): 

    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
