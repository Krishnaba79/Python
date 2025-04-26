from tkinter import*
from tkinter import messagebox

win = Tk()
win.geometry("200x200")

def btnclick():
    # messagebox.showinfo("SPACE RUNNING OUT","Your disk space have no memory space.")
    # messagebox.showerror("SPACE RUNNING OUT","Your disk space have no memory space.")
    messagebox.showwarning("SPACE RUNNING OUT","Your disk space have no memory space.")

    result = messagebox.askquestion("Question","Are you sure to delete the fils")

    if result == "yes":
        messagebox.showinfo("DONE","You have selected YES")
    else:
        messagebox.showerror("ERROR","You have selected No")

btn = Button(win,text="selected",command=btnclick)
btn.pack(pady=20)

win.mainloop()