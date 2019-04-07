#!/usr/bin/env python3.6

from user import User
from user_credentials import User_Credentials
import random


def create_user(f_name, l_name, u_name, p_word):
    """
    A function that creates a new user
    """
    new_user = User(f_name, l_name, u_name, p_word)
    return new_user


def create_credential(platform, fc_name, sc_name, uc_name, pc_number, email, pc_word):
    """
    Function to create a credential account
    :param platform: 
    :param fc_name:
    :param sc_name:
    :param uc_name:
    :param pc_number:
    :param email:
    :param pc_word:
    :return: new credential object
    """
    new_user_credential = User_Credentials(platform, fc_name, sc_name, uc_name, pc_number, email, pc_word)
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

    print(f"Hello {account_name}. \n Please use the following short code menu to continue \n")

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

            if check_existing_user(p_word):
                print(f"\n Welcome back {u_name}")
                print("You can now create and save your credentials")
                print('*'*30)

                print("\n Which social media platform account do you want to create?")
                print('*' * 30)
                platform = input()

                print("\n Enter your first name for this Account")
                print('*' * 30)
                fc_name = input()

                print("\n Enter your second name for this Account")
                print('*' * 30)
                sc_name = input()

                print("\n Enter Username  for this Account")
                print('*' * 30)
                uc_name = input()

                print("\nPress  cp - to create your own password OR  gp - to automatically generate password\n")
                print('#' * 30)
                password_choice = input()

                if password_choice == 'cp':
                    print("\nEnter Password")
                    pc_word = input()

                elif password_choice == 'gp':
                    characters = "AbcdefghijKLmnopqrstuvWXYZ0123456789"
                    pc_word = "".join(random.choice(characters) for _ in range(8))
                    print(f"The generated Password is: {pc_word}\n")

                print("\n Enter phone number")
                print('*' * 30)
                pc_number = input()

                print("\n Enter e-mail")
                print('*' * 30)
                email = input()



                save_credential(create_credential(platform, fc_name, sc_name, uc_name, pc_number, email, pc_word))
                print(f"\n A new account for {platform} has been successfully Created")

            else:
                print("\n You Entered wrong credentials")
                print("\n Re-Enter your username")
                print("*" * 50)
                print("\n Username:::")
                print("*" * 15)
                u_name = input()
                print("\n Password:::")
                print("*" * 15)
                p_word = input()
                if check_existing_user(p_word):
                    print("\n Login successful")

                else:
                    print("\n Seems you have not Registered")

        elif short_code == 'dc':
            if display_credentials():
                print("\n Your Current Account Credentials are:")
                print("*"*50)

                for cred in display_credentials():
                    print(f"Platform {cred.platform} \n First Name: {cred.firstname} \t Second Name: {cred.secondname} \tUsername: {cred.username}"
                          f"\t Phone number: {cred.phone_number}\t Email: {cred.email} \t Password: {cred.password}")
            else:
                print("\n No Credentials saved yet")

        elif short_code == 'lo':
            print("\n You have logged out")
            print("*"*40)
            break

        else:
            print("\n Seems you entered a wrong short code")


if __name__ == '__main__':
    main()
