from tkinter import*
import tkinter as tk #import for GUI interface

def authent():
    username = str(username_enter.get())
    password = str(password_enter.get())
    if (username == "randomuser1") and (password == "randompassword"):
        print("Welcome back")
    else:
        print("Incorrect Username or Password")

def exit():
    hello.destroy() #exits the program      

hello = Tk()
hello.geometry('400x300') #error: keep text together for dimension
hello.resizable(False, False)
hello.title('Welcome')
hello.config(bg="#FFDEAD")

intro = tk.Label(hello, text="Welcome to The Login Page",font=("Arial", 12),fg="black",bg="#FFDEAD") #intro
enteruser = tk.Label(hello, text="Enter Username",font=("Arial", 12),fg="black",bg="#FFDEAD") #label for entering username
enterpass = tk.Label(hello, text="Enter Password",font=("Arial", 12),fg="black",bg="#FFDEAD") #label for entering username

empty_l1 = tk.Label(hello,bg="#FFDEAD") 
empty_l2 = tk.Label(hello,bg="#FFDEAD") 
empty_l3 = tk.Label(hello,bg="#FFDEAD") 
empty_l4 = tk.Label(hello,bg="#FFDEAD") 

username_enter = tk.Entry(hello,font=('Arial',10))
password_enter = tk.Entry(hello,font=('Arial',10))

accbutton = tk.Button(hello,text="Enter",font=("Arial", 10),command=authent)
exitbutton = tk.Button(hello,text="Exit Program",font=("Arial", 10),command=exit)

intro.pack()
empty_l1.pack()
enteruser.pack()
username_enter.pack()
empty_l2.pack()
enterpass.pack()
password_enter.pack()
empty_l3.pack()
accbutton.pack()
empty_l4.pack()
exitbutton.pack()


hello.mainloop() 








