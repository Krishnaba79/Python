from tkinter import*

win = Tk()
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenwidth()}")

mycanvas = Canvas(win,height=win.winfo_screenheight(),width=win.winfo_screenwidth())
mycanvas.place(x=0,y=0)

# mycanvas.create_rectangle(0,0,100,100,fill="black")
# mycanvas.create_rectangle(100,0,200,100,fill="white")
# mycanvas.create_rectangle(200,0,300,100,fill="black")

x1 = 0
y1 = 100
x2 = 100
y2 = 200

color = False

def btnclick():
    global x1,y1,x2,y2,color

    if color:
        mycolor = "white"
    else:
        mycolor = "black"

    if x2 > win.winfo_screenwidth():
        x1 = 0
        y1 = y1 + 100
        x2 = 100
        y2 = y2 + 100

    mycanvas.create_rectangle(x1,y1,x2,y2,fill=mycolor)
    x1 += 100
    x2 += 100

    color = not(color)

btn = Button(mycanvas,text="click",bg="black",fg="white",font="arial 20 bold",command=btnclick)
btn.place(x=700,y=10)

win.mainloop()
