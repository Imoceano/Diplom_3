import allure
from faker import Faker

faker = Faker()


@allure.step('Генерация данных  для регистрации нового пользователя пользователя.')
def generate_info_for_registration():
    email = faker.email()
    password = faker.password()
    name = faker.name()
    return email, password, name