import requests
import allure
from endpoints.base_endpoint import Endpoint

class CreateObject(Endpoint):

    @allure.step('Create a new object')
    def new_object(self, payload):
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.response_json = self.response.json()

    @allure.step('Check that name is correct')
    def check_name(self, name):
        assert self.response_json["name"] == name