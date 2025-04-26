# Python Tkinter Imports

from tkinter import *
from tkinter import messagebox
# from tkinter.ttk import *
from tkinter import ttk
from PIL import Image,ImageTk

window = Tk()

#-----------------------------------------------------------------------------------------------------------
# **** Window ****

# window = Tk()

# window.mainloop()




# **** Label ****

# label = Label(window,text="Label")
# label.pack()




# **** Geometry ****

# window.geometry("200x200")  




# **** Title ****

# window.title("Title1")




#------------------------------------------------------------------------------------------------------------

# Forms


# **** Label ****

# label = Label(window,text="Label")
# label.pack()




# **** Entry ****

# name = Label(window,text="Name :",font=("Georgia 16 bold"))
# name.place(x=10,y=50)

# nameEntry = Entry(window,width=25)
# nameEntry.place(x=200,y=50)




# **** Buttons ****

# btn = Button(window,text="Click here")
# btn.grid(column=1,row=1)




# **** Button Click Event [Functions] ****

# def btnclicked():
#     label = Label(window,text="Button was clicked")
#     label.pack()

# btn = Button(window,text="Click here",command=btnclicked)
# btn.pack()




# **** Text ****

# def gettext():
#     print(text.get("1.0","end-1c")) #UNICODE Value

# btn = Button(window,text="Get Text",command=gettext)
# btn.pack()

# text = Text(window,wrap=WORD)
# text.pack(fill=BOTH,expand=True)




# **** Images ****

#JPG Image
# pil_img = Image.open("pathofImg")
# img_tk = ImageTk.PhotoImage(pil_img)

# Label = Label(window,image=img_tk)
# Label.pack()

#PNG Image
# img = PhotoImage(file="pathofImg")

# Label2 = Label(window,image=img)
# Label2.grid(row=0,column=1)




# **** Radio Buttons ****

# selectedLanguage = StringVar(value="Python language")

# Python = Radiobutton(window,text="Python",variable=selectedLanguage,value="Python language")
# JAVA = Radiobutton(window,text="JAVA",variable=selectedLanguage,value="JAVA language")
# DataStrucutre = Radiobutton(window,text="DataStrucutre",variable=selectedLanguage,value="DataStrucutre language")

# l1 = Label(window,text="Ans : ")

# def show():
#     name = selectedLanguage.get()
#     l1.config(text=f"Result : {name}")
    
# btn = Button(window,text="Show Result",command=show)

# Python.pack()
# JAVA.pack()
# DataStrucutre.pack()
# l1.pack()
# btn.pack()




# **** DropDown [Option Menu] ****

# myList = ["Python","JAVA","C#","MySQL"]

# myvar = StringVar(window)
# myvar.set(myList[0])

# drop_down = OptionMenu(window, myvar, *myList)
# drop_down.pack()

# l1 = Label(window,text="Current Selected")
# l1.pack()

# def btnClick():
#     CurrentSelectedIten = myvar.get()
#     l1.config(text=CurrentSelectedIten)

# btn = Button(window,text="Select",command=btnClick)
# btn.pack()




# **** CheckBox ****

# def toggle_check():
#     if Checkbox_var.get() == 1:
#         # print("CHECKED")
#         frame.config(bg="black")
#         l1.config(fg="white",bg="black",text="Light Mode")
#     else:
#         # print("UNCHECKED")
#         frame.config(bg="white")
#         l1.config(fg="black",bg="white",text="Dark Mode")

# Checkbox_var = IntVar()

# check_btn = Checkbutton(window,text="Change Theme",variable=Checkbox_var,command=toggle_check,font=("calibri 14"))
# check_btn.pack()

# frame = Frame(window,width=1000,height=500,bg="white")
# frame.pack()

# l1 = Label(frame,text="Dark Mode",fg="black",bg="white",width=1000,height=500,font=("calibri 26 bold"))
# l1.pack()




# **** Label Frame ****

# w = window.winfo_screenwidth()
# h = window.winfo_screenheight()
# window.geometry("{}x{}".format(w,h))

# lFrame = LabelFrame(window,text="Personal Details")
# lFrame.pack(padx=10,pady=10)

# name = Label(lFrame,text="Name")
# name.grid(row=0,column=0,padx=5,pady=5)
# nameEntry = Entry(lFrame,width=25)
# nameEntry.grid(row=0,column=1,padx=5,pady=5)

# email = Label(lFrame,text="Email")
# email.grid(row=1,column=0,padx=5,pady=5)
# emailEntry = Entry(lFrame,width=25)
# emailEntry.grid(row=1,column=1,padx=5,pady=5)




# **** Scale [Slider] ****

# def onchange(value):
#     l1.config(text=f"Font size : {value}")
#     l1.config(font=f"calibri {value} bold")

# scale = Scale(window,from_=0,to=100,orient=HORIZONTAL,command=onchange)
# scale.pack()

# l1 = Label(window,text="Font Size : 0",font=("calibri 24 bold"))
# l1.pack()




# **** Spin Box ****

# spinbox = Spinbox(window,from_=0,to=100)
# spinbox.pack(pady=10)

# def get():
#     num = spinbox.get()
#     l1.config(num)

# l1 = Label(window,text="Result : ",font=("Arial 16"))
# l1.pack()

# btn = Button(window,text="get data",command=get)
# btn.pack(pady=20)


#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
 

# Geometry Management

#pack [One by one (stack like stucture)]
# label = Label(window,text="Label")
# label.pack()

#grid [Tabel like (rows & Columns)]
# label = Label(window,text="Label")
# label.grid(row=0,column=1)

#place [Coordinates (x & y)]
# label = Label(window,text="Label")
# label.place(x=20,y=20)


#--------------------------------------------------------------------------------------------------------------


# Frames & Layouts

# **** Paned Window ****

