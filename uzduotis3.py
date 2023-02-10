import requests

# iš adreso https://orai.15min.lt/prognozes
# ištraukti ir atspausdinti oro prognozę Birstone

r = requests.get('https://orai.15min.lt/prognozes')
html = r.text
split_by_vilnius = html.split('Birštonas')
split_by_hot = split_by_vilnius[-1].split('hot">')
res = split_by_hot[1].split()[0]

print(res)