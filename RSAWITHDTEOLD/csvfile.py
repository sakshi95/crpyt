import csv
import random
def openfile():
    f=open('fruitname.txt','r')
    message=f.read()
    f.close()
    return message

'''def display():
  with open('newcsv.csv', 'r') as f:
    username='the'
    reader = csv.reader(f, delimiter=',',lineterminator='\n')
    for row in reader:
          if username == row[0]:
              print("The value of"+row[0]+"is"+row[1])
         
              
              
def iswordexist(username):
  with open('newcsv.csv', 'r') as f:
    #username='the'
    reader = csv.reader(f, delimiter=',',lineterminator='\n')
    for row in reader:
          if username == row[0]:
              return 1
    return 0
   '''
def searchElement(element):
    with open('fruitcsv.csv', 'r') as outcsv:
        reader = csv.reader(outcsv, delimiter=',',lineterminator='\n')
        for item in reader:
            if element==item[0]:
                print(item[1])
                return
    with open('fruitcsv.csv', 'w') as outcsv:
                 writer = csv.writer(outcsv,lineterminator='\n')
                 value=random.getrandbits(32)
                 writer.writerow([element,value])
                 return value
                 
            
            
        

    
          
def create():
  with open('fruitcsv.csv', 'w') as outcsv:
  
    #configure writer to write standard csv file
    writer = csv.writer(outcsv,lineterminator='\n')
    #writer.writerow(['number'])
    list=openfile()
    #values=random.getrandbits(32)
    words=[]
    for item in list.split():
        #Write item to outcsv
        item=item.lower()
        if item not in words:
           words.append(item)
           #values+=1
           writer.writerow([item,random.getrandbits(32)])
           words.append(item)
       
        
    

create()
#display()'''

    
    
    


            



            
            
        




