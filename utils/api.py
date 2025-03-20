import pytest
from utils.http_methods import Http_methods
from faker import Faker
import random
from string import ascii_letters,hexdigits,punctuation

class Stellarburger_api_tests:

    base_url = "https://stellarburgers.nomoreparties.site"
    ingredients_data = "/api/ingredients"
    create_order = "/api/orders"
    password_reset = "/api/password-reset"
    create_user = "/api/auth/register"
    auth = "/api/auth/login"
    register = "/api/auth/register"
    logout = "/api/auth/logout"
    refresh_token = "/api/auth/token"
    user_data = "/api/auth/user"
    all_orders = "/api/orders/all"
    user_orders = "/api/orders"


    @staticmethod
    def test_send_empty_request():
        """
        sending an empty request, expected status code 403
        """
        used_url = Stellarburger_api_tests.base_url+Stellarburger_api_tests.create_user
        base_json = {
            "email": "",
            "password": "",
            "name": ""
            }
        request = Http_methods.post(used_url,base_json)
        assert request.status_code == 403
        assert request.json()['success'] == False
        assert request.json()['message'] == "Email, password and name are required fields"
        print("Success, it's impossible to send an empty request, test passed")


    @staticmethod
    def test_send_half_request():
        """
        create an account for user by using generating random data with faker and random
        """
        used_url = Stellarburger_api_tests.base_url+Stellarburger_api_tests.create_user
        fake = Faker()

        email = f"{fake.first_name()}@gmail.com"
        username = fake.first_name()
        password = ""
        for i in range(10):
            password += random.choice(ascii_letters + hexdigits + punctuation)

        create_user_json = {
            "email": f"{email}",
            "password": "",
            "name": f"{username}"
            }

        request = Http_methods.post(used_url,create_user_json)
        assert request.status_code == 403
        assert request.json()['success'] == False
        assert request.json()['message'] == "Email, password and name are required fields"
        print("Success, it's impossible to send an half-empty request, test passed")


    @staticmethod
    def test_create_user():
        """
        create an account for user by using generating random data with faker and random
        """
        used_url = Stellarburger_api_tests.base_url+Stellarburger_api_tests.create_user
        fake = Faker()

        email = f"{fake.first_name()}@gmail.com"
        username = fake.first_name()
        password = ""
        for i in range(10):
            password += random.choice(ascii_letters + hexdigits + punctuation)

        create_user_json = {
            "email": f"{email}",
            "password": f"{password}",
            "name": f"{username}"
            }

        request = Http_methods.post(used_url,create_user_json)
        assert request.status_code == 200
        assert request.json()['success'] == True
        assert email.lower() == request.json()['user']['email']
        assert username == request.json()['user']['name']
        return f"accessToken - {request.json()['accessToken']}" f"refreshToken - {request.json()['refreshToken']}"
