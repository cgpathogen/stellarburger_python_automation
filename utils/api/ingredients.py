import requests

from utils.http_methods import Http_methods

class TestIngredients:

    base_url = "https://stellarburgers.nomoreparties.site"
    all_ingredients = "/api/ingredients"
    order = "/api/orders"


    @staticmethod
    def test_get_all_ingredients():
        used_url = TestIngredients.base_url+TestIngredients.all_ingredients
        request = requests.get(used_url)
        assert request.status_code == 200
        assert request.json()['success'] == True
        print("Ingredients list received")



    @staticmethod
    def test_order_by_unauthorized_uer():
        used_url = TestIngredients.base_url + TestIngredients.order
        json = {
            "ingredients": []
        }
        request = requests.post(used_url,json)
        assert request.status_code == 401


    @staticmethod
    def test_place_empty_order():
        used_url = TestIngredients.base_url + TestIngredients.order
        json = {
            "ingredients": []
        }
        request = requests.post(used_url,json)
        assert request.status_code == 400