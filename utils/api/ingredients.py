import random

import requests

from utils.http_methods import Http_methods

class TestIngredients:
    #urls
    base_url = "https://stellarburgers.nomoreparties.site"
    all_ingredients = "/api/ingredients"
    order = "/api/orders"

    #lists
    ingredients_list = []


    @staticmethod
    def test_get_all_ingredients():
        """
        test getting all available ingredients
        """
        used_url = TestIngredients.base_url+TestIngredients.all_ingredients
        request = Http_methods.get(used_url)
        assert request.status_code == 200
        assert request.json()['success'] == True
        for item in request.json()['data']:
            TestIngredients.ingredients_list.append(item["_id"]) #collect all ids to list for further using
        print("Ingredients list received, ids were saved")


    @staticmethod
    def test_get_unauthorized_user_orders():
        """
        test of attempt to get list of orders without passing authorization, expected status code - 401
        """
        used_url = TestIngredients.base_url + TestIngredients.order
        request = Http_methods.get(used_url)
        print(request.json())
        assert request.status_code == 401
        print("Success, couldn't get set of orders without authorization")



    @staticmethod
    def test_place_empty_order():
        """
        test of attempt to save an empty order
        """
        used_url = TestIngredients.base_url + TestIngredients.order
        json = {
            "ingredients": []
        }
        request = Http_methods.post(used_url,json)
        print(request.json())
        assert request.status_code == 400
        assert request.json()['success'] == False


    @staticmethod
    def place_order():
        """
        test placing order by authorized user
        """
        global json, ids_list
        used_url = TestIngredients.base_url + TestIngredients.order
        for n in range(3):
            ids_list = []
            ids_list.append(random.choice(ids_list))
        json = {
            "ingredients": [*ids_list]
        }
        request = Http_methods.post(used_url,json)
