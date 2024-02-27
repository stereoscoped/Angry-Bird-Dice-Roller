"""
Angry Bird Dice Roller
2/24/2024
by stereoscoped
"""

import random
from PIL import ImageTk,Image
import time
import tkinter


# Creates the main window object
window = tkinter.Tk()
window.grid()
window.geometry("400x400")
window.maxsize(400, 400)
window.minsize(400,400)
window.title("Angry Bird Dice Roller")

def button_press():
    print("test")
    bird = random.randint(0, 5)
    print(bird)


# Canvas for bird image
canvas = tkinter.Canvas(window)
red = ImageTk.PhotoImage(Image.open("images/red.png"))
canvas.pack()
canvas.create_image(180,125, image=red)

def show_red():
    canvas = tkinter.Canvas(window)
    red = ImageTk.PhotoImage(Image.open("images/blue.png"))
    canvas.itemconfig(image_container,image=img2)
    canvas.pack()
    canvas.create_image(180,125, image=red)

# Creates the roll button
roll_button = tkinter.Button(window, text="Roll", width=25, command=lambda:show_red)
roll_button.pack()


# Infinite loop for window
window.mainloop()
