from tkinter import *
from tkinter import messagebox
import mysql.connector

# **************************************************************************************
""" This Part is for forget password"""


def forget_pass():
    # Functionality Parts
    def change_password():
        if user_entry.get() == '' or newpass_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('Error', 'All Fields Are Required', parent=window)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Error', 'Password And Confirm Password Mismatch', parent=window)
        else:
            con = mysql.connector.connect(host='localhost', user='root', password='Monica123@#', database='user_data')
            mydb = con.cursor()

            # This section of username is not working, i will fix it later
            """query = " SELECT * from data where username=%s"
            mydb.execute(query, (user_entry.get()))
            row = mydb.fetchone()
            if row is None:
                messagebox.showerror("Error", 'Incorrect Username', parent=window)
            else:"""
            query = 'update data set password=%s where username=%s'
            mydb.execute(query, (newpass_entry.get(), user_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", 'Password Reset, Please Login with New Password', parent=window)
            window.destroy()

    # Forget password GUI
    window = Toplevel()
    window.title('Change Password')

    backgroundImage = PhotoImage(file="images/forgetbg.png")
    backgroundLabel = Label(window, image=backgroundImage)
    backgroundLabel.grid(row=0, column=0)
    window.resizable(False, False)

    # create a frame2
    frame = Frame(window, bg='white')
    frame.place(x=455, y=35)
    # heading section
    heading_label = Label(frame, text="RESET PASSWORD", font=("Goudy Old style", 18, "bold"),
                          fg="blue", bg="white")
    heading_label.grid(row=0, column=0, padx=12, pady=12)
    # Username Label
    userLabel = Label(frame, text='Username', font=("Goudy Old style", 15, "bold")
                      , bg="white", fg='black')
    userLabel.grid(row=1, column=0, sticky='w', padx=25)
    # Username entry1
    user_entry = Entry(frame, width=30, font=("Goudy Old style", 11, "bold")
                       , fg='magenta2', bd=2)
    user_entry.grid(row=2, column=0, sticky='w', padx=25, pady=10)

    # New Password Label
    passwordLabel = Label(frame, text='New Password', font=("Goudy Old style", 15, "bold")
                          , bg="white", fg='black')
    passwordLabel.grid(row=3, column=0, sticky='w', padx=25)
    # Password Entry
    newpass_entry = Entry(frame, width=30, font=("Goudy Old style", 11, "bold")
                          , fg='magenta2', bd=2)
    newpass_entry.grid(row=4, column=0, sticky='w', padx=25, pady=10)

    # Confirm Password Label
    conpasswordLabel = Label(frame, text='Confirm Password', font=("Goudy Old style", 15, "bold")
                             , bg="white", fg='black')
    conpasswordLabel.grid(row=5, column=0, sticky='w', padx=25)
    # Confirm Password Entry
    confirmpass_entry = Entry(frame, width=30, font=("Goudy Old style", 11, "bold")
                              , fg='magenta2', bd=2)
    confirmpass_entry.grid(row=6, column=0, sticky='w', padx=25, pady=10)

    # Submit Button

    submitButton = Button(frame, text='Submit', font=("Goudy Old style", 14, "bold"), bd=2, bg='magenta2', fg='white'
                          , activebackground='green', activeforeground='black', width=14, command=change_password)
    submitButton.grid(row=7, column=0, pady=10, padx=12, sticky='s')

    window.mainloop()
    # import forget_password


# ************************************************************************************************


""" This Part is for login users """


def login_users():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror("Error", "All Field Are Required")
    else:
        try:
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Monica123@#'
            )
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established try again')
            return
        # database section
        query = 'use user_data'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid Username or Password ')
        else:
            messagebox.showinfo('Welcome', 'Login Successful')


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


def signup_page():
    login_window.destroy()
    import signup


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

forgetButton = Button(login_window, text="Forget Password?", bd=0, bg='white', fg="blue", activebackground='white'
                      , cursor='hand2', command=forget_pass)
forgetButton.place(x=700, y=250)

# Login Button section

loginButton = Button(login_window, text="Login", font=('Open Sans', 16, 'bold')
                     , fg='white', bg='firebrick1', activeforeground='green',
                     activebackground='firebrick1', cursor='hand2', bd=0, width=16, command=login_users)
loginButton.place(x=600, y=290)

# OR Label section
orLabel = Label(login_window, text='----------OR-----------', font=('Open Sans', 19), fg='white', bg='green')
orLabel.place(x=600, y=340)

# Signup Section
signupLable = Label(login_window, text="Don't have an account", font=('Open Sans', 8, 'bold'), fg='firebrick1',
                    bg='white')
signupLable.place(x=600, y=450)

# Signup Button
signupButton = Button(login_window, text="Create New Account", font=('Open Sans', 8, 'bold underline')
                      , fg='blue', bg='white', activeforeground='blue'
                      , activebackground='firebrick1', cursor='hand2', bd=0, width=17, command=signup_page)
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