# window.geometry("1800x1700")

# paned_window = PanedWindow(window,orient=HORIZONTAL)
# paned_window.pack(fill=BOTH,expand=True)

# left = Frame(paned_window,bg="pink",width=200,height=200)

# def homeclick():
#     black = Frame(paned_window,bg="black",width=200,height=200)
#     paned_window.forget(right)
#     paned_window.add(black)

# homebtn = Button(left,text="HOME",font=("calibri 18 bold"),command=homeclick)
# homebtn.place(x=55,y=100)

# right = Frame(paned_window,bg="skyblue",width=200,height=200)

# paned_window.add(left)
# paned_window.add(right)




# **** Frames ****

# def onclick():
#     # left side frame
#     frame1 = Frame(main,width=300,height=580,bg="pink")
#     frame1.place(x=0,y=0)

#     # right side frame
#     frame2 = Frame(main,width=600,height=420,bg="skublue")
#     frame2.place(x=370,y=80)

# btn = Button(window,text="Click me",command=onclick)
# btn.pack()

# # main frame
# main = Frame(window,width=1100,height=580,bg="white")
# main.place(x=230,y=200)




# **** Top Level ****

# w = window.winfo_screenwidth()
# h = window.winfo_screenheight()
# window.geometry("{}x{}".format(w,h))

# def open_new_window():
#     new_win = Toplevel(window)
#     new_win.geometry("300x300")

#     l1 = Label(new_win,text="new window",font=("calibri 24 bold"))
#     l1.pack()

# open_window = Button(window,text="Open new Window",command=open_new_window)
# open_window.pack()


#------------------------------------------------------------------------------------------------------------

# Menu 

# **** Menu & Submenu ****

# mainmenu = Menu(window)

# # file menu
# filemenu = Menu(mainmenu)

# filemenu.add_command(label="New File")
# filemenu.add_command(label="Open...")
# mainmenu.add_cascade(label="File",menu=filemenu)

# # edit menu
# editmenu = Menu(mainmenu)

# editmenu.add_command(label="Cut")
# editmenu.add_command(label="Copy")
# editmenu.add_cascade(label="Paste")

# window.config(menu=mainmenu)

# [Note : Submenu are in Notepad App]


#------------------------------------------------------------------------------------------------------------

# Draw and Shapes

# **** Canvas ****

# w = window.winfo_screenwidth()
# h = window.winfo_screenheight()
# window.geometry(f"{w}x{h}")

# canvas = Canvas(window,bg="skyblue",height=400,width=500)
# canvas.place(x=250,y=150)

#[create line in canvas
# canvas.create_line(0,0,300,300,fill="black")]




# **** Rectangle ****

# w = window.winfo_screenwidth()
# h = window.winfo_screenheight()
# window.geometry(f"{w}x{h}")

# canvas = Canvas(window,bg="skyblue",height=400,width=500)
# canvas.place(x=250,y=150)

# canvas.create_rectangle(0,0,300,300,fill="red")

# def btnclick():
#     canvas.create_rectangle(70,80,250,250,fill="yellow")

# btn = Button(canvas,text="Click",font=("Arial 16 bold"),command=btnclick)
# btn.place(x=250,y=20)




# **** Oval ****

# w = window.winfo_screenwidth()
# h = window.winfo_screenheight()
# window.geometry(f"{w}x{h}")

# canvas = Canvas(window,bg="skyblue",height=400,width=500)
# canvas.place(x=250,y=150)

# canvas.create_oval(10,10,200,200,fill="pink")

# def btnclick():
#     canvas.create_oval(70,80,150,150,fill="yellow")

# btn = Button(canvas,text="Click",bg="black",fg="white",font=("Arial 16 bold"),command=btnclick)

# btn.place(x=250,y=20)




# **** Destroy ****

# login = Frame(window,width=500,height=400,bg="lightblue")
# login.place(x=500,y=200)

# def submit():
#     login.destroy()

# submit = Button(window,text="Submit",fg="white",bg="dodgerblue",font=("calibri 15"),padx=20,command=submit)
# submit.place(x=190,y=250)




# **** MessageBox ****

# def btnclick():
#     messagebox.showinfo("SPACE RUNNING OUT","Your disk space have no space.")
#     # messagebox.showerror("SPACE RUNNING OUT","Your disk space have no space.")
#     # messagebox.showwarnig("SPACE RUNNING OUT","Your disk space have no space.")

#     result = messagebox.askquestion("Name","Hello World")

#     if result == "yes":
#         messagebox.showinfo("DONE","You have selected YES")
#     else:
#         messagebox.showerror("ERROR","You have selected NO")

# btn = Button(window,text="Selected",command=btnclick)
# btn.pack()


window.mainloop()
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

# Projects


# **** Student Registration Form ****

# class Student():
#     def __init__(self,fname,lname,email,address,lang,gender,sem,enroll):
#         self.stuFName = fname
#         self.stuLName = lname
#         self.stuEmail = email
#         self.stuAddress = address
#         self.stuLang = lang
#         self.stuGender = gender
#         self.stuSemester = sem
#         self.stuEnroll = enroll
 
# StudentList = []

# win = Tk()

# w = win.winfo_screenwidth()
# h = win.winfo_screenheight()
# win.geometry("{}x{}".format(w,h))
# win.config(bg="white")
# win.title("Registration Form")

# # main frame
# mainFrame = Frame(win,width=w,height=h,bg="white")
# mainFrame.pack()

# title = Label(mainFrame,text="REGISTRATION FORM",font=("Futura 24 bold"),fg="black",bg="white")
# title.place(x=600,y=20)

# #Submit btn
# def submitbtn():
#     stuFName = fnameEntry.get()
#     stuLName = lnameEntry.get()
#     stuEmail = emailEntry.get()
#     stuAddress = addressEntry.get()
#     stuLang = myLang.get()
#     stuGender = selectedGender.get()
#     stuSemester = mySem.get()
#     stuEnroll = SelectEnrollment.get()

