import re

def checkValueInt(num):
      if num.isdigit():
          return True
      else:
          print("Invalid Input!!")
      return False

def checkValueString(String):
      if String.isalpha():
          return True
      else:
          print("Invalid Input!!")
      return False

def checkValueEmail(Email):
      regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
      if(re.search(regex,Email)):  
         return True
      else:  
        print("Invalid Email")  
      return False

def checkValueChar(char):
      if len(char) == 1:
          if char.lower() == 'n': 
             return True         
          else: 
             if char.lower() == 'y': 
                return True
             else:
                return False
      else:
          print("Invalid Input!!")
          return False

def checkValueBbyURL(url):
      try:
            if (url[:29] == 'https://www.bestbuy.com/site/'):
                  return True
            else:
                  print('Invalid BestBuy Product Link (ex. https://www.bestbuy.com/site/........ )')
                  return False
      except:
            print('Invalid BestBuy Product Link (ex. https://www.bestbuy.com/site/........ )')
