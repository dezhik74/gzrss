import feedparser
import requests
from bs4 import BeautifulSoup


url_for_parse = 'http://zakupki.gov.ru/epz/capitalrepairs/extendedsearch/rss.html?morphology=on&pageNumber=1&sortDirection=false&recordsPerPage=_10&sortBy=UPDATE_DATE&contractStage_0=on&contractStage_1=on&contractStage_2=on&contractStage=0%2C1%2C2&customerTitle=%D0%9D%D0%95%D0%9A%D0%9E%D0%9C%D0%9C%D0%95%D0%A0%D0%A7%D0%95%D0%A1%D0%9A%D0%90%D0%AF+%D0%9E%D0%A0%D0%93%D0%90%D0%9D%D0%98%D0%97%D0%90%D0%A6%D0%98%D0%AF+%22%D0%A4%D0%9E%D0%9D%D0%94-%D0%A0%D0%95%D0%93%D0%98%D0%9E%D0%9D%D0%90%D0%9B%D0%AC%D0%9D%D0%AB%D0%99+%D0%9E%D0%9F%D0%95%D0%A0%D0%90%D0%A2%D0%9E%D0%A0+%D0%9A%D0%90%D0%9F%D0%98%D0%A2%D0%90%D0%9B%D0%AC%D0%9D%D0%9E%D0%93%D0%9E+%D0%A0%D0%95%D0%9C%D0%9E%D0%9D%D0%A2%D0%90+%D0%9E%D0%91%D0%A9%D0%95%D0%93%D0%9E+%D0%98%D0%9C%D0%A3%D0%A9%D0%95%D0%A1%D0%A2%D0%92%D0%90+%D0%92+%D0%9C%D0%9D%D0%9E%D0%93%D0%9E%D0%9A%D0%92%D0%90%D0%A0%D0%A2%D0%98%D0%A0%D0%9D%D0%AB%D0%A5+%D0%94%D0%9E%D0%9C%D0%90%D0%A5%22&customerCode=05727000001&customerFz94id=2190472&regionDeleted=false'
user_agent_string = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

d = feedparser.parse(url_for_parse)
number_of_rec: int = 0
for x in d['entries']:
    number_of_rec += 1
    print(str(number_of_rec) + ' ------------------------------------------')
#    print(x['title'])
#    print(x['link'])
#    s = x['link'].split('?')[1]
#    url = x['link'].split('?')[0]
#    s1 = s.split('=')
#    payload = {s1[0]: s1[1]}
    headers = {'user-agent': user_agent_string}
    page = requests.get(x['link'],  headers=headers)
#    print(page.url)
#    print(page.status_code)
#    print(page.text)
    if page.status_code == requests.codes.ok:

        soup = BeautifulSoup(page.text, features="html.parser")
        all_td = soup.select('td')
        for i in range(len(all_td)):
            if all_td[i].getText() == 'Номер реестровой записи':
                print('Номер реестровой записи: ' + all_td[i+1].getText().strip(' \n'))
            if all_td[i].getText() == 'Этап договора':
                print('Этап договора: ' + all_td[i+1].getText().strip(' \n'))
            if all_td[i].getText() == 'Дата заключения договора':
                print('Дата заключения договора: ' + all_td[i+1].getText().strip(' \n'))
            if all_td[i].getText() == 'Номер договора':
                print('Номер договора: ' + all_td[i+1].getText())
            if all_td[i].getText() == 'Цена договора, рублей':
                print('Цена договора, рублей : ' + all_td[i+1].getText().strip(' \n'))
            if all_td[i].getText() == 'Дата начала исполнения договора':
                print('Дата начала исполнения договора: ' + all_td[i+1].getText().strip(' \n'))
            if all_td[i].getText() == 'Дата окончания исполнения договора':
                print('Дата окончания исполнения договора: ' + all_td[i+1].getText().strip(' \n'))
            if all_td[i].getText() == 'Полное наименование ЮЛ / ФИО индивидуального предпринимателя':
                print('Подрядчик: ' + all_td[i + 1].getText().strip(' \n'))
            if all_td[i].getText() == 'Контактный телефон':
                print('Контактный телефон: ' + all_td[i + 1].getText().strip(' \n'))
            if all_td[i].getText() == 'Электронная почта':
                print('Электронная почта: ' + all_td[i + 1].getText().strip(' \n'))

print('--------------------------------------------')