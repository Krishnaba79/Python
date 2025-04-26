from tkinter import *

win = Tk()
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.geometry(f"{w}x{h-70}")

# main white color full screen frame
frame = Frame(win, width=w, height=h, bg="white")
frame.place(x=0, y=0)

# Phone title heading (Iphone 13 )
title = Label(frame, text="Apple iPhone 13 (128GB)",
              bg="white", font="Arial 24 bold")
title.place(x=720, y=130)

# red color deal sticker
dealLabel = Label(frame, text="Limited time deal", bg="red",
                  fg="white", padx=10, pady=5, font="Arial 12 bold")
dealLabel.place(x=720, y=190)

# current color Label
colorLabel = Label(frame, text="Color : Red", bg="white",
                   padx=10, pady=5, font="Arial 12 bold")
colorLabel.place(x=720, y=240)

# Price Label
PriceLabel = Label(frame, text="₹ 50000", bg="white", font="Arial 24 bold")
PriceLabel.place(x=720, y=300)

# current color selected
phonecolor = "red"

# current image position
currentNum = 1


# change color of phone ('red','blue','green','black')
def colorChange(color):
    global phonecolor
    phonecolor = color

    global currentNum
    currentNum = 1

    image.config(file=f"./images/{color}/1.PNG")
    colorLabel.config(text=f"Color : {color.capitalize()}")


# colors Buttons
redBtn = Button(frame, bg="red", height=2, width=3,
                command=lambda: colorChange('red'))
redBtn.place(x=720, y=370)

blueBtn = Button(frame, bg="skyblue", height=2, width=3,
                 command=lambda: colorChange('blue'))
blueBtn.place(x=760, y=370)

greenBtn = Button(frame, bg="darkgreen", height=2, width=3,
                  command=lambda: colorChange('green'))
greenBtn.place(x=800, y=370)

blackBtn = Button(frame, bg="darkgrey", height=2, width=3,
                  command=lambda: colorChange('black'))
blackBtn.place(x=840, y=370)


# Phone Image
image = PhotoImage(file="./images/red/1.PNG")
imageLabel = Label(frame, image=image, width=400, height=600, bg="white")
imageLabel.place(x=200, y=100)


# calculating total price [ price * quantity ]
def get():
    num = int(spinBox.get())
    PriceLabel.config(text=f"₹ {50000 * int(num)}")


spinBox = Spinbox(frame, from_=1, to=10, command=get, font="Arial 20 bold")
spinBox.place(x=720, y=470)


# changing image for same color (1,2,3) [NEXT, PREVIOUS]
def changeimage(func):
    global currentNum

    if func:
        # Next image
        currentNum += 1
        if currentNum > 3:
            currentNum = 1
    else:
        # Previous image
        currentNum -= 1
        if currentNum < 1:
            currentNum = 3

    image.config(file=f"./images/{phonecolor}/{currentNum}.PNG")

    # Update the current image text
    currentImageText.config(text=f"{currentNum}/3")


# Initialize the image to the first one
image.config(file=f"./images/{phonecolor}/{currentNum}.PNG")

# previous button
previousBtn = Button(frame, text="Previous", padx=10,
                     pady=5, command=lambda: changeimage(0))
previousBtn.place(x=720, y=560)

# next button
nextButton = Button(frame, text="Next", padx=10, pady=5,
                    command=lambda: changeimage(1))
nextButton.place(x=950, y=560)

# show current image position  1/3
currentImageText = Label(frame, text="1/3", font="Arial 20 bold")
currentImageText.place(x=850, y=560)


# Buy now button
nextButton = Button(frame, text="Next", padx=10, pady=5,
                    command=lambda: changeimage(1))
nextButton.place(x=950, y=560)

win.mainloop()
