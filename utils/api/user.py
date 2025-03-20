import os

from utils.http_methods import Http_methods
from faker import Faker
import random
from string import ascii_letters,hexdigits,punctuation

class Test_user:

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
        used_url = Test_user.base_url + Test_user.create_user
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
        used_url = Test_user.base_url + Test_user.create_user
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
        used_url = Test_user.base_url + Test_user.create_user
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
        print(request.text)
        assert request.status_code == 200
        assert request.json()['success'] == True
        assert email.lower() == request.json()['user']['email']
        assert username == request.json()['user']['name']
        print("Successful user creation, all fields match")
        Test_user.save_name(request.json()['user']['name'])
        Test_user.save_email(request.json()['user']['email'])
        Test_user.save_password(password)
        Test_user.save_bearer_token(request.json()['accessToken'])
        Test_user.save_refresh_token(request.json()['refreshToken'])


    # save/read user data into .txt methods

    @staticmethod       # write
    def save_email(user_email):
        with open(f"{os.getcwd()}/api/txt/user/user_email.txt", "w") as file:
            file.write(user_email)
            return user_email


    @staticmethod       # read
    def read_email(user_email):
        with open(f"{os.getcwd()}/api/txt/user/user_email.txt", "r") as file:
            f = file.read(user_email)
            return f


    @staticmethod       # write
    def save_name(username):
        with open(f"{os.getcwd()}/api/txt/user/user_name.txt", "w") as file:
            file.write(username)
            return username


    @staticmethod       # read
    def read_name(username):
        with open(f"{os.getcwd()}/api/txt/user/user_name.txt", "r") as file:
            f = file.read(username)
            return f


    @staticmethod       # write
    def save_password(user_password):
        with open(f"{os.getcwd()}/api/txt/user/user_password.txt", "w") as file:
            file.write(user_password)
            return user_password


    @staticmethod       # read
    def read_password(user_password):
        with open(f"{os.getcwd()}/api/txt/user/user_password.txt", "r") as file:
            f = file.read(user_password)
            return f


    @staticmethod       # write
    def save_bearer_token(bearer):
        with open(f"{os.getcwd()}/api/txt/user/bearer_token.txt", "w") as file:
            file.write(bearer)
            return bearer


    @staticmethod       # read
    def read_bearer_token(bearer):
        with open(f"{os.getcwd()}/api/txt/user/bearer_token.txt", "r") as file:
            f = file.read(bearer)
            return f


    @staticmethod       # write
    def save_refresh_token(refresh_token):
        with open(f"{os.getcwd()}/api/txt/user/refresh_token.txt", "w") as file:
            file.write(refresh_token)
            return refresh_token


    @staticmethod       # read
    def read_refresh_token(refresh_token):
        with open(f"{os.getcwd()}/api/txt/user/refresh_token.txt", "r") as file:
            f = file.read(refresh_token)
            return f