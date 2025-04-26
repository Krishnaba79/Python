from tkinter import*

win = Tk()
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenwidth()}")

def onchange(value):
    # l1.config(text=f"Result : {value}")
    l1.config(font=f"arial {value} bold")

scale = Scale(win,from_=0,to=100,orient=HORIZONTAL,command=onchange)
scale.pack()

l1 = Label(win,text="RESULT : 50",font="arial 16 bold")
l1.pack()

win.mainloop()