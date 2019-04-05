class User:
    """
    Class that generates new instances of users
    """
    def __init__(self,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: New user username.
            password : New user password.
        '''

        self.username = username
        self.password = password