#!/usr/bin/env python3.6

from user import User
from user_credentials import User_Credentials

def create_user(f_name, l_name, u_name, p_word):
    """
    A function that creates a new user
    """
    new_user = User(f_name, l_name, u_name, p_word)
    return new_user

def create_credential(platform, f_name, s_name, u_name, p_number, email, p_word)
    """
    Function to create a credential account
    :param platform: 
    :param f_name: 
    :param s_name: 
    :param u_name: 
    :param p_number: 
    :param email: 
    :param p_word: 
    :return: new credential object
    """
    new_user_credential = User_Credentials(platform, f_name, s_name, u_name, p_number, email, p_word)
    return  new_user_credential