from tkinter import *
from tkinter import messagebox

"""incase of jpg photo import the command"""


# from PIL import imageTK
# pip install pillow


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        """name the form"""
        self.root.geometry("1199x600+100+50")
        """give diamension of the form, lenght width and high"""
        self.root.resizable(False, False)
        """disable resizable"""

        # Background image
        # self.bg =ImageTK.PhotoImage(file="images/pic.jpg")
        self.bg = PhotoImage(file="images/pic22.png")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=330, y=150, width=500, height=370)

        # Title & subtitle
        title = Label(frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#e28743", bg="white").place(x=90,
                                                                                                                   y=30)
        subtitle = Label(frame_login, text="User Login", font=("Goudy old style", 15, "bold"), fg="#21130d",
                         bg="white").place(x=90, y=100)
        # Username
        lbl_user = Label(frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey",
                         bg="white").place(x=90, y=140)

        # Entry part
        self.username = Entry(frame_login, font=("Goudy old style", 15), fg="#063970", bg="white")
        self.username.place(x=90, y=170, width=320, height=35)

        # Password
        lbl_password = Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",
                             bg="white").place(x=90, y=210)
        self.password = Entry(frame_login, font=("Goudy old style", 15), fg="#063970", bg="white")
        self.password.place(x=90, y=240, width=320, height=35)

        # Button
        forget = Button(frame_login, text="forget password", bd=0, font=("Goudy old style", 12), fg="#700639",
                        bg="white").place(x=90, y=280)
        submit = Button(frame_login,command=self.check_function, cursor="hand2", text="Login", bd=0,
                        font=("Goudy old style", 15), bg="#700639", fg="white").place(
            x=90, y=320, width=180, height=40)

        # we have to make our form functional
    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get() != "Akoatem79" or self.password.get() != "123456":
            messagebox.showerror("Error", "invalid name or password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome{self.username.get()}")


root = Tk()
obj = Login(root)
root.mainloop()
