from tkinter import*
window = Tk()

w = window.winfo_screenmmwidth()
h = window.winfo_screenheight()

frame1 = Frame(window,height=900,width=1550,bg="pink")
frame1.place(x=0,y=0)

l1 = Label(frame1,text="HAVMOR",bg="pink",fg="white",font="arial 20 bold")
l1.place(x=720,y=20)

def btnclicked():
    frame2 = Frame(window,height=500,width=300,bg="white")
    frame2.place(x=250,y=90)

    l2 = Label(frame2,text="PRODUCT",bg="white",fg="black",font="arial 20")
    l2.place(x=90,y=0)

    def add():
        frame3 = Frame(window,height=500,width=800,bg="bisque")
        frame3.place(x=560,y=90)

        frame4 = Frame(frame3,height=400,width=500,bg="black")
        frame4.place(x=150,y=50)

        l3 = Label(frame4,fg="white",bg="black",text="Product Name :",width=15)
        l3.place(x=113,y=70)

        entry1 = Entry(frame4)
        entry1.place(x=250,y=70)

        l4 = Label(frame4,fg="white",bg="black",text="Categroy :",width=10)
        l4.place(x=115,y=100)

        entry2 = Entry(frame4)
        entry2.place(x=250,y=100)

        l5 = Label(frame4,fg="white",bg="black",text="Quantity :",width=10)
        l5.place(x=115,y=130)

        entry3 = Entry(frame4)
        entry3.place(x=250,y=130)

        l6 = Label(frame4,fg="white",bg="black",text="Price :",width=10)
        l6.place(x=106,y=160)

        entry4 = Entry(frame4)
        entry4.place(x=250,y=160)

        l7 = Label(frame4,fg="white",bg="black",text="Description :",width=10)
        l7.place(x=123,y=190)

        entry5 = Entry(frame4)
        entry5.place(x=250,y=190)

        btn9 = Button(frame4,text="SUBMIT",bg="lightgray",width=10,font="arial 10 bold")
        btn9.place(x=170,y=220)

        btn10 = Button(frame4,text="RESET",bg="lightgray",width=9,font="arial 10 bold")
        btn10.place(x=270,y=220)

    btn6 = Button(frame2,text="ADD",bg="lightgray",width=20,font="arial 10 bold",command=add)
    btn6.place(x=70,y=50)

    btn7 = Button(frame2,text="VIEW",bg="lightgray",width=20,font="arial 10 bold")
    btn7.place(x=70,y=100)

    btn8 = Button(frame2,text="UPDATE",bg="lightgray",width=20,font="arial 10 bold")
    btn8.place(x=70,y=150)

    btn9 = Button(frame2,text="DELETE",bg="lightgray",width=20,font="arial 10 bold")
    btn9.place(x=70,y=200)
    

btn1 = Button(frame1,text="Product",bg="lightgray",width=10,command=btnclicked)
btn1.place(x=500,y=60)

btn2 = Button(frame1,text="Customer",bg="lightgray",width=10)
btn2.place(x=600,y=60)

btn3 = Button(frame1,text="Bill Record",bg="lightgray",width=10)
btn3.place(x=700,y=60)

btn4 = Button(frame1,text="Billing",bg="lightgray",width=10)
btn4.place(x=800,y=60)

btn5 = Button(frame1,text="Close",bg="lightgray",width=10)
btn5.place(x=900,y=60)

window.mainloop()