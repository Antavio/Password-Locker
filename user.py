class User:
    """
    Class that generates new instances of users
    """
    users_list = []
    def __init__(self,firstname,secondname,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: New user username.
            password : New user password.
        '''

        self.firstname = firstname
        self.secondname = secondname
        self.username = username
        self.password = password

    def saveUser(self):
        """
        This Method saves user objects into  users_list array
        """
        User.users_list.append(self)