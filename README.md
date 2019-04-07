# Password-Locker Application

## Author
[Anthony Njuguna Kiarie](https://github.com/Antavio)

## Project Description
This is a Python project that helps a user score their different account credentials which may include Facebook, Instagram, Twitter, Google+ etc.
In addition the user has the option of putting in a password for the new credential or have one generated for them. Finally a user can be able 
to view all their credentials in one place.

### Project Setup instructions
Use the following commands to use this project.
- install python 3
- git clone https://github.com/Antavio/Password-Locker.git
- cd Password-Locker
- atom .  //For those using atom text editor.
- code .  //For those using Visual Studio editor.

To run this project in your local machine 
1. Give executable rights to the run.py file by running `chmod +x run.py` on the terminal
2. Run `./run.py` to start interacting with the program.

### Technologies used
The different technologies that were used to develop this program include:
1. Python 3.6

### Project's BDD
| Behaviour/Input | Expected Output |
|-----------|-----------------|
| When the user first interacts with the application User is prompted to enter their name| Welcome message including name of the user|
|User is provided with a menu| User should choose the action they prefer from the Menu|
|When user chooses rg  | User prompted to enter their details to create an account |
|User chooses cc | User is required to login using Username & password    |
| User prompted to enter credentials information they want to store after pressing cc | User enters all the relevant info. An alert message for successful creation of an account is displayed |
|The app prompts user to create or generate a password | If user chooses cp - they can create their own password else the program generates a password|
| User presses dc          | A list of all credentials is displayed |
| User presses lo          | The program logs the user out |
| User chooses non existence short code | Program display wrong input message for the user|

### Contact Me
If you have any suggestions, additions or modifications on this project you can reach me via my email: njuguna13@gmail.com

### License  & Copyright information
Copyright (c) 2019 Anthony Njuguna

[MIT License](./LICENSE)