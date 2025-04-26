from tkinter import*

win = Tk()
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenwidth()}")

mycanvas = Canvas(win,bg="pink",height=win.winfo_screenheight(),width=win.winfo_screenwidth())
# mycanvas.pack()
mycanvas.place(x=0,y=0)

# mycanvas.create_line(0,0,300,300,fill="red")
mycanvas.create_oval(0,0,300,300,fill="gray")

def btnclick():
    mycanvas.create_rectangle(300,300,600,600,fill="blue")          # x0 , y0 , x1 , y1

btn = Button(mycanvas,text="click",bg="black",fg="white",font="arial 20 bold",command=btnclick)
btn.place(x=700,y=10)
 
win.mainloop()