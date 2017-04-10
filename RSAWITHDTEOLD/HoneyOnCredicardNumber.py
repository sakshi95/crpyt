import csv
import random
'''def openfile():
    f=open('fruitname.txt','r')
    message=f.read()
    f.close()
    return message'''
#It return seed Value corresponding element
def searchElement(element):
    with open('creditcard.csv', 'r') as outcsv:
        reader = csv.reader(outcsv, delimiter=',', lineterminator='\n')
        element=element.lower()
        for item in reader:
            if element == item[0]:
                return item[1]
    #insert element if was not exist
    with open('creditcard.csv', 'a') as outcsv:
        writer = csv.writer(outcsv, lineterminator='\n')
        mapvalue=random.getrandbits(32)
        item=element.lower()
        writer.writerow([item, mapvalue])
        return str(mapvalue)

#It return honey key if attempt by wrong key
def returnDiifMapValue(index):
    with open('creditcard.csv', 'r') as outcsv:
        reader = csv.reader(outcsv, delimiter=',', lineterminator='\n')
        rows = list(reader)
        row_count = len(rows)
        #index=int(random.random()*100)
        return rows[index%row_count][0]

#It return the corresponding element of seed value
def searchMapvalueElement(value,key):
    with open('creditcard.csv', 'r') as outcsv:
        reader = csv.reader(outcsv, delimiter=',', lineterminator='\n')

        for item in reader:
            if value == item[1]:
                return item[0]

        rows = list(reader)
        row_count = len(rows)
        return rows[key % row_count][0]