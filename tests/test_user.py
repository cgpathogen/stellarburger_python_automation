from utils.api.user import TestUser

class TestUserMethods:

    def test_sending_empty_request(self):
        TestUser.test_send_empty_request()


    def test_sending_half_request(self):
        TestUser.test_send_half_request()


    def test_user_lifecycle(self):
        TestUser.test_create_user()
        TestUser.test_authorization_with_wrong_password()
        TestUser.test_authorization()
        TestUser.test_get_info_about_user()
        TestUser.test_update_user_info()
        TestUser.test_delete_user()


    def test_create_existing_user(self):
        TestUser.test_create_user()
        TestUser.test_creating_of_existing_user()


    def test_reauthorization(self):
        TestUser.test_create_user()
        TestUser.test_authorization()
        TestUser.test_logout()
        TestUser.test_authorization()