from bs4 import BeautifulSoup
import requests

# ссылка на страницу, которую парсим
url_for_parse = 'http://fkr-spb.ru/auction2018'
# Строка юзер-агент для того, чтобы сайт отвечал корректно
user_agent_string = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

headers = {'user-agent': user_agent_string}
page = requests.get(url_for_parse, headers=headers)

#f = open("11.html",'rt',encoding='utf-8',)
#page = f.read()

#if len(page) > 0:
if page.status_code == requests.codes.ok:
    soup = BeautifulSoup(page.text, features="html.parser")
#    soup = BeautifulSoup(page, features="html.parser")
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
                atag1=soup1.findAll('a', class_='documents__link file-')
                if len(atag1) > 0:
                    url_docx = atag1[0].get('href')
                    print(url_docx)





#        for tdtag in trtag.findAll('td'):
#            print (tdtag.getText())

