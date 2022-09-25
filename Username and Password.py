from tkinter import* #import for GUI interface

def login():
    username_enter = input("Please enter username: \n")
    password_enter = input("Please enter password: \n")


def authent():
    if (username_enter == "randomuser1") and (password_enter == "randompassword"):
        print("Welcome back")
    else:
        print("Incorrect Username or Password")
        

hello = Tk()
hello.geometry('400x300') #error: keep text together for dimension
hello.resizable(False, False)
hello.title('Welcome')
hello.config(bg="#FFDEAD")


intro = Label(
    hello, 
    text = "Welcome to the Login Page",
    font = ("Arial", 12),
    fg = "black",
    bg = "#FFDEAD"
).place(
    x = 95,
    y = 0
)

enterusername = Label(
    hello,
    text = "Enter username: ",
    font = ("Arial", 10),
    fg = "black",
    bg = "#FFDEAD"
).place(
    x = 10,
    y = 60
)

enterpassword = Label(
    hello,
    text = "Enter password: ",
    font = ("Arial", 10),
    fg = "black",
    bg = "#FFDEAD"
).place(
    x = 10,
    y = 120
)

username_enter = StringVar()  
password_enter = StringVar()  

usernamebox = Entry(
    hello,
    textvariable = username_enter,
    bg = "#E5E5E5",
    width = 20,  
    font = (20)
    ).place(
        x= 120,
        y = 60
    )

passwordbox = Entry(
    hello,
    textvariable = password_enter,
    bg = "#E5E5E5",
    width = 20,  
    font = (20)
    ).place(
        x= 120,
        y = 120
    )

submit = Button(
    hello,
    command= authent,
    text = "Enter",  
    fg = "white",  
    bg = "#A0522D",  
    width = 15,  
    font=20
). place(
    x = 100, 
    y = 200
)

hello.mainloop() 
