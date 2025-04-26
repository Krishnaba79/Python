from tkinter import *

class Product:
    def __init__(self,product,category,quantity,price,descri):
        self.Product = product
        self.Category = category
        self.Quantity = quantity
        self.Price = price
        self.Description = descri
        
    
productList = []

win =Tk()

w= win.winfo_screenwidth()
h= win.winfo_screenheight()

print(w,h)

win.geometry("{}x{}".format(w,h))

mainframe = Frame(win,bg="pink",width=w,height=h,)
mainframe.place(x=0,y=0)

l1 = Label(win,text="Vinod Namkeen & Sweets",bg="pink",fg="black",font="Arial 26 bold")
l1.place(x=550,y=20)

def btnpro():
    frame1 = Frame(win,height=500,width=300,bg="beige",borderwidth=1)
    frame1.place(x=30,y=200)

    product1 = Label(win,text="PRODUCT",fg="black",bg="beige",width=13,height=0,font="Arial 16 bold")
    product1.place(x=105,y=230)

    def btnadd():
        frame1 = Frame(win,height=500,width=1000,bg="bisque")
        frame1.place(x=330,y=200)

        frameadd = Frame(win,height=400,width=500,bg="lightblue")
        frameadd.place(x=590,y=240)

        productname = Label(win,text="Product Name:",fg="black",bg="lightblue",font="8")
        productname.place(x=630,y=260)
        nameinput = Entry(win,width=30)
        nameinput.place(x=850,y=265) 

        category = Label(win,text="Category:",fg="black",bg="lightblue",font="8")
        category.place(x=630,y=310)
        catname = Entry(win,width=30)
        catname.place(x=850,y=315)

        quantity = Label(win,text="Quantity:",fg="black",bg="lightblue",font="10")
        quantity.place(x=630,y=360)
        qname = Entry(win,width=30)
        qname.place(x=850,y=365)

        price = Label(win,text="Price:",fg="black",bg="lightblue",font="10")
        price.place(x=630,y=410)
        pricename = Entry(win,width=30)
        pricename.place(x=850,y=415)

        des = Label(win,text="Description:",fg="black",bg="lightblue",font="10")
        des.place(x=630,y=460)
        desname = Entry(win,width=30)
        desname.place(x=850,y=465) 

        def click():
            product = nameinput.get()
            category = catname.get()
            quantity = qname.get()
            price = pricename.get()
            descri = desname.get()

            p1 = Product(product,category,quantity,price,descri)
            productList.append(p1)

            nameinput.delete(0,END)
            catname.delete(0,END)
            qname.delete(0,END)
            pricename.delete(0,END)
            desname.delete(0,END)

        submit = Button(win,text="Submit",width=10,font="Arial 10 bold",command=click)
        submit.place(x=750,y=550)

        reset = Button(win,text="Reset",width=10,font="Arial 10 bold",command=click)
        reset.place(x=850,y=550)


    add = Button(win,text="ADD",width=13,height=0,font="Arial 12 bold",command=btnadd)
    add.place(x=120,y=300)

    view = Button(win,text="VIEW",width=13,height=0,font="Arial 12 bold")
    view.place(x=120,y=370)

    update = Button(win,text="UPDATE",width=13,height=0,font="Arial 12 bold")
    update.place(x=120,y=440)

    delete = Button(win,text="DELETE",width=13,height=0,font="Arial 12 bold")
    delete.place(x=120,y=510)

product = Button(win,text="Product",width=10,height=0,font="bold",command=btnpro)
product.place(x=300,y=80)

def btncus():
    frame1 = Frame(win,height=500,width=300,bg="black",borderwidth=1)
    frame1.place(x=30,y=200)

    customer1 = Label(win,text="CUSTOMER",fg="black",bg="beige",width=13,height=0,font="Arial 16 bold")
    customer1.place(x=105,y=230)

    def btnadd1():
        frame1 = Frame(win,height=500,width=1000,bg="maroon")
        frame1.place(x=330,y=200)

        frameadd = Frame(win,height=400,width=500,bg="rosybrown")
        frameadd.place(x=590,y=240)

        firstname = Label(win,text="First Name:",fg="black",bg="rosybrown",font="8")
        firstname.place(x=630,y=260)
        firstinput = Entry(win,width=30)
        firstinput.place(x=850,y=265) 

        lastname = Label(win,text="Last Name:",fg="black",bg="rosybrown",font="8")
        lastname.place(x=630,y=310)
        lastinput = Entry(win,width=30)
        lastinput.place(x=850,y=315)

        address = Label(win,text="Address:",fg="black",bg="rosybrown",font="10")
        address.place(x=630,y=360)
        addressinput = Entry(win,width=30)
        addressinput.place(x=850,y=365)

        city = Label(win,text="City:",fg="black",bg="rosybrown",font="10")
        city.place(x=630,y=410)
        cityinput = Entry(win,width=30)
        cityinput.place(x=850,y=415)

        state = Label(win,text="State:",fg="black",bg="rosybrown",font="10")
        state.place(x=630,y=460)
        stateinput = Entry(win,width=30)
        stateinput.place(x=850,y=465) 

        def click1():
            product = firstinput.get()
            category = lastinput.get()
            quantity = addressinput.get()
            price = cityinput.get()
            descri = stateinput.get()

            p1 = Product(product,category,quantity,price,descri)
            productList.append(p1)

            firstinput.delete(0,END)
            lastinput.delete(0,END)
            addressinput.delete(0,END)
            cityinput.delete(0,END)
            stateinput.delete(0,END)

        submit = Button(win,text="Submit",width=10,font="Arial 10 bold",command=click1)
        submit.place(x=750,y=550)

        reset = Button(win,text="Reset",width=10,font="Arial 10 bold",command=click1)
        reset.place(x=850,y=550)

    add = Button(win,text="ADD",width=13,height=0,font="Arial 12 bold",command=btnadd1)
    add.place(x=120,y=300)

    view = Button(win,text="VIEW",width=13,height=0,font="Arial 12 bold")
    view.place(x=120,y=370)

    update = Button(win,text="UPDATE",width=13,height=0,font="Arial 12 bold")
    update.place(x=120,y=440)

    delete = Button(win,text="DELETE",width=13,height=0,font="Arial 12 bold")
    delete.place(x=120,y=510)

customer = Button(win,text="Customer",width=10,height=0,font="bold",command=btncus)
customer.place(x=500,y=80)

bill_record = Button(win,text="Bill Records",width=10,height=0,font="bold")
bill_record.place(x=700,y=80)

billing = Button(win,text="Billing",width=10,height=0,font="bold")
billing.place(x=900,y=80)

def btnclo():
        frame1 = Frame(win,height=500,width=1000,bg="indigo")
        frame1.place(x=330,y=200)

        frameadd = Frame(win,height=400,width=500,bg="thistle")
        frameadd.place(x=590,y=240)

        def btnclose():
            win.destroy()

        close = Button(win,text="Close",width=10,height=3,font="Arial 10 bold",command=btnclose)
        close.place(x=790,y=350)


        reset = Button(win,text="Reset",width=10,height=3,font="Arial 10 bold")
        reset.place(x=790,y=450)


close = Button(win,text="Close",width=10,height=0,font="bold",command=btnclo)
close.place(x=1100,y=80)


win.mainloop()