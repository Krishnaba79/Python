from tkinter import*

win = Tk()
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.geometry(f"{h}x{w}")

    # main menu

# mymenu = Menu(win)
# def save():
#     print("Saved file")
# def settings():
#     print("Settings open")
# mymenu.add_command(label="File",command=save)
# mymenu.add_command(label="settings",command=settings)

mymenu = Menu(win)
mainmenu = Menu(win)
filemenu = Menu(mainmenu)
editmenu = Menu(mainmenu)

newfilelan = Menu()
newfilelan.add_command(label="Hindi")
newfilelan.add_command(label="English")
newfilelan.add_command(label="Gujarati")
filemenu.add_cascade(label="LANGUAGE",menu=newfilelan)

filemenu.add_command(label="NEW FILE")
filemenu.add_command(label="OPEN FILE")
filemenu.add_command(label="SAVE AS")
mainmenu.add_cascade(label="SAVE",menu=filemenu)

editmenupaste = Menu()
editmenupaste.add_command(label="Paste Formating")
editmenupaste.add_command(label="Paste Normal")
editmenu.add_cascade(label="PASTE",menu=editmenupaste)

editmenuselect = Menu()
# editmenuselect.add_command(label="Select All")
editmenu.add_cascade(label="SELECT",menu=editmenuselect)

selectall = Menu()
selectall.add_command(label="New Select")
selectall.add_command(label="Clipbord")
selectall.add_command(label="File")
editmenuselect.add_cascade(label="SELECT ALL",menu=selectall)


editmenu.add_command(label="CUT")
editmenu.add_command(label="COPY")
mainmenu.add_cascade(label="EDIT",menu=editmenu)

exitmenu = Menu(mainmenu)
mainmenu.add_cascade(label="EXIT",menu=exitmenu)

win.config(menu=mainmenu)

win.mainloop()