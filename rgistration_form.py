from tkinter import *
from tkinter import messagebox


# Functionality part
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def pass_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

# hide eye function


def hide():
    openeye.config(file='images/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='images/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

# GUI part

login_window = Tk()
# login_window.geometry("990x660+150+150")
login_window.title("login_window Form")
login_window.resizable(False, False)
bgImage = PhotoImage(file="images/bg.png")
bgLabel = Label(login_window, image=bgImage)
bgLabel.grid(row=0, column=0)
# bgLabel.place(x=0, y=0)
bgLabel.pack()

heading = Label(login_window, text="USER'S LOGIN", font=("Open Sans", 22, "bold"), bd=0, fg="red", bg="white")

heading.place(x=600, y=110)

# Username entry
usernameEntry = Entry(login_window, width=25, font=("Impact", 11), fg="#154c79", bg="white", bd=0)
usernameEntry.place(x=600, y=170)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

# frame line 1
frame1 = Frame(login_window, width=205, height=2, bg="firebrick1")
frame1.place(x=600, y=195)

# password entry

passwordEntry = Entry(login_window, width=25, font=("Impact", 11), fg="#154c79", bg="white", bd=0)
passwordEntry.place(x=600, y=210)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', pass_enter)

# frame line 2
frame2 = Frame(login_window, width=205, height=2, bg="firebrick1")
frame2.place(x=600, y=230)

# open eye part
openeye = PhotoImage(file="images/openeye.png")
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white',
       cursor="hand2", command=hide)
eyeButton.place(x=800, y=210)

# forget button part

forgetButton = Button(login_window, text="Forget Password?", bd=0, fg="blue", activebackground='white'
                      ,cursor='hand2')
forgetButton.place(x=600, y=250)

loginButton = Button(login_window, text="Login", font=('Open Sans', 16, 'bold')
                     , fg='white', bg='firebrick1', activeforeground='green'
                     ,activebackground='firebrick1', cursor='hand2',bd=0, width=16)
loginButton.place(x=600, y=290)

orLabel = Label(login_window, text='----------OR-----------', font=('Open Sans', 19), fg='white', bg='green')
orLabel.place(x=600, y=340)

signupLable = Label(login_window, text="Don't have an account", font=('Open Sans', 8, 'bold'), fg='firebrick1',bg='white')
signupLable.place(x=600, y=450)

signupButton = Button(login_window, text="Create New Account", font=('Open Sans', 8, 'bold underline')
                     , fg='white', bg='green', activeforeground='blue'
                     ,activebackground='firebrick1', cursor='hand2',bd=0, width=17)
signupButton.place(x=725, y=450)

# facebook logo part
facebookLogo = PhotoImage(file="images/facebook.png")
fbLabel = Label(login_window, image=facebookLogo, bg='white')
fbLabel.place(x=630, y=380)

# Twitter logo part
twitterLogo = PhotoImage(file="images/twitter.png")
twLabel = Label(login_window, image=twitterLogo, bg='white')
twLabel.place(x=680, y=380)

# google logo part
googleLogo = PhotoImage(file="images/google.png")
goLabel = Label(login_window, image=googleLogo, bg='white')
goLabel.place(x=730, y=380)


login_window.mainloop()
