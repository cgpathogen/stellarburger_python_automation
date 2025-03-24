from utils.api.user import TestUser
from utils.api.ingredients import TestIngredients

class TestOrders:

    def test_get_orders_without_authorization(self):
        TestIngredients.test_get_unauthorized_user_orders()


    def test_place_order_without_ingredients(self):
        TestIngredients.test_place_empty_order()


    def test_create_order(self):
        TestUser.test_create_user()
        TestUser.test_authorization()
        TestIngredients.test_get_all_ingredients()
        TestIngredients.test_place_order() # create first burger
        TestIngredients.test_place_order() # create another burger
        TestIngredients.test_get_authorized_user_orders()