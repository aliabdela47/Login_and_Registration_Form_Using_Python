from tkinter import *
import mysql.connector
from tkinter import messagebox


# Functionality function part

# delete entries after registered
def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmpasswordEntry.delete(0, END)
    check.set(0)


# Registration entry configuration and database connectivity

def connect_database():
    if emailEntry.get() == '' or passwordEntry.get() == '' or usernameEntry.get() == '' or confirmpasswordEntry.get() == '':
        messagebox.showerror("Error", "All Fields Are Required")
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror("Error", "Password Not Equal")
    elif check.get() == 0:
        messagebox.showerror("Error", "Please Accept Terms & Conditions")
    else:
        try:
            con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Monica123@#'
            )
        except:
            messagebox.showerror("Error", "Database Connection Problem, Please  Try Later")
            return

        mydb = con.cursor()

        # To create database
        try:
            query = 'create database user_data'
            mydb.execute(query)
            query = 'use user_data'
            mydb.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50),' \
                    ' username varchar(100), password varchar(20))'
            mydb.execute(query)
        except:
            mydb.execute('use user_data')

            # Not to register same username to be fixed
            """query = 'select * from data where username=%s'
            mycursor.execute(query, (usernameEntry.get()))

            row = mycursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Username Already Exist")"""

            # To insert the data into the table
            # else:
            query = 'insert into data(email,username,password) values(%s, %s, %s)'
            mydb.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            # commit our changes
            con.commit()
            # disconnect the connection
            con.close()
            # display
            messagebox.showinfo("Congrats", "The Registration is Successful")
            # delete the entry
            clear()
            # close signup window
            signup_window.destroy()
            import user_login


def login_page():
    signup_window.destroy()
    import user_login


signup_window = Tk()

signup_window.title("Signup Form")
signup_window.resizable(False, False)
backgroundImage = PhotoImage(file="images/background.png")
backgroundLabel = Label(signup_window, image=backgroundImage)
backgroundLabel.grid(row=0, column=0)

# create a frame

frame = Frame(signup_window, bg='white')
frame.place(x=454, y=25)
# heading section
heading = Label(frame, text="CREATE AN ACCOUNT", font=("Open Sans", 18, "bold"), bd=0, fg="red", bg="white")

heading.grid(row=0, column=0, padx=10, pady=10)

# Email Label
emailLabel = Label(frame, text='Email', font=("Open Sans", 10, "bold")
                   , bg="white", fg='blue')
emailLabel.grid(row=1, column=0, sticky='w', padx=25)

# Email entry
emailEntry = Entry(frame, width=30, font=("Open Sans", 10, "bold")
                   , bg='red', fg='white')
emailEntry.grid(row=2, column=0, sticky='w', padx=25, pady=(10, 0))

# Username Label
usernameLabel = Label(frame, text='Username', font=("Open Sans", 10, "bold")
                      , bg="white", fg='blue')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25)

# Username entry
usernameEntry = Entry(frame, width=30, font=("Open Sans", 10, "bold")
                      , bg='red', fg='white')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25, pady=(10, 0))

# Password Label
passwordLabel = Label(frame, text='Password', font=("Open Sans", 10, "bold")
                      , bg="white", fg='blue')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25)

# Password entry
passwordEntry = Entry(frame, width=30, font=("Open Sans", 10, "bold")
                      , bg='red', fg='white')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25, pady=(10, 0))

# Confirm Password Label
confirmpasswordLabel = Label(frame, text='Confirm Password', font=("Open Sans", 10, "bold")
                             , bg="white", fg='blue')
confirmpasswordLabel.grid(row=7, column=0, sticky='w', padx=25)

# Confirm Password entry
confirmpasswordEntry = Entry(frame, width=30, font=("Open Sans", 10, "bold")
                             , bg='red', fg='white')
confirmpasswordEntry.grid(row=8, column=0, sticky='w', padx=25, pady=(10, 0))

# check button
check = IntVar()
termsandconditions = Checkbutton(frame, text='I agree to the Terms & Conditions', font=("Open Sans", 9, "bold")
                                 , bg='white', fg='black', activebackground='white', activeforeground='black',
                                 cursor='hand2',
                                 variable=check)
termsandconditions.grid(row=9, column=0, pady=10, padx=15, sticky='w')

# Signup Button
signupButton = Button(frame, text='Signup', font=("Open Sans", 15, "bold"), bd=0, bg='firebrick1', fg='white'
                      , activebackground='firebrick1', activeforeground='white', width=19, command=connect_database)
signupButton.grid(row=10, column=0, pady=12, padx=15, sticky='w')

# Dont have an Account section

alreadyAccount = Label(frame, text="Don't have an account?", font=("Open Sans", 9, "bold"), bg='white',
                       fg='black')
alreadyAccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

# Login Button
loginButton = Button(frame, text='Login', font=("Open Sans", 9, "bold underline"), bd=0, bg='white', fg='blue'
                     , activebackground='white', activeforeground='blue', cursor='hand2', command=login_page)
loginButton.place(x=170, y=376)

signup_window.mainloop()
