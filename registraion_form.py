from tkinter import *


def get_vals():
    print("Accepted")


class Registration:
    def __init__(self, root):
        self.root = root

        # background image
        self.bg = PhotoImage(file="images/pic22.png")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        # create heading
        Label(root, text="User's Registration Form", font="ar 15 bold").grid(row=0, column=3)

        # create variables field names
        name = Label(root, text="Name")
        phone = Label(root, text="Phone")
        gender = Label(root, text="Gender")
        address = Label(root, text="Address")
        paymentmode = Label(root, text="Payment Mode")

        # Back the variables up
        name.grid(row=1, column=2)
        phone.grid(row=2, column=2)
        gender.grid(row=3, column=2)
        address.grid(row=4, column=2)
        paymentmode.grid(row=5, column=2)

        # create variable to store feeds
        namevalue = StringVar
        phonevalue = StringVar
        gendervalue = StringVar
        addressvalue = StringVar
        paymentmodevalue = StringVar
        checkvalue = IntVar

        # create entry
        nameentry = Entry(root, textvariable=namevalue)
        phoneentry = Entry(root, textvariable=phonevalue)
        genderentry = Entry(root, textvariable=gendervalue)
        addressentry = Entry(root, textvariable=addressvalue)
        paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

        # back our entry
        nameentry.grid(row=1, column=3)
        phoneentry.grid(row=2, column=3)
        genderentry.grid(row=3, column=3)
        addressentry.grid(row=4, column=3)
        paymentmodeentry.grid(row=5, column=3)

        # create check button
        checkbtn = Checkbutton(text="remember me?", variable=checkvalue)
        checkbtn.grid(row=6, column=4)

        # submit button

        Button(text="Submit Registration", command=get_vals, cursor="hand2").grid(row=7, column=3)


root = Tk()
obj = Registration(root)
root.mainloop()
