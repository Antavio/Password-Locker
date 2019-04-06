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
    return new_user_credential


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


def main():
    print("Welcome to the Password Locker Application\n")
    print("What is your name\n")
    account_name = input()

    print(f"Hello {account_name}. Please use the following short code menu to continue \n")

    while True:
        print("Menu: rg - Create Account, cc - create credentials, cp - create password, gp - generate password, "
              "dc - Display Credentials, lo - Logout")
        short_code = input().lower()

        if short_code == 'rg':
            print("New User Account")
            print('*'*20)

            print("Enter First Name")
            f_name = input()

            print("Enter Second Name")
            l_name = input()

            print("Enter your Username")
            u_name = input()

            print("Enter Password")
            p_word = input()

            save_user(create_user(f_name, l_name, u_name, p_word))

            print(f"\n A new account for {f_name} {l_name} has been created successfully \n")

        elif short_code == 'cc':
            print("\n Please Login into  your Account")
            print("*" * 50)
            print("\n Username:::")
            print("*" * 15)
            u_name = input()
            print("\n Password:::")
            print("*" * 15)
            p_word = input()

