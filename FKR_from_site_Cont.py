from bs4 import BeautifulSoup
import requests

# ссылка на страницу, которую парсим
url_for_parse = 'http://fkr-spb.ru/auction2018'
# Строка юзер-агент для того, чтобы сайт отвечал корректно
user_agent_string = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

headers = {'user-agent': user_agent_string}
page = requests.get(url_for_parse, headers=headers)

if page.status_code == requests.codes.ok:
    soup = BeautifulSoup(page.text, features="html.parser")
    tbodytag=soup.find('tbody')
    for trtag in tbodytag.findAll('tr'):
        tdtag = trtag.findAll('td')
        if tdtag[4].getText() == 'отменен':
            continue
        print (tdtag[0].getText())
        print (tdtag[1].getText())
        print (tdtag[2].getText())
        print (tdtag[3].getText())
        tdtag = trtag.findAll('a')
        if len(tdtag) >0:
            print (tdtag[1].get('href'))

#        for tdtag in trtag.findAll('td'):
#            print (tdtag.getText())

