    # RADIO BTN

# from tkinter import*
# win = Tk()

# selected_lan = StringVar()

# python = Radiobutton(win,text="pyton",variable=selected_lan,value="Pyton language")
# java = Radiobutton(win,text="java",variable=selected_lan,value="Java language")
# linux = Radiobutton(win,text="linux",variable=selected_lan,value="Linux language")

# l1 = Label(win,text="Ans is : ")
# def show():
#     name = selected_lan.get()
#     l1.config(text=f"result is : {name}")

# btn = Button(win,text="Show result",command=show)

# python.pack()
# java.pack()
# linux.pack()
# l1.pack()
# btn.pack()

# win.mainloop()


    # DROPDOWN BTN

from tkinter import*
win = Tk()

mylist = ["java","python","c sharp","mysql"]

myvar = StringVar(win)
myvar.set(mylist[0])    

drop_down = OptionMenu(win,myvar,*mylist)
drop_down.pack()

l1 = Label(win,text="Current Selected : ")
l1.pack()

def btnclick():
    CurrentSelectedItem = myvar.get()
    l1.config(text="CurrentSelectedItem")

btn = Button(win,text="Selected",command=btnclick)
btn.pack()

win.mainloop()