#     s1 = Student(stuFName,stuLName,stuEmail,stuAddress,stuLang,stuGender,stuSemester,stuEnroll)
#     StudentList.append(s1)

#     if(stuFName or stuLName or stuEmail or stuAddress == ""):
#         messagebox.showerror("ERROR", "Required field is empty")

#     fnameEntry.delete(0,END)
#     lnameEntry.delete(0,END)
#     emailEntry.delete(0,END)
#     addressEntry.delete(0,END)
#     myLang.delete(0,END)
#     selectedGender.delete(0,END)
#     mySem.delete(0,END)
#     SelectEnrollment.delete(0,END)

# #first name
# fname = Label(mainFrame,text="First Name",font=("Calibri 16"),bg="white")
# fname.place(x=350,y=100)
# fnameEntry = Entry(mainFrame,width=40)
# fnameEntry.place(x=600,y=100)

# #last name
# lname = Label(mainFrame,text="Last Name",font=("Calibri 16"),bg="white")
# lname.place(x=350,y=150)
# lnameEntry = Entry(mainFrame,width=40)
# lnameEntry.place(x=600,y=150)

# #email
# email = Label(mainFrame,text="Email-ID",font=("Calibri 16"),bg="white")
# email.place(x=350,y=200)
# emailEntry = Entry(mainFrame,width=40)
# emailEntry.place(x=600,y=200)

# #address
# address = Label(mainFrame,text="Address",font=("Calibri 16"),bg="white")
# address.place(x=350,y=250)
# addressEntry = Entry(mainFrame,width=40)
# addressEntry.place(x=600,y=250)

# #Language
# Language = Label(mainFrame,text="Language",font=("Calibri 16"),bg="white")
# Language.place(x=350,y=300)

# LangList = ["English","Hindi","Gujarati"]

# myLang = StringVar(mainFrame)
# myLang.set(LangList[0])

# LangDrop_Down = OptionMenu(mainFrame, myLang, *LangList)
# LangDrop_Down.config(bg="white")
# LangDrop_Down.place(x=600,y=300)

# #Gender
# Gender = Label(mainFrame,text="Gender",font=("Calibri 16"),bg="white")
# Gender.place(x=350,y=350)

# selectedGender = StringVar(value="Male")

# Male = Radiobutton(mainFrame,text="Male",variable=selectedGender,value="Male",font=("Calibri 14"),bg="white")
# Male.place(x=600,y=350)
# Female = Radiobutton(mainFrame,text="Female",variable=selectedGender,value="Female",font=("Calibri 14"),bg="white")
# Female.place(x=700,y=350)
# Other = Radiobutton(mainFrame,text="Other",variable=selectedGender,value="Other",font=("Calibri 14"),bg="white")
# Other.place(x=800,y=350)

# #Semester
# Semester = Label(mainFrame,text="Semester",font=("Calibri 16"),bg="white")
# Semester.place(x=350,y=400)

# SemList = ["Sem 1","Sem 3","Sem 5","Sem 7","Sem 9"]

# mySem = StringVar(mainFrame)
# mySem.set(SemList[0])

# SemDrop_Down = OptionMenu(mainFrame, mySem, *SemList)
# SemDrop_Down.config(bg="white")
# SemDrop_Down.place(x=600,y=400)

# #Enrollment
# Enroll = Label(mainFrame,text="Enrolled in Course?",font=("Calibri 16"),bg="white")
# Enroll.place(x=350,y=450)

# SelectEnrollment = StringVar(value="Yes")

# Yes = Radiobutton(mainFrame,text="Yes",variable=SelectEnrollment,value="Yes",font=("Calibri 14"),bg="white")
# Yes.place(x=600,y=450)
# No = Radiobutton(mainFrame,text="No",variable=SelectEnrollment,value="No",font=("Calibri 14"),bg="white")
# No.place(x=700,y=450)

# #Submit
# submit = Button(mainFrame,text="Submit",bg="dodgerblue",fg="white",font=("Calibri 14 bold"),padx=20,command=submitbtn)
# submit.place(x=650,y=500)

# #show details
# def showstu():
#     table = " First Name \t Last Name \t Email \t \t Address \t \t Language \t Gender \t \t Semester \t \t Enrollment"

#     for stu in StudentList:
#         table += "\n{} \t \t{} \t \t{} \t \t{} \t \t{} \t \t{} \t \t{} \t \t{}".format(stu.stuFName,stu.stuLName,stu.stuEmail,stu.stuAddress,stu.stuLang,stu.stuGender,stu.stuSemester,stu.stuEnroll)
#     tableLabel.config(text=table)

# # show button
# showbtn = Button(mainFrame,text="Show Details",command=showstu,bg="white",font=("Calibri 13"))
# showbtn.place(x=650,y=550)

# # Show Detail Table 
# tableLabel = Label(mainFrame,text=" ",font=("Times 16"),bg="white",fg="black")
# tableLabel.place(x=20,y=600)

# win.mainloop()


# -------------------------------------------------------


# **** Login Registration **** 


# class user():
#     def __init__(self,fname,lname,email,password):
#         self.userFname = fname
#         self.userLname = lname
#         self.userEmail = email
#         self.userPass = password

# userList = []

# win = Tk()

# w = win.winfo_screenwidth()
# h = win.winfo_screenheight()
# win.geometry("{}x{}".format(w,h))
# win.config(bg="white")
# win.title("Login")

# #login 
# login = Frame(win,width=500,height=400,bg="lightblue")
# login.place(x=500,y=200)

# title = Label(login,text="LOGIN",fg="black",bg="lightblue",font=("calibri 20 bold"))
# title.place(x=210,y=20)

