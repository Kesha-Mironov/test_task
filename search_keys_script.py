import requests


keys_list = []


def get_keys (offset_value):
    #Получаем данные от API по интересующим нас 500 вакансиям
    response = requests.get("http://opendata.trudvsem.ru/api/v1/vacancies?",{'offset':offset_value, 'value':100})

    print(response.request.url)

    count = 0

    #Раскрываем первичные струкртуры полученных данных в читаемый вид
    inp_vacancy = response.json()['results']['vacancies']

    #Проходимся по данным, собирая в список названия ключей, если они нам ещё не встречались
    for i in range(len(inp_vacancy)):
        for d_key, d_value in inp_vacancy[i].items():
            count += 1
            for d_key1, d_value1 in d_value.items():
                if d_key1 not in keys_list:
                    keys_list.append(d_key1)

    print(count)


for off_value in range(5):
    get_keys(off_value * 100)

for i in keys_list:
    print(i)

print(keys_list)