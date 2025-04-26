from tkinter import*

win = Tk()

def toggle_check():
    if checkbox_var.get() == 1:
        print("CHECKED")
        frame.config(bg="lightblue")
        l1.config(text="LIGHT MODE",fg="black",bg="lightblue")
    else:
        print("UNCHECKED")
        frame.config(bg="black")
        l1.config(text="DARK MODE",fg="white",bg="Black")

checkbox_var = IntVar()

check_btn = Checkbutton(win,text="I AGREE",variable=checkbox_var,command=toggle_check)
check_btn.pack()

frame = Frame(win,width=1000,height=500,bg="gray")
frame.pack()

l1 = Label(frame,text="LIGHT MODE",fg="black",bg="white",width=1000,height=500,font="arial 36 bold")
l1.pack()

win.mainloop()