from faker import Faker

fake = Faker('ru_RU')


class Generator:
    # Генерируем логин
    @staticmethod
    def generate_login():
        login = fake.user_name()
        return login

    # Генерируем пароль
    @staticmethod
    def generate_password():
        password = fake.password(length=10)
        return password

    # Генерируем имя
    @staticmethod
    def generate_first_name():
        first_name = fake.first_name()
        return first_name

    # Генерируем фамилию
    @staticmethod
    def generate_last_name():
        last_name = fake.last_name()
        return last_name

    # Генерируем адрес
    @staticmethod
    def generate_address():
        address = fake.street_address()
        return address

    # Генерируем номер телефона
    @staticmethod
    def generate_phone_number():
        phone_number = fake.phone_number()
        return phone_number
