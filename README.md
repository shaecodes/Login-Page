# Login Page GUI Application
This is a simple login page GUI application implemented in Python using the Tkinter library. It provides a graphical user interface for users to enter their username and password, and then click the "Enter" button to authenticate. If the entered username and password match the predefined values, it displays a "Welcome back" message. Otherwise, it shows an "Incorrect Username or Password" message and plays a sound effect using the winsound library.

# Prerequisites
Python 3.2 installed on your machine 
Tkinter library (usually included with Python)
Winsound library (can be installed using pip)

# How to Run
Clone or download the repository to your local machine.
Open the terminal/command prompt and navigate to the directory where the code is saved.
Run the following command to execute the program: python login_page.py
The login page window will open with dimensions set to 400x300 pixels, and you can enter the predefined username and password for authentication.
Click the "Enter" button to authenticate. If the username and password are correct, it will display a "Welcome back" message. Otherwise, it will show an "Incorrect Username or Password" message and play a sound effect.
You can also click the "Exit Program" button to close the application.

# Customization
You can customize the code by modifying the values of predefined username and password in the authent() function, as well as the path to the sound effect file in the ws.PlaySound() function.

# License
This project is licensed under the MIT License which allows you to use, modify, and distribute the code for both personal and commercial purposes.
