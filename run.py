#!/usr/bin/env python3.6

from user import User
from user_credentials import User_Credentials


def create_user(f_name, l_name, u_name, p_word):
    """
    A function that creates a new user
    """
    new_user = User(f_name, l_name, u_name, p_word)
    return new_user


def create_credential(platform, f_name, s_name, u_name, p_number, email, p_word):
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


def save_user(user):
    """
    Function to save a user
    :param user:
    """
    user.saveUser()


def save_credential(credential):
    """
    Function to save a credential
    :param credential
    """
    credential.saveCredentials()


def delete_credential(credential):
    """
    A function to delete a user
    :param credential:
    """
    credential.delete_account_credentials()


def find_credential(platform):
    """
    A function that a finds a user credential
    :param platform:
    :return: that specific credential
    """
    return User_Credentials.find_credentials_by_platform(platform)

def check_existing_user(password):
    """
    A function to check if a user exists using the password
    :param password:
    :return: Boolean
    """
    return User.user_exists(password)


def check_existing_credential(platform):
    """
    A function to check if a credential exists using that particular platform
    :param platform:
    :return: Boolean
    """
    return User_Credentials.credentials_exist(platform)


def display_credentials():
    """
    Function to display all account credentials
    :return: All saved credentials
    """
    return User_Credentials.display_credentials()