import unittest
from user_credentials import User_Credentials

class TestCredentials(unittest.TestCase):

    """
    Test class which will define test cases for the User_Credentials class behaviours
    """
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


if __name__ == '__main__':
    unittest.main()

