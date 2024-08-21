import sqlite3
import requests


# Устанавливаем соединение с базой данных
connection = sqlite3.connect('Vacancies.db')
cursor = connection.cursor()

# Создаем таблицу Vacancies_DB
cursor.execute('''
CREATE TABLE IF NOT EXISTS Vacancies_Table (
table_id INTEGER PRIMARY KEY,
vacancy_id INTEGER,
source TEXT,
region TEXT,
company TEXT,
creation_date TEXT,
salary TEXT,
salary_min INTEGER,
salary_max INTEGER,
job_name TEXT,
vac_url TEXT,
employment TEXT,
schedule TEXT,
duty TEXT,
category TEXT,
requirement TEXT,
addresses TEXT,
social_protected TEXT,
contact_list TEXT,
contact_person TEXT,
work_places TEXT,
code_profession INTEGER,
currency TEXT,
term TEXT
)
''')


def insert_values(offset_val):
    #Получаем данные от API по 100 вакансиям, раскрываем для более удобной работы
    response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies?", {'offset': offset_val, 'value': 100})
    inp_vacancy = response.json()['results']['vacancies']

#Записываем значения ключей в промежуточный словарь, чтобы не допустить ошибки об отсутствии элемента
    for i in range(len(inp_vacancy)):
        for d_key, d_value in inp_vacancy[i].items():
            temp_list = {}
            for d_key1, d_value1 in d_value.items():
                temp_list[d_key1] = str(d_value1)
            cursor.execute("INSERT INTO Vacancies_Table (vacancy_id, source, region, company, creation_date, salary, salary_min, salary_max, job_name, vac_url, employment, schedule, duty, category, requirement, addresses, social_protected, contact_list, contact_person, work_places, code_profession, currency, term) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (temp_list.pop('id', None), temp_list.pop('source', None), temp_list.pop('region', None), temp_list.pop('company', None), temp_list.pop('creation-date', None), temp_list.pop('salary', None), temp_list.pop('salary_min', None), temp_list.pop('salary_max', None), temp_list.pop('job-name', None), temp_list.pop('vac_url', None), temp_list.pop('employment', None), temp_list.pop('schedule', None), temp_list.pop('duty', None), temp_list.pop('category', None), temp_list.pop('requirement', None), temp_list.pop('addresses', None), temp_list.pop('social_protected', None), temp_list.pop('contact_list', None), temp_list.pop('contact_person', None), temp_list.pop('work_places', None), temp_list.pop('code_profession', None), temp_list.pop('currency', None), temp_list.pop('term', None) ))



for i in range(5):
    insert_values(i * 100)

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
