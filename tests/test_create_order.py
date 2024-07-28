import allure
import pytest
import requests
from data import *


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа при указании разных цветов самоката')
    @pytest.mark.parametrize('payload', [DataForOrder.black_scooter,
                                         DataForOrder.grey_scooter,
                                         DataForOrder.no_color_scooter,
                                         DataForOrder.both_colors_scooters])
    def test_create_order_with_diff_colors_success(self, payload):

        response = requests.post(ApiUrls.ORDER_API, json=payload)
        assert response.status_code == 201, 'track' in response.json()
