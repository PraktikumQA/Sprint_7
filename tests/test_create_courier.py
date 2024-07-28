import allure
import pytest
import requests
from data import *
from generator import Generator


class TestCreateCourier:

    @allure.title('Проверка на успешное создания курьера')
    def test_create_courier_success(self):
        payload = {
            "login": Generator.generate_login(),
            "password": Generator.generate_password(),
            "firstName": Generator.generate_first_name()
        }
        response = requests.post(ApiUrls.CREATE_COURIER_API, data=payload)
        assert response.status_code == 201, response.json() == Responses.create_courier_success_text

    @allure.title('Проверка невозможности создания двух одинаковых аккаунтов курьеров')
    def test_create_courier_already_exist(self):
        payload = {
            "login": Generator.generate_login(),
            "password": Generator.generate_password(),
            "firstName": Generator.generate_first_name()
        }

        requests.post(ApiUrls.CREATE_COURIER_API, data=payload)
        response = requests.post(ApiUrls.CREATE_COURIER_API, data=payload)
        assert response.status_code == 409, response.json() == Responses.already_exist_courier_text

    @allure.title('Проверка на ошибку создания курьера без ввода логина или пароля или имени')
    @pytest.mark.parametrize('payload', [DataForOrder.no_login, DataForOrder.no_password])
    def test_create_courier_without_login_or_password(self, payload):
        response = requests.post(ApiUrls.CREATE_COURIER_API, json=payload)
        assert response.status_code == 400, response.json() == Responses.create_courier_without_login_or_password_text
