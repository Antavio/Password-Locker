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