# id = Label(login,text="Email-Id",fg="black",bg="lightblue",font=("calibri 16"))
# id.place(x=50,y=120)
# idEntry = Entry(login,width=30)
# idEntry.place(x=150,y=120)

# password = Label(login,text="Password",fg="black",bg="lightblue",font=("calibri 16"))
# password.place(x=50,y=180)
# passEntry = Entry(login,width=30)
# passEntry.place(x=150,y=180)

# def stbtn():
#         state = False

#         for i in userList:
#             if (idEntry.get() == i.userEmail) and (passEntry.get() == i.userPass):
#                 state = True

#         if state:
#             login.destroy()
#             messagebox.showinfo("Logged In Successfully","WELCOME USER")
#             #home frame
#             homeFrame = Frame(win,width=1800,height=1000)
#             homeFrame.place(x=0,y=0)

#             homel1 = Label(homeFrame,text="Welcome Home",font=("calibri 24 bold"))
#             homel1.pack()

#         else:
#             messagebox.showerror("ERROR","User Not Found")
#             idEntry.delete(0,END)
#             passEntry.delete(0,END)

# submit = Button(login,text="Submit",fg="white",bg="dodgerblue",font=("calibri 15"),padx=20,command=stbtn)
# submit.place(x=190,y=250)

# acc = Label(login,text="Don't have an account?",fg="white",bg="lightblue",font=("calibri 13 bold"))
# acc.place(x=120,y=300)

# #RegistrationForm
# def signinclick():
#     # login.destroy()
#     register = Frame(win,width=600,height=500,bg="pink")
#     register.place(x=420,y=150)

#     title = Label(register,text="Sign In Page",fg="black",bg="pink",font=("calibri 20 bold"))
#     title.place(x=210,y=20)

#     #first name
#     fname = Label(register,text="First Name",font=("Calibri 14"),bg="pink")
#     fname.place(x=80,y=120)
#     fnameEntry = Entry(register,width=40)
#     fnameEntry.place(x=180,y=120)

#     #last name
#     lname = Label(register,text="Last Name",font=("Calibri 14"),bg="pink")
#     lname.place(x=80,y=180)
#     lnameEntry = Entry(register,width=40)
#     lnameEntry.place(x=180,y=180)

#     #email
#     email = Label(register,text="Email-ID",font=("Calibri 14"),bg="pink")
#     email.place(x=80,y=250)
#     emailEntry = Entry(register,width=40)
#     emailEntry.place(x=180,y=250)

#     #password
#     password = Label(register,text="Password",font=("Calibri 14"),bg="pink")
#     password.place(x=80,y=310)
#     passwordEntry = Entry(register,width=40)
#     passwordEntry.place(x=180,y=310)


#     def submit():
#         fname = fnameEntry.get()
#         lname = lnameEntry.get()
#         email = emailEntry.get()
#         password = passwordEntry.get()

#         u1 = user(fname,lname,email,password)
#         userList.append(u1)

#         fnameEntry.delete(0,END)
#         lnameEntry.delete(0,END)
#         emailEntry.delete(0,END)
#         passwordEntry.delete(0,END)

#         # register.destroy()

#         messagebox.showinfo("SUCCESS","Registered Successfully!!!")
#         register.destroy()

#     sign = Button(register,text="Sign In",fg="white",bg="dodgerblue",font=("calibri 15"),padx=20,command=submit)
#     sign.place(x=250,y=360)

#     acc = Label(register,text="Already have an account?",fg="white",bg="pink",font=("calibri 13 bold"))
#     acc.place(x=180,y=410)

#     def loginpage():
#         register.destroy()

#     loginbtn = Button(register,text="Login In",fg="dodgerblue",bg="pink",font=("calibri 14 bold"),bd=0,command=loginpage)
#     loginbtn.place(x=370,y=405)

# signin = Button(login,text="Sign In",fg="dodgerblue",bg="lightblue",font=("calibri 14 bold"),bd=0,command=signinclick)
# signin.place(x=300,y=295)

# win.mainloop()


#-------------------------------------------------------------


# **** Chess Board ****

# win = Tk()
# w = win.winfo_screenwidth()
# h = win.winfo_screenheight()
# win.geometry(f"{w}x{h}")

# canvas = Canvas(win,width=w,height=h)
# canvas.place(x=380,y=10)

# x1 = 0
# y1 = 0
# x2 = 0
# y2 = 0
# color = False

# def chess_board():
#     global x1,y1,x2,y2
#     global color
#     if(y2<800):
#         if(color):
#             mycolor = "white"

#         else:  
#             mycolor = "black"

#         canvas.create_rectangle(x1,y1,x2+100,y2+100,fill=mycolor) 
#         x2+=100
#         x1+=100
#         color = not(color)

#         if x1==800:
#             x1=0
#             y1=y1+100
#             x2=0
#             y2=y2+100
#             color = not(color)

# btn = Button(win,text="Create Chess Board",command=chess_board)
# btn.place(x=30,y=50)

# win.mainloop()


#-----------------------------------------------------------


# **** Student Management System [CRUD operations] ****


# class Student():
#     def __init__(self,name,email,sem):
#         self.stuName = name
#         self.stuEmail = email
#         self.stuSemester = sem
 
# StudentList = []

# win = Tk()
# win.title("Student Management")

# # Window
# h = win.winfo_screenheight()
# w = win.winfo_screenwidth()
# win.geometry("1536x864")

# # heading
# heading = Label(win,text="Student Management System",font=("Georgia 24 bold"))
# heading.pack()

# # Add btn function
# def addbtn():
#     stuName = nameEntry.get()
#     stuEmail = emailEntry.get()
#     stuSemester = semesterEntry.get()

#     s1 = Student(stuName,stuEmail,stuSemester)
#     StudentList.append(s1)

