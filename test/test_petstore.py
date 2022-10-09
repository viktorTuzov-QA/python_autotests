from urllib import response
import pytest
import requests

id_pet = 123
name_pet = "MACHO"
url = "https://petstore.swagger.io/v2/pet/"

def test_status_code():
    response = requests.get(url + str(id_pet))
    assert response.status_code == 200

def test_name_pet():
    response = requests.get(url + str(id_pet))
    assert response.json()["name"] == name_pet
