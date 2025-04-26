    # bassic tkinter

# from tkinter import*
# window = Tk()
# window.title("Hello world")
# l1 = Label(window,text="Hello world")
# l1.pack()
# btn = Button(window,text="lable 2")
# btn.pack()
# window.mainloop()

    # grid

# from tkinter import *
# window = Tk()
# window.geometry("600x600")
# l1 = Label(window,text="conter:")
# l1.grid()
# def btnclicked():
#     print("btn was clicked")
#     l1.config(text="Hello")
# btn = Button(window,text="click here",command=btnclicked)
# btn.grid(column=1,row=0)
# window.mainloop()

    # for middel sentence

# from tkinter import*
# window = Tk()
# Frame = Frame(window)
# Frame.pack()
# Label1 = Label(Frame,text="this is inside frame widge")
# Label1.pack()
# window.mainloop()

    # clike btn and change num
# from tkinter import*
# window = Tk()
# window.geometry("600x600")
# l1 = Label(window,text="0")
# l1.grid()
# num = 0
# def btnclicked():
#     print("btn clicked")
#     global num
#     num += 1
#     l1.config(text = num)

# btn = Button(window,text="click me",command = btnclicked)
# btn.grid(column=1,row=0)
# window.mainloop()


    #btn styling
from tkinter import*
# from tkinter.ttk import*

window = Tk()
window.geometry("400x500")

# style = Style()
# style.configure('W.TButton',
#                 font=('calibri',10,'bold','undeline'),
#                 foreground='red')


btn1 = Button(window,text='Quite !',command=window.destroy,bg='blue',fg='black',font='arial 10 bold')
btn1.grid(row = 0,column = 3, pady=10)

btn2 = Button(window,text='Click me !',command=None)
btn2.grid(row = 1,column = 3, pady= 10, padx= 10)

window.mainloop()
