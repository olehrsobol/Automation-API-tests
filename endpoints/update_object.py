import requests
from endpoints.base_endpoint import Endpoint

class UpdateObject(Endpoint):

    def update_obj_by_id(self, obj_id, payload):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
        self.response_json = self.response.json()

    def check_response_by_name(self, name):
        assert self.response_json["name"] == name