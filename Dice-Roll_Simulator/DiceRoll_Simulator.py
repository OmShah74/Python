from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry('1300x700')
root.minsize(300,200)
root.maxsize(1366,768)
diceintro=Image.open('infodicerollbetting.png')
dice_intro=ImageTk.PhotoImage(diceintro)
label=Label(image=dice_intro)
label.pack(expand=True,fill='both')

def resize_image(event):
    new_width=event.width
    new_height=event.height
    resized_image=diceintro.resize((new_width, new_height))
    global dice_intro
    dice_intro=ImageTk.PhotoImage(resized_image)
    label.config(image=dice_intro)

root.bind('<Configure>',resize_image)
root.mainloop()