#     nameEntry.delete(0,END)
#     emailEntry.delete(0,END)
#     semesterEntry.delete(0,END)

# # Student input 
# name = Label(win,text="Student Name",font=("Georgia 16 bold"))
# name.place(x=10,y=110)

# nameEntry = Entry(win,width=25)
# nameEntry.place(x=200,y=110)

# rollNo = Label(win,text="Student RollNo",font=("Georgia 16 bold"))
# rollNo.place(x=10,y=150)

# rollNoEntry = Entry(win,width=25)
# rollNoEntry.place(x=200,y=150)

# email = Label(win,text="Student Email-ID",font=("Georgia 16 bold"))
# email.place(x=450,y=110)

# emailEntry = Entry(win,width=25)
# emailEntry.place(x=670,y=110)

# semester = Label(win,text="Student Semester",font=("Georgia 16 bold"))
# semester.place(x=910,y=110)

# semesterEntry = Entry(win,width=25)
# semesterEntry.place(x=1150,y=110)

# # Add button
# addbtn = Button(win,text="Add Student",command=addbtn,bg="white",font=("Georgia 12"))
# addbtn.place(x=470,y=200)


# # table print function
# def showstu():
#     table = " Roll No. \t \t  Student Name \t \t Student Email \t \t Student Semester"

#     rollNo = 1

#     for stu in StudentList:
#         table += "\n{} \t \t {} \t \t {} \t \t {}".format(rollNo,stu.stuName,stu.stuEmail,stu.stuSemester)
#         rollNo += 1
#     tableLabel.config(text=table)

# # show button
# showbtn = Button(win,text="Show Details",command=showstu,bg="white",font=("Georgia 12"))
# showbtn.place(x=675,y=280)


# # Delete Student
# def deletebtn():
#     roll = int(rollNoEntry.get())
#     index = roll - 1
#     StudentList.pop(index)
#     showstu()
#     rollNoEntry.delete(0,END)

# deletebtn = Button(win,text="Delete Student",command=deletebtn,bg="white",font=("Georgia 12"))
# deletebtn.place(x=670,y=200)

# updateRollNo = 0

# # Update Student
# def updatebtn():
#     stuName = nameEntry.get()
#     stuEmail = emailEntry.get()
#     stuSemester = semesterEntry.get()

#     StudentList[updateRollNo].stuName = stuName
#     StudentList[updateRollNo].stuEmail = stuEmail
#     StudentList[updateRollNo].stuSemester = stuSemester

#     nameEntry.delete(0,END)
#     emailEntry.delete(0,END)
#     semesterEntry.delete(0,END)

#     showbtn()

# updatebtn = Button(win,text="Update Student",command=updatebtn,bg="white",font=("Georgia 12"))
# updatebtn.place(x=900,y=200)

# # Get Details of Student
# def getbtn():
#     rollno = int(rollNoEntry.get())

#     global updateRollNo
#     updateRollNo = rollno - 1


#     if(rollno - 1 < len(StudentList)):
#         nameEntry.delete(0,END)
#         emailEntry.delete(0,END)
#         semesterEntry.delete(0,END)

#         nameEntry.insert(0,StudentList[rollno - 1].stuName)
#         emailEntry.insert(0,StudentList[rollno - 1].stuEmail)
#         semesterEntry.insert(0,StudentList[rollno - 1].stuSemester)
#     else:
#         messagebox.showerror("ERROR","Invalid Roll No.")

# getbtn = Button(win,text="Get Student",command=getbtn,bg="white",font=("Georgia 12"))
# getbtn.place(x=270,y=200)

# # Show Detail Table 
# tableLabel = Label(win,text=" ",font=("Times 16"))
# tableLabel.place(x=200,y=350)

# win.mainloop()


#--------------------------------------------------------------------------


# **** Paint App ****


# win = Tk()
# w = win.winfo_screenwidth()
# h = win.winfo_screenheight()
# win.geometry("{}x{}".format(w,h))

# # main window
# main = Frame(win,height=600,width=800,highlightbackground="black",highlightthickness=2)
# main.pack()

# # color frame
# color = Frame(win,height=100,width=370)
# color.place(x=580,y=630)


# black = Button(color,height=1,width=3,bg="black",command=lambda : main.config(bg="black"))
# black.place(x=10,y=10)

# grey = Button(color,height=1,width=3,bg="grey",command=lambda : main.config(bg="grey"))
# grey.place(x=50,y=10)

# brown = Button(color,height=1,width=3,bg="brown",command=lambda : main.config(bg="brown"))
# brown.place(x=90,y=10)

# red = Button(color,height=1,width=3,bg="red",command=lambda : main.config(bg="red"))
# red.place(x=130,y=10)

# orange = Button(color,height=1,width=3,bg="orange",command=lambda : main.config(bg="orange"))
# orange.place(x=170,y=10)

# yellow = Button(color,height=1,width=3,bg="yellow",command=lambda : main.config(bg="yellow"))
# yellow.place(x=210,y=10)

# lightblue = Button(color,height=1,width=3,bg="lightblue",command=lambda : main.config(bg="lightblue"))
# lightblue.place(x=250,y=10)

# darkblue = Button(color,height=1,width=3,bg="darkblue",command=lambda : main.config(bg="darkblue"))
# darkblue.place(x=290,y=10)

# purple = Button(color,height=1,width=3,bg="purple",command=lambda : main.config(bg="purple"))
# purple.place(x=330,y=10)

# white = Button(color,height=1,width=3,bg="white",command=lambda : main.config(bg="white"))
# white.place(x=10,y=60)

# lightgrey = Button(color,height=1,width=3,bg="lightgrey",command=lambda : main.config(bg="lightgrey"))
# lightgrey.place(x=50,y=60)

