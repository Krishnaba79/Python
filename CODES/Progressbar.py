from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Progress bar Modes")

determinate = ttk.Progressbar(win,mode="determinate",length=300)
determinate.pack(pady=10)
determinate["value"] = 30

indeterminate = ttk.Progressbar(win,mode="indeterminate",length=300)
indeterminate.pack(pady=10)
indeterminate["value"] = 100

def click():
    indeterminate.start()
    
btn = Button(win,text="click",command=click).pack()

win.mainloop()