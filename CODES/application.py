from tkinter import*

win = Tk()

class user:
    def __init__(self,fname,lname,email,passw):
        self.firstName = fname
        self.lastName = lname
        self.email = email
        self.password = passw

userList = []

w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.geometry(f"{w}x{h}")


#login frame
def login():

    loginframe =Frame(win,height=500,width=500,bg="lightblue")
    loginframe.place(x=500,y=100)

    loginhead = Label(loginframe,text="LOG IN",font="arial 24 bold",bg="lightblue")
    loginhead.place(x=200,y=10)

    email = Label(loginframe,text="EMAIL :",font="arial 16 bold",bg="lightblue")
    email.place(x=70,y=120)
    eentry = Entry(loginframe,width=40)
    eentry.place(x=70,y=170)

    password = Label(loginframe,text="PASSWORD :",font="arial 16 bold",bg="lightblue")
    password.place(x=70,y=250)
    pentry = Entry(loginframe,width=40)
    pentry.place(x=70,y=300)

    def logincheck():
        emailValue = eentry.get()
        passwordValue = pentry.get()

        for person in userList:
            if emailValue == person.email and passwordValue == person.password:
                print("User Found")
            else:
                print("User Not Found")


    loginbtn = Button(loginframe,text="LOG IN",font="arial 12 bold",command=logincheck)
    loginbtn.place(x=270,y=400)

    def singinframopen():
        loginframe.destroy()
        singin()

    singinbtn = Button(win,text="SING IN",font="arial 12 bold",command=singinframopen)
    singinbtn.place(x=650,y=500)


# singin form

def singin():

    global singinrame
    singinframe =Frame(win,height=500,width=700,bg="gray")
    singinframe.place(x=500,y=100)

    singinhead = Label(singinframe,text="SING IN",font="arial 24 bold",bg="gray")
    singinhead.place(x=280,y=30)

    fname = Label(singinframe,text="FIRST NAME :",font="arial 16 bold",bg="gray")
    fname.place(x=70,y=120)
    fentry = Entry(singinframe,width=40)
    fentry.place(x=70,y=160)

    lname = Label(singinframe,text="LAST NAME :",font="arial 16 bold",bg="gray")
    lname.place(x=350,y=120)
    lentry = Entry(singinframe,width=40)
    lentry.place(x=350,y=160)

    email = Label(singinframe,text="EMAIL :",font="arial 16 bold",bg="gray")
    email.place(x=70,y=210)
    eentry = Entry(singinframe,width=60)
    eentry.place(x=70,y=250)

    password = Label(singinframe,text="password :",font="arial 16 bold",bg="gray")
    password.place(x=70,y=310)
    pentry = Entry(singinframe,width=60)
    pentry.place(x=70,y=350)

    def submit():
        fname = fentry.get()
        lname = lentry.get()
        email = eentry.get()
        passw = pentry.get()

        u1 = user(fname,lname,email,passw)
        userList.append(u1)

        fentry.delete(0,END)
        lentry.delete(0,END)
        eentry.delete(0,END)
        pentry.delete(0,END)

        print(len(userList))

    singinbtn = Button(win,text="SING IN",font="arial 12 bold",command=submit)
    singinbtn.place(x=920,y=530)

    account = Label(singinframe,text="Having an Account?",font="arial 14 bold",bg="gray")
    account.place(x=100,y=430)

    def click():
        singinframe.destroy()
        login()

    loginbtn = Button(singinframe,text="Log In",font="arial 12 bold",command=click)
    loginbtn.place(x=320,y=430)

login()

win.mainloop()