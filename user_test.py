import unittest
from user import User

class TestUser(unittest.TestCase):

    """
    Test class which will define test cases for the User class behaviours
    """

    def setUp(self):
        """
        This method runs before each test case.
        """
        self.new_user = User("Anthony", "Njuguna", "Antavio", "password")

    def test_init(self):
        """
        Testing if the object is initialized the correct way
        """
        self.assertEqual(self.new_user.firstname,"Anthony")
        self.assertEqual(self.new_user.secondname, "Njuguna")
        self.assertEqual(self.new_user.username, "Antavio")
        self.assertEqual(self.new_user.password, "password")

    def test_save_user(self):
        """
        Testing if the object is saved into users_list
        """
        self.new_user.saveUser()
        self.assertEqual(len(User.users_list),1)

if __name__ == '__main__':
    unittest.main()