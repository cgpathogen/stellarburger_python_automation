from utils.api.user import TestUser

class TestUserMethods:

    def test_user_lifecycle(self):

        TestUser.test_send_empty_request()
        TestUser.test_send_half_request()
        TestUser.test_create_user()
        TestUser.test_authorization_with_wrong_password()
        TestUser.test_authorization()
        TestUser.test_get_info_about_user()
        TestUser.test_update_user_info()
        TestUser.test_delete_user()



test = TestUserMethods()
test.test_user_lifecycle()