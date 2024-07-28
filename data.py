from generator import Generator


class ApiUrls:
    HOME_PAGE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_API = f'{HOME_PAGE_URL}/api/v1/courier'
    LOGIN_COURIER_API = f'{HOME_PAGE_URL}/api/v1/courier/login'
    ORDER_API = f'{HOME_PAGE_URL}/api/v1/orders'


class Responses:
    create_courier_success_text = '{"ok": true}'
    create_courier_without_login_or_password_text = '{"message": "Недостаточно данных для создания учетной записи"}'
    already_exist_courier_text = '{"message": "Этот логин уже используется"}'
    courier_without_login_or_password_text = '{"message":  "Недостаточно данных для входа"}'
    courier_not_exist = '{"message": "Учетная запись не найдена"}'


class DataForOrder:
    black_scooter = {
        "firstName": Generator.generate_first_name(),
        "lastName": Generator.generate_last_name(),
        "address": Generator.generate_address(),
        "metroStation": 5,
        "phone": Generator.generate_phone_number(),
        "rentTime": 1,
        "deliveryDate": "2024-07-30",
        "comment": "Быстрее",
        "color": ["BLACK"]
    }

    grey_scooter = {
        "firstName": Generator.generate_first_name(),
        "lastName": Generator.generate_last_name(),
        "address": Generator.generate_address(),
        "metroStation": 3,
        "phone": Generator.generate_phone_number(),
        "rentTime": 3,
        "deliveryDate": "2024-07-31",
        "comment": "Я на работе",
        "color": ["GREY"]
    }

    both_colors_scooters = {
        "firstName": Generator.generate_first_name(),
        "lastName": Generator.generate_last_name(),
        "address": Generator.generate_address(),
        "metroStation": 7,
        "phone": Generator.generate_phone_number(),
        "rentTime": 2,
        "deliveryDate": "2024-07-29",
        "comment": "Хочу разноцветный",
        "color": ["BLACK",
                  "GREY"
                  ]
    }

    no_color_scooter = {
        "firstName": Generator.generate_first_name(),
        "lastName": Generator.generate_last_name(),
        "address": Generator.generate_address(),
        "metroStation": 11,
        "phone": Generator.generate_phone_number(),
        "rentTime": 4,
        "deliveryDate": "2024-08-10",
        "comment": "Без комментария",
        "color": []
    }

    no_login = {
        "login": '',
        "password": Generator.generate_password(),
        "firstName": Generator.generate_first_name()
    }

    no_password = {
        "login": Generator.generate_login(),
        "password": '',
        "firstName": Generator.generate_first_name()
    }

    no_first_name = {
        "login": Generator.generate_login(),
        "password": Generator.generate_password(),
        "firstName": ''
    }

    wrong_password = '@12345678oAo87654321@'