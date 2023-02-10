import json

import requests

# gaunam zmones kurie siuo metu yra Tarptautinej kosminej stoty.JSON formatu
# people = requests.get('http://api.open-notify.org/astros.json')
# print(people.text)

# naudojant nemokama API gaunam euru-doleriu kursu pokycius kas menesi

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
for month in months:
    r = requests.get(f'https://api.ratesapi.io/api/2019-{month}-15')
    dictionary = json.loads(r.text)
    print(f"2019-{month}-15     EUR-USD    {dictionary['rates']['USD']}")
