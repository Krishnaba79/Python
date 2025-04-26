#     # password typ

# from tkinter import*
# window = Tk()

# window.geometry("400x300")

# l1 = Label(window,text="Enter your password : ")
# l1.grid(row=0,column=0)

# Entry1 = Entry(window)
# Entry1.grid(row=0,column=1)

# l2 = Label(window,text="..")
# l2.grid(row=2,column=0)

# def btnclick():
#     password = Entry1.get()
#     passwordsize = len(password)

#     if passwordsize > 8:
#         l2.config(text="Successful",fg="green")
#     else:
#         l2.config(text="Error : password must of 8 characters",fg="red")

# btn = Button(window,text="submit",command=btnclick)
# btn.grid(row=1,column=0)

# window.mainloop()

# from tkinter import*
# window = Tk()

# window.geometry("300x200")

# l1 = Label(window,text="Enter your name : ")
# l1.grid(row=0,column=0)

# NameInput = Entry(window,width=50)
# NameInput.grid(row=0,column=1)

# l2 = Label(window,text="Your Name : ")
# l2.grid(row=2,column=0)

# def btnclick():
#     NameInput.delete(0,END)
#     NameInput.insert(0,"paragraph")

# b1 = Button(window,text="submit",command=btnclick)
# b1.grid(row=1,column=0)

# window.mainloop()


# from tkinter import*
# win = Tk()
# w = win.winfo_screenmmwidth()
# h = win.winfo_screenheight()

# print(w,h)
# win.geometry("{}x{}".format(w,h))

# btn = Button(win,text="click")
# btn.place(x=100,y=0)

# frame1 = Frame(win,height=300,width=500,bg="gray")
# frame1.place(x=100,y=10)

# frame2 = Frame(win,height=300,width=500,bg="pink")
# frame2.place(x=100,y=10)

# def btnclicked():
#     frame1.config(bg="black",width=700)

# btn2 = Button(win,text="click",bg="blue",command=btnclicked)
# btn2.place(x=0,y=0)

# win.mainloop()

