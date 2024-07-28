import allure
import requests
from data import ApiUrls


class TestGetOrderList:

    @allure.title('Проверка получения всего списка заказов')
    def test_get_order_list(self):
        response = requests.get(ApiUrls.ORDER_API)
        assert response.status_code == 200, 'availableStations' and 'orders' in response.json()
