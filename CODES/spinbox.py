from tkinter import*
win = Tk()
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenwidth()}")

spinbox = Spinbox(win,from_=0,to=100)
spinbox.pack(pady=10)

l1 = Label(win,text=f"",font="arial 16 bold")
l1.pack()

def get():
    num = spinbox.get()
    l1.config(text=f"Result is: {num}")
    # l1 = Label(win,text=f"Result is: {num}",font="arial 16 bold")
    # l1.pack()

btn = Button(win,text="Get Data",font="arial 16 bold",command=get)
btn.pack(pady=20)

win.mainloop()