from  tkinter import*
window = Tk()

l1 =Label(window,text="Enter text: ")
l1.grid(column=0,row=0)

input = Entry(window)
input.grid(column=1,row=0)

def encrypt():
    text=input.get()
    en = ""
    ans = ""
    for j in text[ : :-1]:
        ans+=j
    for i in ans:
        x=ord(i)+1
        en += chr(x)

    # for j in range[len(en)-1:-1:-1]:
    #     ans+=en[j]
    result.config(text=en)

def decrypt():
    text=input.get()
    en = ""
    ans = ""
    for j in text[ : :-1]:
        ans+=j
    for i in ans:
        x=ord(i)-1
        en += chr(x)
    result.config(text=en)

b1=Button(window,text="Encrypt",command=encrypt)
b1.grid(column=0,row=1)

b2=Button(window,text="Decrypt",command=decrypt)
b2.grid(column=1,row=1)

result=Label(window)
result.grid(column=0,row=2)

window.mainloop()