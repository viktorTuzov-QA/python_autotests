import requests

id_pet = 123
name_pet = 'diego'
url = "https://petstore.swagger.io/v2/pet"
def data_json (id_pet, name_pet):

    data_json_pet = {
    "id": id_pet,
    "category": {
     "id": 0,
        "name": "string"
     },
    "name": name_pet,
     "photoUrls": [
        "string"
     ],
     "tags": [
     {
          "id": 0,
         "name": "string"
     }
    ],
    "status": "available"
    }
    return data_json_pet
response = requests.post(url, json = data_json(id_pet, name_pet))

print(response.text)

name_pet = "MACHO"

response = requests.put(url, json = data_json(id_pet, name_pet))

print(response.text)

response = requests.get(url + '/' + str(id_pet))

print(response.text)