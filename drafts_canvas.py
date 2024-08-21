import sqlite3
import requests


#
#
#
#
#
#
#
# Заброшенный файл, в котором проверял гипотезы и ставил эксперименты
#
#
#
#
#
#
#

response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies?offset=1&limit=2")


inp_vacancy = response.json()['results']

print(inp_vacancy)


#cursor.execute('INSERT INTO Vacancies_DB (vacancy_id, source, region_code, region_name) VALUES (?, ?, ?, ?)', (inp_vacancy['id'], inp_vacancy['source'], inp_vacancy['region']['region_code'], inp_vacancy['region']['name']))


# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Vacancies_DB
cursor.execute('''
CREATE TABLE IF NOT EXISTS Vacancies_DB (
table_id INTEGER PRIMARY KEY,
vacancy_id INTEGER
source TEXT
region TEXT
company TEXT
creation-date TEXT
salary TEXT
salary_min INTEGER
salary_max INTEGER
job-name TEXT
vac_url TEXT
employment TEXT
schedule TEXT
duty TEXT 
category TEXT
requirement TEXT
addresses TEXT
social_protected TEXT
contact_list TEXT
contact_person TEXT
work_places TEXT
code_profession INTEGER
currency TEXT
term TEXT
)
''')



for i in range(0, 500):
    inp_vacancy = response.json()['results']['vacancies'][i]['vacancy']

    cursor.execute('INSERT INTO Vacancies_DB (vacancy_id, source, region_code, region_name) VALUES (?, ?, ?, ?)', (inp_vacancy['id'], inp_vacancy['source'], inp_vacancy['region']['region_code'], inp_vacancy['region']['name']))



#for key, value in inp_vacancy.items():
#    cursor.execute('''
#    ALTER TABLE Vacancies_DB
#    ADD COLUMN :inp TEXT;
#    ''')


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()




#print(response.status_code, '\n\n\n', response.json())



