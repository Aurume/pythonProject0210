import requests

#r = requests.get('http://google.com')

#print(dir(r)) #ka galiu istraukti

#print(r.text) #gaunamas html

#print(r.content) #gaunamas html binary formatu

#r = requests.get('https://www.python.org/static/img/python-logo.png')
#print(r.content)

#issiaugomas paveikslelis is to binary kur virsuj
# with open('logo.png', 'wb') as f:
#     f.write(r.content)

#suzinom koks atsako kodas. Galim patikrinti veikia ar ne.
# r = requests.get('http://python.org')
# print(r.status_code)

# tikrinamas atsakas konkreciau
# r = requests.get('http://python.org/blabla')
# if r.status_code not in range(400, 600):
#     print('Pavyko prisijungti! Dirbame toliau...')
# else:
#     print(f'Kažkas ne taip.. Kodas {r.status_code}')

# ok metodas su kuriuo galima patikrinti atsaka taip pat
# r = requests.get('http://python.org/blabla')
# if r.ok:
#     print('važiuojam toliau!')
# else:
#     print(f'Klaida! kodas {r.status_code}')

# galim istraukti papildoma informacija is python puslapio
# r = requests.get('http://python.org/')
# print(r.headers)

# gaunu koks tipas(text/html)
# r = requests.get('http://python.org/')
# print(r.headers['content-type'])

# gaunu adresa puslapio
# r = requests.get('http://python.org/')
# print(r.url)

