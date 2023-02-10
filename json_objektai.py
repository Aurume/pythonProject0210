import json

data = '''{
  "student": [ 

     { 
        "id":"01", 
        "name": "Tom", 
        "lastname": "Price" 
     }, 

     { 
        "id":"02", 
        "name": "Nick", 
        "lastname": "Thameson" 
     } 
  ]   
}'''

#pavertem String tipo duomenis i JSON naudojant .loads()
#data_dict = json.loads(data)
# print(data_dict)
# print(type(data_dict))

# istraukiam konkrecia info po loads pavertimo, pvz:lyti
# data_dict = json.loads(data)
# data_dict['student'][1]['name'] = 'Kyle'
# for student in data_dict['student']:
#     student.update({'gender':'male'})
# print(data_dict)

# atgal i Json formata naudojant .dumps(), indent-tarpu kiekis(2)
# data_dict = json.loads(data)
# new_json = json.dumps(data_dict, indent=2)
# print(new_json)

# su .dump() irasoma i faila, galima rusiuoti
# pvz pagal abecele naudojant sort_keys
with open('example2.json', 'w') as file:
    json.dump(data, file, indent=2, sort_keys=True)