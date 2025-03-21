from utils.api.user import TestUser

class TestUserLifecycle:

    def test_user_lifecycle(self):
        TestUser.test_create_user()
        TestUser.test_authorization()
        TestUser.test_get_info_about_user()
        TestUser.test_update_user_info()
        TestUser.test_delete_user()


test = TestUserLifecycle()
test.test_user_lifecycle()