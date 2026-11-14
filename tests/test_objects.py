import pytest
import requests
import allure
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject

payload = {
          "name": "Apple MacBook Pro 17",
          "data": {
            "year": 2020,
            "price": 1999.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
          }
    }

# @pytest.mark.parametrize('payload', payloads.create_payloads)
def test_create_object():
    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_name(payload["name"])
    new_object_endpoint.check_response_is_200()

def test_get_object(obj_id):
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_by_id(obj_id)
    get_obj_endpoint.check_response_is_200()

# @pytest.mark.parametrize('payload', payloads.upload_payloads)
def test_update_object(obj_id):
    update_obj_endpoint = UpdateObject()
    update_obj_endpoint.update_obj_by_id(obj_id, payload=payload)
    update_obj_endpoint.check_response_by_name(payload["name"])
    update_obj_endpoint.check_response_is_200()

def test_delete_object(obj_id):
    delete_obj_endpoint = DeleteObject()
    delete_obj_endpoint.delete_obj_by_id(obj_id)
    delete_obj_endpoint.check_response_is_200()
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_404()
