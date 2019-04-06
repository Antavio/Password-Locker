import unittest
from user_credentials import User_Credentials

class TestCredentials(unittest.TestCase):

    """
    Test class which will define test cases for the User_Credentials class behaviours
    """
    def tearDown(self):
        """
        tearDown method that cleans up after each test case has run.
        """
        User_Credentials.user_credential_list = []

    def setUp(self):
        """
        This method runs before each test case.
        """
        self.new_user_credential = User_Credentials("Facebook", "Anthony", "Njuguna", "Antavio", "0723308037", "njuguna13@gmail.com", "password")

    def test_init(self):
        """
        Testing if the object is initialized the correct way
        """
        self.assertEqual(self.new_user_credential.platform, "Facebook")
        self.assertEqual(self.new_user_credential.firstname, "Anthony")
        self.assertEqual(self.new_user_credential.secondname, "Njuguna")
        self.assertEqual(self.new_user_credential.username, "Antavio")
        self.assertEqual(self.new_user_credential.phone_number, "0723308037")
        self.assertEqual(self.new_user_credential.email, "njuguna13@gmail.com")
        self.assertEqual(self.new_user_credential.password, "password")

    def test_save_user_credentials(self):
        """
        Testing if the object is saved into user_credential_list
        """
        self.new_user_credential.saveCredentials()
        self.assertEqual(len(User_Credentials.user_credential_list), 1)

    def test_save_multiple_credentials(self):
        """
        Test to see if the app can save multiple account credentials
        """
        self.new_user_credential.saveCredentials()
        test_user_credentials = User_Credentials("TestPlatform", "TestFirst", "TestLast", "UserTest", "0700123654", "nm@mail.com", "pd123")
        test_user_credentials.saveCredentials()
        self.assertEqual(len(User_Credentials.user_credential_list), 2)


    def test_delete_user_credentials(self):

        """
        This is to test if the app can remove account credentials from the user credentials list
        """
        self.new_user_credential.saveCredentials()
        test_user_credentials = User_Credentials("TestPlatform", "TestFirst", "TestLast", "UserTest", "0700123654",
                                                 "nm@mail.com", "pd123")
        test_user_credentials.saveCredentials()

        self.new_user_credential.delete_account_credentials()
        self.assertEqual(len(User_Credentials.user_credential_list), 1)

    def test_find_credentials_by_platform(self):
        """
        test to check if we can find user credentials using the respective platforms
        """
        self.new_user_credential.saveCredentials()
        test_user_credentials = User_Credentials("TestPlatform", "TestFirst", "TestLast", "UserTest", "0700123654",
                                                 "nm@mail.com", "pd123")
        test_user_credentials.saveCredentials()

        found_account = User_Credentials.find_credentials_by_platform("TestPlatform")

        self.assertEqual(found_account.phone_number, test_user_credentials.phone_number)

    def test_credentials_exists(self):

        """
        Test to check if credentials exists
        """
        self.new_user_credential.saveCredentials()
        test_user_credentials = User_Credentials("TestPlatform", "TestFirst", "TestLast", "UserTest", "0700123654",
                                                 "nm@mail.com", "pd123")
        test_user_credentials.saveCredentials()

        credentials_exist = User_Credentials.credentials_exist("TestPlatform")
        self.assertTrue(credentials_exist)

    def test_display_all_credentials(self):
        """
        This method returns a list of user credential accounts
        """
        self.assertEqual(User_Credentials.display_credentials(), User_Credentials.user_credential_list)


if __name__ == '__main__':
    unittest.main()

