from bs4 import BeautifulSoup
from ftplib import FTP

def load_from_xml(filename):
    page = open(filename,'rt',encoding='utf-8').read()
    soup = BeautifulSoup(page, 'xml')
    if len(soup.findAll('ns2:fcsNotificationEF')) > 0:
        print ("Это правильный файл")
    print(soup.find('id').getText())
    print(soup.find('purchaseObjectInfo').getText())
    print(soup.find('purchaseResponsible').find('fullName').getText() + ' ' + soup.find('purchaseResponsible').find('INN').getText())
    for i in soup.find_all('purchaseNumber'):
        print(i.getText())
    print(soup.find('printForm').find('url').getText())
    for i in soup.find('attachments').find_all('fileName'):
        print(i.getText())

def loadfromftp ():
    pass

if __name__ == '__main__':
    load_from_xml('tst.xml')
