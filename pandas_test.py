import pandas as pd

mycolumns = ['reestrnum', 'etap', 'dog_data', 'dog_number', 'dog_price', 'dog_begin', 'dog_end', 'podr_name', 'podr_tel', 'pord_email']

maindf = pd.DataFrame(columns=mycolumns)
maindf.insert(['реестровый номер', 'Этап', 'Дата договора', 'Номер договора', 'Цена договора', 'Начало договора', 'Конец договора', 'Подрядчик', 'Тел', 'Эл Почта'])
# maindf[0] = ['реестровый номер', 'Этап', 'Дата договора', 'Номер договора', 'Цена договора', 'Начало договора', 'Конец договора', 'Подрядчик', 'Тел', 'Эл Почта']
print(maindf)