# darkred = Button(color,height=1,width=3,bg="darkred",command=lambda : main.config(bg="darkred"))
# darkred.place(x=90,y=60)

# pink = Button(color,height=1,width=3,bg="pink",command=lambda : main.config(bg="pink"))
# pink.place(x=130,y=60)

# gold = Button(color,height=1,width=3,bg="gold",command=lambda : main.config(bg="gold"))
# gold.place(x=170,y=60)

# lightyellow = Button(color,height=1,width=3,bg="lightyellow",command=lambda : main.config(bg="lightyellow"))
# lightyellow.place(x=210,y=60)

# skyblue = Button(color,height=1,width=3,bg="skyblue",command=lambda : main.config(bg="skyblue"))
# skyblue.place(x=250,y=60)

# dodgerblue = Button(color,height=1,width=3,bg="dodgerblue",command=lambda : main.config(bg="dodgerblue"))
# dodgerblue.place(x=290,y=60)

# lavender = Button(color,height=1,width=3,bg="lavender",command=lambda : main.config(bg="lavender"))
# lavender.place(x=330,y=60)

# win.mainloop()


#--------------------------------------------------------------------


# **** Encrypt Decrypt  ****


# window= Tk()
# window.geometry("300x200")

# Label1 = Label(window,text="Enter your name : ")
# Label1.grid(row=0,column=0)

# Input = Entry(window,width=18)
# Input.grid(row=0,column=1)

# def encrypt():
#     Text = Input.get()
#     en = ""
#     ans = ""
#     for j in Text[ : :-1]:
#         ans += j
#     for i in ans:
#         a = ord(i)+1
#         en += chr(a)

#     Result.config(text=en)

# def decrypt():
#     Text = Input.get()
#     en = ""
#     ans = ""
#     for j in Text[ : :-1]:
#         ans += j
#     for i in ans:
#         a = ord(i)-1
#         en += chr(a)

#     Result.config(text=en)    

# encry = Button(window,text="Encryption",command=encrypt)
# encry.grid(row=1,column=0)

# decry = Button(window,text="Decryption",command=decrypt)
# decry.grid(row=1,column=1)

# Result = Label(window)
# Result.grid(row=2,column=0)

# window.mainloop()


#----------------------------------------------------------------------------


# **** Calculator App ****


# window = Tk()
# window.geometry("400x300")
# window.title("Calc")
 
# number1 = Label(window, text="Number 1:")
# number1.grid(row=0, column=0)

# num1_entry = Entry(window)
# num1_entry.grid(row=0, column=1)

# number2 = Label(window, text="Number 2:")
# number2.grid(row=1, column=0)

# num2_entry = Entry(window)
# num2_entry.grid(row=1, column=1)

# Ans = Label(window, text="Answer :")
# Ans.grid(row=4, column=0)

# # Addition
# def add():
#     num1 = float(num1_entry.get())
#     num2 = float(num2_entry.get())
#     result = num1 + num2
#     Calculation.config(text=result)
 
# Addition = Button(window, text="Addition", command=add)
# Addition.grid(row=2, column=0)

# Calculation = Label(window)
# Calculation.grid(row=4, column=1)

# # Subtraction
# def sub():
#     num1 = float(num1_entry.get())
#     num2 = float(num2_entry.get())
#     result = num1 - num2
#     Calculation.config(text=result)
 
# Subtraction = Button(window, text="Subtraction", command=sub)
# Subtraction.grid(row=2, column=1)

# Calculation = Label(window)
# Calculation.grid(row=4, column=1)

# #Multiplication
# def multi():
#     num1 = float(num1_entry.get())
#     num2 = float(num2_entry.get())
#     result = num1 * num2
#     Calculation.config(text=result)
 
# Multiplication = Button(window, text="Multiplication", command=multi)
# Multiplication.grid(row=3, column=0)

# Calculation = Label(window)
# Calculation.grid(row=4, column=1)

# #Divition
# def div():
#     num1 = float(num1_entry.get())
#     num2 = float(num2_entry.get())
#     result = num1 / num2
#     Calculation.config(text=result)
 
# Divition = Button(window, text="Divition", command=div)
# Divition.grid(row=3, column=1)

# Calculation = Label(window)
# Calculation.grid(row=4, column=1)
 
# window.mainloop()


#----------------------------------------------------------------------------


# **** Password Validations ****


# window = Tk()
# window.geometry("500x500")

# L1 = Label(window,text="Enter your Password : ")
# L1.grid(row=0,column=0)

# PassInput = Entry(window,width=20)
# PassInput.grid(row=0,column=1)

# L2 = Label(window,text="")
# L2.grid(row=2,column=0)

# def btnclick():
#     if(len(PassInput.get()) >= 8):
#         L2.config(text="Password set successfully!",fg="green",font="arial 10 bold")
#     else:
#         L2.config(text="Error!!Password must be 8 characters long..",fg="red",font="arial 10 bold")

# btn = Button(window,text="Submit",command=btnclick)
# btn.grid(row=1,column=0)

# window.mainloop()


#-----------------------------------------------------------------------------


# **** Ice Cream Management System ****


# win = Tk()

# w = win.winfo_screenwidth()
# h = win.winfo_screenheight()

# win.geometry("{}x{}".format(w,h))
# win.config(bg="lavender")
# win.title("Havmor ice cream")

# head = Label(win,text="HAVMOR",font=("Arial 28 bold"),fg="white",bg="lavender")
# head.place(x=700,y=20)


# # button frame
# btnframe = Frame(win,width=900,height=40,bg="lavender")
# btnframe.place(x=350,y=90)

# def pro_onclick():

#     # left side frame
#     frame1 = Frame(main,width=300,height=580,bg="pink")
#     frame1.place(x=0,y=0)

#     product.config(bg="black",fg="white")

