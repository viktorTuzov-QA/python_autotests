from os import access
from urllib import response
from jsonschema import validators

import pytest
import requests



def test_autorisation():
    url = "https://k-ampus.dev/api/v1/login"
    body_json = {
        "username": "skhalipa@gmail.com",
        "password": "skhalipa@gmail.com"


    }
    response = requests.post(url, json=body_json)
    assert response.status_code == 200
    token = response.json()["accessToken"]
    assert token != ""

    url = "https://k-ampus.dev/api/v1/competence"

    header = {"Authorization": f"{token}"}
    response = requests.get(url, headers = header)
    assert response.status_code == 200
    json_resp = response.json()
    schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "content": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "skillIds": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          },
          "isHardSkill": {
            "type": "boolean"
          }
        }
      }
    },
    "pageable": {
      "type": "object",
      "properties": {
        "sort": {
          "type": "object",
          "properties": {
            "sorted": {
              "type": "boolean"
            },
            "unsorted": {
              "type": "boolean"
            },
            "empty": {
              "type": "boolean"
            }
          }
        },
        "pageNumber": {
          "type": "integer"
        },
        "pageSize": {
          "type": "integer"
        },
        "offset": {
          "type": "integer"
        },
        "unpaged": {
          "type": "boolean"
        },
        "paged": {
          "type": "boolean"
        }
      }
    }
  }
}
    va = validators.Draft4Validator(schema)
    va.validate(json_resp)
   
    



