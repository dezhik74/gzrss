from bs4 import BeautifulSoup
import requests

# ссылка на страницу, которую парсим
url_for_parse = 'http://fkr-spb.ru/auction2018'
# Строка юзер-агент для того, чтобы сайт отвечал корректно
user_agent_string = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
headers = {'user-agent': user_agent_string}


def Get_text_from_site (url):
    """ Качает html с сайта. возвращает текст странички или пустую строку """
    page = requests.get(url, headers=headers)
    if page.status_code == requests.codes.ok:
        return page.text
    else:
        return ''

def Get_FKR_text_from_file():
    """ Берет html из файла. возвращает содержимое файла или пустую строку """
    f = open("11.html",'rt',encoding='utf-8',)
    page = f.read()
    if len(page) > 0:
        return page
    else:
        return ''

# True - читаем из файла, False - читаем с сайта
Mode_develop = True
if Mode_develop:
    FKR_Text = Get_FKR_text_from_file()
else:
    FKR_Text = Get_text_from_site(url_for_parse)

#Возвращает значения: Auction_Nunber, Type_of_Work, Region, Auction_Price, URL_Roseltorg
def Parse_FKR (FKR_html):
    soup = BeautifulSoup(FKR_html, features="html.parser")
    tbodytag = soup.find('table')
    for trtag in tbodytag.findAll('tr'):
        tdtag = trtag.findAll('td')
        if tdtag[2].getText() == 'Район':
            continue
        if tdtag[4].getText() == 'отменен':
            continue
        print(tdtag[0].getText())
        print(tdtag[1].getText())
        print(tdtag[2].getText())
        print(tdtag[3].getText())
        s = tdtag[7].getText().split(',')
        if len(s) == 1:
            url_for_parse_1 = s[0]
        elif s[0].count('zakupki') > 1:
            url_for_parse_1 = s[1]
        elif s[1].count('zakupki') > 1:
            url_for_parse_1 = s[0]
        print(url_for_parse_1)
        return


if len(FKR_Text) >0:
    soup = BeautifulSoup(FKR_Text, features="html.parser")
    tbodytag=soup.find('table')
    for trtag in tbodytag.findAll('tr'):
        tdtag = trtag.findAll('td')
        if tdtag[2].getText() == 'Район':
            continue
        if tdtag[4].getText() == 'отменен':
            continue
        print (tdtag[0].getText())
        print (tdtag[1].getText())
        print (tdtag[2].getText())
        print (tdtag[3].getText())
        s = tdtag[7].getText().split(',')
        if len(s) == 1:
            url_for_parse_1 = s[0]
        elif s[0].count('zakupki') > 1:
            url_for_parse_1 = s[1]
        elif s[1].count('zakupki') > 1:
            url_for_parse_1 = s[0]
        print(url_for_parse_1)

#        atag=tdtag[7].findAll('a')
#        if len(atag) == 1:
#            url_for_parse_1 = atag[0].get('href')
#        elif atag[0].get('href').count('zakupki') > 1 :
#            url_for_parse_1 = atag[0].get('href')
#        elif atag[1].get('href').count('zakupki') > 1 :
#            url_for_parse_1 = atag[1].get('href')
#        print(url_for_parse_1)

        page = requests.get(url_for_parse_1, headers=headers)
        if page.status_code == requests.codes.ok:
            soup1=BeautifulSoup(page.text, features="html.parser")
            divtag=soup1.findAll('div', class_='steps__title')
            if divtag[len(divtag)-1].getText().count('Закупка завершена') > 0:
                print('Закупка завершена')
                atag1=soup1.findAll('a', class_='documents__link file-docx')
                if len(atag1) > 0:
                    url_docx = atag1[len(atag1)-1].get('href')
                    print(url_docx)





#        for tdtag in trtag.findAll('td'):
#            print (tdtag.getText())

