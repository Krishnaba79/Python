from tkinter import*
win = Tk()

img = PhotoImage(file="./pic/6.png")
l1 = Label(win,image=img)
l1.pack()

l1 = Label(win,text="Hello World",fg="white",bg="gray",height=5,width=15,font="Arial 20 bold",borderwidth=10,relief=GROOVE,padx=50,pady=50)
l1.pack(fill=Y,side=LEFT)

win.mainloop()



# from tkinter import*
# from PIL import Image,ImageTk

# win = Tk()

# pil_img = Image.open("./pic/1.jpg")
# img_tk = ImageTk.PhotoImage(pil_img)
# l1 = Label(win,image=img_tk).pack()

# win.mainloop()


