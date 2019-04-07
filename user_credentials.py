class User_Credentials:

    """
    Class that generates new instances of user credentials
    """
    user_credential_list = []

    def __init__(self, platform, firstname, secondname, username, phone_number, email, password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            platform: Social Media platform
            firstname: New user firstname
            secondname: New user secondname
            username: New user username.
            email: New user email.
            password : New user password.
        '''

        self.platform = platform
        self.firstname = firstname
        self.secondname = secondname
        self.username = username
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def saveCredentials(self):

        """
        This Method saves user objects into  users_list array
        """
        User_Credentials.user_credential_list.append(self)

    def delete_account_credentials(self):
        """
        This method deletes a saved account from the users_list
        """
        User_Credentials.user_credential_list.remove(self)

    @classmethod
    def find_credentials_by_platform(cls, platform):
        """
        This methods takes in an account platform & returns user credentials that matches that platform
        """
        for credential in cls.user_credential_list:
            if credential.platform == platform:
                return credential

    @classmethod
    def credentials_exist(cls, platform):
        """
        This Method checks if a Social media account exists
        :param platform:
        :return: boolean depending whether the credentials exists
        """
        for credential in cls.user_credential_list:
            if credential.platform ==platform:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        A method that returns the credential list
        """
        return cls.user_credential_list
