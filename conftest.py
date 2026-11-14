import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

@pytest.fixture
def obj_id():
    create_object_endpoint = CreateObject()
    delete_object_endpoint = DeleteObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_object_endpoint.new_object(payload)
    yield create_object_endpoint.response_json['id']
    delete_object_endpoint.delete_obj_by_id(create_object_endpoint.response_json['id'])