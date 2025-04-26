from tkinter import*

win = Tk()
win.geometry("500x500")

lf = LabelFrame(win,text="Personal Details")
lf.pack(padx=10,pady=10)

name = Label(lf,text="NAME")
name.grid(row=0,column=0)
nentry = Entry(lf)
nentry.grid(row=0,column=1)

email = Label(lf,text="EMAIL")
email.grid(row=1,column=0)
eentry = Entry(lf)
eentry.grid(row=1,column=1)

win.mainloop()