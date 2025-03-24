import random
from utils.http_methods import Http_methods
from utils.api.user import TestUser

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
        print(TestIngredients.ingredients_list)


    @staticmethod
    def test_get_unauthorized_user_orders():
        """
        test of attempt to get list of orders
        """
        used_url = TestIngredients.base_url + TestIngredients.order
        request = Http_methods.get(used_url)
        print(request.json())
        assert request.status_code == 401
        print("Success - couldn't get user's order list, authorization required")


    @staticmethod
    def test_get_authorized_user_orders():
        """
        test of attempt to get list of orders
        """
        used_url = TestIngredients.base_url + TestIngredients.order
        request = Http_methods.get(used_url, TestUser.read_bearer_token())
        print(request.json())
        assert request.status_code == 200
        print(f"Success - user's list of orders - {request.json()}")


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
    def test_place_order():
        """
        test placing order by authorized user
        """
        global json, ids_list
        used_url = TestIngredients.base_url + TestIngredients.order
        ids_list = random.sample(TestIngredients.ingredients_list,3)
        json = {
            "ingredients": [*ids_list]
        }
        request = Http_methods.post(used_url,json)
        print(request.json())
        assert request.status_code == 200