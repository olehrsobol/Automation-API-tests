import allure

class Endpoint:
    response = None
    response_json = None

    @allure.step('Check the response is 200')
    def check_response_is_200(self):
        assert self.response.status_code == 200