from tkinter import*

class User:
      def __init__(self,fname,lname,email,address):
            self.FName = fname
            self.LName = lname
            self.email = email
            self.address = address
            # self.language = language
            # self.gender = gender
            # self.sem = sem
            # self.course = course

Userlist = []           
        
win = Tk()
win.title("RAGSTRETION FORM")
win.geometry("1500x800")

heading = Label(win,text="RAGSTRETION FORM",font="Arial 24 bold")
heading.place(x=500,y=10)

fname = Label(win,text="First Name :",font="Arial 16 bold")
fname.place(x=10,y=50)
fentry = Entry(win,width=30)
fentry.place(x=155,y=60)

lname = Label(win,text="Last Name :",font="Arial 16 bold")
lname.place(x=10,y=100)
lentry = Entry(win,width=30)
lentry.place(x=155,y=110)

email = Label(win,text="Email : ",font="arial 16 bold")
email.place(x=10,y=150)
eentry = Entry(win,width=40)
eentry.place(x=155,y=160)

address = Label(win,text="Address : ",font="arial 16 bold")
address.place(x=10,y=200)
aentry = Entry(win,width=100)
aentry.place(x=155,y=210)


      # drop down btn
lan = Label(win,text="Your Language : ",font="arial 16 bold")
lan.place(x=10,y=260)
mylist = ["Hindi","English","Gujarati"]

myvar = StringVar(win)
myvar.set(mylist[0])

drop_down = OptionMenu(win,myvar,*mylist)
drop_down.place(x=190,y=260)

l1 = Label(win,text="Current Selected Language : ",font="arial 10 bold")
l1.place(x=150,y=290)

      # radio btn
gender = Label(win,text="Gender : ",font="arial 16 bold")
gender.place(x=10,y=310)
selected_gen = StringVar()

Male = Radiobutton(win,text="MALE",variable=selected_gen,value="MALE")
Female = Radiobutton(win,text="FEMALE",variable=selected_gen,value="FEMALE")
Other = Radiobutton(win,text="OTHER",variable=selected_gen,value="OTHER")

Male.place(x=110,y=320)
Female.place(x=110,y=340)
Other.place(x=110,y=360)

sem = Label(win,text="Your sem:",font="arial 16 bold")
sem.place(x=10,y=400)

mylist1 = ["SEM1","SEM2","SEM3","SEM4","SEM5","SEM6","SEM7"]

myvar1 = StringVar(win)
myvar1.set(mylist1[0])

drop_down = OptionMenu(win,myvar1,*mylist1)
drop_down.place(x=130,y=400)

l1 = Label(win,text="Current Selected Sem : ",font="arial 10 bold")
l1.place(x=150,y=430)

course = Label(win,text="Enrolment Course : ",font="arial 16 bold")
course.place(x=10,y=450)
selected_course = StringVar()

yes = Radiobutton(win,text="YES",variable=selected_course,value="YES")
no = Radiobutton(win,text="No",variable=selected_course,value="NO")

yes.place(x=220,y=450)
no.place(x=220,y=470)

tableLabel = Label(win,font="Arial 24 bold")
tableLabel.place(x=50,y=600)

def btnclick():
    fname = fentry.get()
    lname = lentry.get()
    ename = eentry.get()
    aname = aentry.get()

    u1 = User(fname,lname,ename,aname)
    Userlist.append(u1)

    fentry.delete(0,END)
    lentry.delete(0,END)
    eentry.delete(0,END)
    aentry.delete(0,END)
    
btn = Button(win,text="SUBMIT",font="arial 16 bold",command=btnclick)
btn.place(x=50,y=500)

def showuser():
      tabel = "First Name \t Last Name \t Email \t Address"

      for user in Userlist:
            tabel +="\n{} \t {} \t {} \t {}".format(user.FName,user.LName,user.email,user.address)

      tableLabel.config(text=tabel)
      
showbtn = Button(win,text="Show",command=showuser,font="arrial 16 bold")
showbtn.place(x=170,y=500)

win.mainloop()