#     Pro_head = Label(frame1,text="PRODUCT",font=("Georgia 20 bold"),bg="pink")
#     Pro_head.place(x=85,y=10)

#     def addbtn():

#         add_btn.config(bg="black",fg="white")

#         # right side frame
#         frame2 = Frame(main,width=600,height=420,bg="pink")
#         frame2.place(x=370,y=80)

#         name = Label(frame2,text="Product Name :",font=("Arial 14"),bg="pink")
#         name.place(x=80,y=50)

#         name_input = Entry(frame2,width=30)
#         name_input.place(x=220,y=50)

#         cat = Label(frame2,text="Category :",font=("Arial 14"),bg="pink")
#         cat.place(x=80,y=100)

#         cat_input = Entry(frame2,width=30)
#         cat_input.place(x=220,y=100)

#         Quantity = Label(frame2,text="Quantity :",font=("Arial 14"),bg="pink")
#         Quantity.place(x=80,y=150)

#         Quantity_input = Entry(frame2,width=30)
#         Quantity_input.place(x=220,y=150)

#         Price = Label(frame2,text="Product Price :",font=("Arial 14"),bg="pink")
#         Price.place(x=80,y=200)

#         Price_input = Entry(frame2,width=30)
#         Price_input.place(x=220,y=200)

#         Description = Label(frame2,text="Description :",font=("Arial 14"),bg="pink")
#         Description.place(x=80,y=250)

#         Description_input = Entry(frame2,width=30)
#         Description_input.place(x=220,y=250)


#         submit_btn = Button(frame2,text="Submit",bg="white",fg="black",width=10,font=("Times 14 bold"),bd=2)
#         submit_btn.place(x=150,y=310)

#         reset_btn = Button(frame2,text="Reset",bg="white",fg="black",width=10,font=("Times 14 bold"),bd=2)
#         reset_btn.place(x=330,y=310)


#     add_btn = Button(frame1,text="ADD",bg="white",fg="black",width=12,font=("Times 18 bold"),bd=2,command=addbtn)
#     add_btn.place(x=70,y=70)

#     View_btn = Button(frame1,text="VIEW",bg="white",fg="black",width=12,font=("Times 18 bold"),bd=2)
#     View_btn.place(x=70,y=170)

#     Update_btn = Button(frame1,text="UPDATE",bg="white",fg="black",width=12,font=("Times 18 bold"),bd=2)
#     Update_btn.place(x=70,y=270)

#     delete_btn = Button(frame1,text="DELETE",bg="white",fg="black",width=12,font=("Times 18 bold"),bd=2)
#     delete_btn.place(x=70,y=370)


# # main buttons (head)
# product = Button(btnframe,text="Product",bg="white",fg="black",font=("Arial 10 bold"),width=12,command=pro_onclick)
# product.place(x=20,y=0)

# cust = Button(btnframe,text="Customer",bg="white",fg="black",font=("Arial 10 bold"),width=12)
# cust.place(x=200,y=0)

# bill = Button(btnframe,text="Bill Records",bg="white",fg="black",font=("Arial 10 bold"),width=12)
# bill.place(x=380,y=0)

# billing = Button(btnframe,text="Billing",bg="white",fg="black",font=("Arial 10 bold"),width=12)
# billing.place(x=560,y=0)

# close = Button(btnframe,text="Close",bg="white",fg="black",font=("Arial 10 bold"),width=12)
# close.place(x=740,y=0)

# # main frame
# main = Frame(win,width=1100,height=580,bg="white")
# main.place(x=230,y=200)

# win.mainloop()


#------------------------------------------------------------------


# **** Notepad App ****

# win = Tk()
# w = win.winfo_screenwidth()
# h = win.winfo_screenheight()
# win.geometry(f"{w}x{h}")
# win.title("Untited - Notepad")

# mainmenu = Menu(win)


# # file menu
# filemenu = Menu(mainmenu)

# filemenu.add_command(label="New File            Ctrl + N")
# filemenu.add_command(label="Open..                Ctrl + O")
# filemenu.add_command(label="Save                   Ctrl + S")
# filemenu.add_command(label="Save as")
# filemenu.add_command(label="Page Setup...")
# filemenu.add_command(label="Print                   Ctrl + P")
# filemenu.add_command(label="Exit",command=win.destroy)

# mainmenu.add_cascade(label="File",menu=filemenu)


# # edit menu
# editmenu = Menu(mainmenu)

# editmenu.add_command(label="Undo            Ctrl + Z")
# editmenu.add_command(label="Cut                Ctrl + X")
# editmenu.add_command(label="Copy             Ctrl + C")
# editmenu.add_command(label="Paste             Ctrl + V")
# editmenu.add_command(label="Delete           Del")
# editmenu.add_command(label="Find               Ctrl + F")
# editmenu.add_command(label="Find Next      F3")
# editmenu.add_command(label="Replace...      Ctrl + H")
# editmenu.add_command(label="Go to...          Ctrl + G")
# editmenu.add_command(label="Select all       Ctrl + A")
# editmenu.add_command(label="Time/Date     F5")

# mainmenu.add_cascade(label="Edit",menu=editmenu)


# # format menu
# formatmenu = Menu(mainmenu)

# formatmenu.add_command(label="Word Wrap")
# formatmenu.add_command(label="Font...")

# mainmenu.add_cascade(label="Format",menu=formatmenu)


# # view menu
# viewmenu = Menu(mainmenu)
# #zoom
# zoommenu = Menu(viewmenu)
# viewmenu.add_cascade(label="Zoom",menu=zoommenu)
# zoommenu.add_command(label="Zoom In")
# zoommenu.add_command(label="Zoom Out")

# viewmenu.add_command(label="Status Bar")
# mainmenu.add_cascade(label="View",menu=viewmenu)


