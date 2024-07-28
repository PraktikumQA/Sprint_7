import allure
import requests
from data import *
from generator import Generator


class TestLoginCourier:

    @allure.title('Проверка успешной атворизации курьера')
    def test_login_courier_success(self):
        payload = {
            "login": Generator.generate_login(),
            "password": Generator.generate_password(),
            "firstName": Generator.generate_first_name()
        }

        requests.post(ApiUrls.CREATE_COURIER_API, data=payload)
        response = requests.post(ApiUrls.LOGIN_COURIER_API, data=payload)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Проверка попытки логина курьера без поля login')
    def test_no_login_courier(self):
        payload = {
            "login": "",
            "password": Generator.generate_password(),
            "firstName": Generator.generate_first_name()
        }

        response = requests.post(ApiUrls.LOGIN_COURIER_API, data=payload)
        assert response.status_code == 400 and response.json() == Responses.courier_without_login_or_password_text

    @allure.title('Проверка попытки логина курьера без поля password')
    def test_no_password_courier(self):
        payload = {
            "login": "",
            "password": Generator.generate_password(),
            "firstName": Generator.generate_first_name()
        }

        response = requests.post(ApiUrls.LOGIN_COURIER_API, data=payload)
        assert response.status_code == 400 and response.json() == Responses.courier_without_login_or_password_text

    @allure.title('Проверка авторизации несуществующего курьера')
    def test_courier_not_exist(self):
        payload = {
            "login": 'thereisnocourier',
            "password": 'password?idonthaveany',
            "firstName": 'idonthaveaname'
        }

        response = requests.post(ApiUrls.LOGIN_COURIER_API, data=payload)
        assert response.status_code == 404, response.json() == Responses.courier_not_exist

    @allure.title('Проверка логина c неправильным паролем')
    def test_login_with_wrong_password(self):
        payload = {
            "login": Generator.generate_login(),
            "password": DataForOrder.wrong_password,
            "firstName": Generator.generate_first_name()
        }

        response = requests.post(ApiUrls.LOGIN_COURIER_API, data=payload)
        assert response.status_code == 404, response.json()['message'] == Responses.courier_not_exist
