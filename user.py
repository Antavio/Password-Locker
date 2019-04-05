class User:
    """
    Class that generates new instances of users
    """
    def __init__(self,firstname,secondname,username,password):

        users_list = []

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