# # help menu
# helpmenu = Menu(mainmenu)
# helpmenu.add_command(label="View Help")
# helpmenu.add_command(label="Send Feedback")
# helpmenu.add_command(label="About Notepad")

# mainmenu.add_cascade(label="Help",menu=helpmenu)

# win.config(menu=mainmenu)

# win.mainloop()

#------------------------------------------------------------------------

# **** Notepad(2) App ****

# win = Tk()
# w = win.winfo_screenwidth()
# h = win.winfo_screenheight()
# win.geometry(f"{w}x{h}")
# win.title("Untited - Notepad")

# mainmenu = Menu(win)

# # file menu
# filemenu = Menu(mainmenu)

# filemenu.add_command(label="New File")
# filemenu.add_command(label="Open...")
# # language
# language = Menu(filemenu)
# filemenu.add_cascade(label="Language",menu=language)
# language.add_command(label="Hindi")
# language.add_command(label="English")
# language.add_command(label="Gujarati")

# filemenu.add_command(label="Save as")
# mainmenu.add_cascade(label="File",menu=filemenu)


# # edit menu
# editmenu = Menu(mainmenu)

# editmenu.add_command(label="Cut")
# editmenu.add_command(label="Copy")
# #paste
# paste = Menu(editmenu)
# paste.add_command(label="Paste formatting")
# paste.add_command(label="Paste normal")
# editmenu.add_cascade(label="Paste",menu=paste)
# #select
# select = Menu(editmenu)
# editmenu.add_cascade(label="Select",menu=select)
# #select all
# selectall = Menu(select)
# selectall.add_command(label="new select")
# selectall.add_command(label="clipboard")
# selectall.add_command(label="file")
# select.add_cascade(label="Select all",menu=selectall)

# mainmenu.add_cascade(label="Edit",menu=editmenu)


# #exit menu
# mainmenu.add_command(label="Exit",command=win.destroy)
# # exitmenu = Menu(mainmenu)
# # mainmenu.add_cascade(label="Exit",menu=exitmenu)

# win.config(menu=mainmenu)

# win.mainloop()

#------------------------------------------------------------



# **** Progress Bar ****

# win = Tk()
# win.title("Progress Bar")

# determinate_progress = ttk.Progressbar(win,mode="determinate",length=300)
# determinate_progress.pack(pady=10)
# determinate_progress["value"] = 100

# indeterminate_progress = ttk.Progressbar(win,mode="indeterminate",length=300)
# indeterminate_progress.pack(pady=10)
# indeterminate_progress.start()

# def click():
#     indeterminate_progress.stop()

# btn = Button(win,text="click",command=click)
# btn.pack()

# win.mainloop()


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

# Some Other Practicles



# **** Count Numbers ****

# window = Tk()

# window.geometry("400x300")

# l1 = Label(window,text="Count")
# l1.grid(column=1,row=0)

# l2 = Label(window,text=0) 
# l2.grid(column=2,row=0)

# num = 0

# def btnclicked():
#     global num
#     num += 1
#     l2.config(text=num)

# btn = Button(window,text="Click here",command=btnclicked)
# btn.grid(column=1,row=1)

# window.mainloop()


#------------------------------------------------------------


# **** Font styling with Style widget ****

# window =Tk()
# window.geometry("500x600")

# # style = Style()

# # style.configure('W.TButton',font=('calibri',10,'bold','underline'),foreground='red')

# b1 = Button(window,text="hii",bg="lightblue",fg="red",font="Arial 34 bold",style="W.TButton")
# b1.grid(row=0,column=3)

# b2 = Button(window,text="hii",bg="black",fg="red",font="Arial 34 bold")
# b2.grid(row=1,column=2)

# window.mainloop()


#-------------------------------------------------------------


# **** Properties (NE,NW,SE,SW) ****

# window = Tk()

# window.geometry("400x600")

# Label1 = Label(window,text="Hello World",font=("Georgia 12 bold"),bg="lavender",fg="black",borderwidth=5,relief="raised",padx=20,pady=20)
# Label1.pack(anchor="nw")

# Label1 = Label(window,text="Hello World",font=("Georgia 12 bold"),bg="red",fg="white",borderwidth=5,relief="raised",padx=20,pady=20)
# Label1.pack(anchor="ne")

# Label1 = Label(window,text="Hello World",font=("Georgia 12 bold"),bg="blue",fg="white",borderwidth=5,relief="raised",padx=40,pady=30)
# Label1.pack(anchor="sw",side=BOTTOM)

# Label1 = Label(window,text="Hello World",font=("Georgia 12 bold"),bg="black",fg="white",borderwidth=5,relief="raised",padx=20,pady=50)
# Label1.pack(anchor="se",side=BOTTOM)

# Label1 = Label(window,text="Hello World",font=("Georgia 12 bold"),bg="lightblue",fg="white",borderwidth=5,relief="raised",padx=20,pady=20)
# Label1.pack(anchor="nw",side=RIGHT,fill=Y)

# Label1 = Label(window,text="Hello World",font=("Georgia 12 bold"),bg="azure",fg="black",borderwidth=5,relief="raised",padx=20,pady=20)
# Label1.pack(anchor="ne",fill=X)

# window.mainloop()


#----------------------------------------------------------------------


# **** Table ****

# win = Tk()

# L1 = Label(win,text="Enter a num")
# L1.place(x=10,y=10)

# E1 = Entry(win)
# E1.place(x=100,y=10)

# anslabel = Label(win,text="ANS")
# anslabel.place(x=10,y=120)


# def btnclick():
#     num = int(E1.get())
#     text = ""
#     for i in range(1,11):
#         text += "{} x {} = {} \n".format(num,i,num*i)
    
#     anslabel.config(text=text)  

# B1 = Button(win,text="Click",command=btnclick)
# B1.place(x=100,y=70)

# win.mainloop()