from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('1000x600')
root.minsize(300,200)
root.maxsize(1000,600)

# Create a frame to hold the label widget
frame = Frame(root)
frame.pack(side=TOP, fill=BOTH, expand=True)

diceintro = Image.open('infodicerollbetting.png')
dice_intro = ImageTk.PhotoImage(diceintro)

# Create a label widget with a background color
label = Label(frame, bg='white')
label.pack(side=TOP, fill=BOTH, expand=True)

def resize_image(event):
    # Use after() method to delay the resizing operation
    root.after(2000, resize_image_delayed, event)

def resize_image_delayed(event):
    # Resize the image and update the label
    new_width = event.width
    new_height = event.height
    resized_image = diceintro.resize((new_width, new_height))
    global dice_intro
    dice_intro = ImageTk.PhotoImage(resized_image)
    label.config(image=dice_intro)

root.bind('<Configure>', resize_image)

# Create a check button and a proceed button
check_var = BooleanVar()
check_button = Checkbutton(root, text="I am 18 or above", variable=check_var)
check_button.pack(side=TOP, pady=10)

proceed_button = Button(root, text="Proceed", state=DISABLED)
proceed_button.pack(side=TOP, pady=10)

def enable_proceed_button():
    # Enable the proceed button if the user is 18 or above
    if check_var.get():
        proceed_button.config(state=NORMAL)
    else:
        proceed_button.config(state=DISABLED)

check_var.trace("w", lambda name, index, mode: enable_proceed_button())

root.mainloop()
