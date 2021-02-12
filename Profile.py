import requests
import ValueCheacker
import os
import sys
from bs4 import BeautifulSoup
import random
import glob
import ValueCheacker
from os import system, name

def getFileList():
     txtfiles=[]
     fileName = []
     for file in glob.glob("*.txt"):
         txtfiles.append(file)
     profileNum = 1    
     for txt in txtfiles:
          profileName = (str(txt[:8])+str(int(profileNum ))+'.txt')
       
          if os.path.exists( profileName ):
             if (os.stat( profileName ).st_size == 0):
                 break
             else:
                  
                  fileName.append(profileName)
                  profileNum = profileNum +1
                  
          else:
               pass
     return fileName
                  
def check_If_Files_Exist():
     txtfiles=[]
     for file in glob.glob("*.txt"):
         txtfiles.append(file)
     if not txtfiles:
          xe = 1
          print('No profiles was found!\n')
          create_Profile_Settings(str(xe))
          userProfile = displayProfileSettings('Profile-'+str(xe)+'.txt')
          return userProfile
     else:
          profileNum = 1
          fileName = getFileList()
          for txt in txtfiles:
                  profileName = (str(txt[:8])+str(profileNum)+'.txt')
                  if os.path.exists( profileName ):
                       if (os.stat( profileName ).st_size == 0):
                          create_Profile_Settings(profileNum)
                          break
                       else:
                            userProfile,x = displayProfiles(profileNum)
                            profileNum = profileNum +1
                            print('')
                            
                            while True:
                                   Profile = input('Chooice to Profile OR type 0 to create new profile : ')
                                   status = ValueCheacker.checkValueInt(Profile)
                                   if (status == True):
                                        break
                            if(str(Profile) == '0'):
                                for y in range(10000):
                                     try:
                                          if (os.stat( str(txt[:8])+str(y)+'.txt' ).st_size == 0):     
                                               userProfile = create_Profile_Settings(y)
                                               return userProfile.split(';')
                                               break
                                     except:
                                          pass
                                userProfile = create_Profile_Settings(x)
                                return userProfile.split(';')
                                 
                         
                            else:
                              Profile = int(Profile) - 1
                              try:
                                  userProfile = displayProfileSettings(fileName[Profile])                                           
                                  return userProfile
                                  
                              except:
                                  print('Invalid Input!!')
                                  pass
                             
                  else:
                       
                       profile = create_Profile_Settings(profileNum)
                       return profile
                       break
                     
def displayProfiles(profileNum):
     
     for x in range(1000):
          x = x+1
          try: 
               with open ('Profile-'+str(x)+'.txt', 'r') as profileInfo:
                   userProfile = profileInfo.read().split(';')
                   print(str(x)+ " : " + userProfile[0])
          except:
               break
          
     return userProfile,x    
def displayProfileSettings(profileNum):
     
     with open (profileNum, 'r') as profileFile:
          userProfile = profileFile.read().split(';')              
          print('\nProduct: '+userProfile[0])
          print('Email: '+userProfile[3])
          print('Emails to send: '+userProfile[4])
          print('Stop if it avalibale: '+userProfile[5])
          print("_______________________________")
          while True:          
               stopLoop = input("Want to use this Settings? y/n: ")
               status = ValueCheacker.checkValueChar(stopLoop)
               if status == True:
                    if (stopLoop == 'y'):
                         break
                         return userProfile
                    else:
                         print('')
                         check_If_Files_Exist()
                         break
          return userProfile
def create_Profile_Settings(num):
     clear()
     print("""    Welcome to BestBuy Product Checker
              Version: 1.01
  --------------------------------------
               """)
     print('Profile Creater')
     print('_______________')

     with open ('Profile-'+str(num)+'.txt', 'w+') as pInfo:
          while True:
               productURL = input("Enter Product Url: ")
               status = ValueCheacker.checkValueBbyURL(productURL)
               if status == True:
                    productName = getProductTittle(productURL)
                    productSKU = productURL.split('=')[1]
                    break
          print('-----')
          while True:
               userEmail = input("Enter your email: ")
               status = ValueCheacker.checkValueEmail(userEmail)
               if status == True:
                    break
          print('-----')
          while True:
               numEmailToSend = input("How many emails you want to recive when is available: ")
               status = ValueCheacker.checkValueInt(numEmailToSend)
               if status == True:
                    break
          print('-----')
          while True:          
               stopLoop = input("Do you want to stop reciving email after '"+numEmailToSend+"' emails have been send? y/n ")
               status = ValueCheacker.checkValueChar(stopLoop)
               if status == True:
                    break
                              
          userP = (str(productName)+';'+str(productURL)+';'+productSKU+";"+str(userEmail)+";"+numEmailToSend+';'+str(stopLoop))
          pInfo.write(userP)
          return userP

def getProductTittle(productURL):
     
     UserAngent = setUserAngent()
     productSKU = productURL.split('=')[1]
     headers ={
     'Host': 'www.bestbuy.com',
     'upgrade-insecure-requests': '1',
     'user-agent': UserAngent,
     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
     'sec-gpc': '1',
     'sec-fetch-site': 'same-origin',
     'sec-fetch-mode': 'navigate',
     'sec-fetch-user': '?1',
     'sec-fetch-dest': 'document',
     'referer': 'https://www.bestbuy.com/',
     'accept-language': 'en-US,en;q=0.9',
     }
     params =(
         ('skuId', productSKU),
     )
     
     try:
          response = requests.get(productURL,headers=headers, params=params)
          soup = BeautifulSoup(response.content, 'html.parser') 
          productTittle = soup.find('h1', class_ = "heading-5 v-fw-regular" ).text
          if productTittle == 'None':
               pass
          else:
               return productTittle
     except:
          getProductTittle(productURL) 
def setUserAngent():
     
     user_agents=[
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
      'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
      'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko)',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
      'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
      'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36']
     return random.choice(user_agents)
def clear(): 

    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
