from tkinter import*

win = Tk()

def gettext():
    print(text.get("1.0","end-1c"))

btn = Button(win,text="Get Text",command=gettext)
btn.pack()


text = Text(win,wrap=WORD)
text.pack(fill=BOTH,expand=True)

win.mainloop()