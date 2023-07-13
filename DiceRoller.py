from tkinter import *
from PIL import ImageTk, Image
import random

def roll_dice():
    global result_label
    
    num_dice = int(dice_var.get())
    dice_images = []
    for _ in range(num_dice):
        dice_number = random.randint(1, 6)
        dice_image = Image.open(f"C:/Users/sayali c. patil/Desktop/python/Dice_img/{dice_number}.gif")
        dice_image = dice_image.resize((100, 100), Image.LANCZOS)
        dice_images.append(ImageTk.PhotoImage(dice_image))
    
    result_label.config(image=dice_images[0])
    result_label.dice_images = dice_images

def quit_app():
    root.destroy()

root = Tk()
root.title("Dice Rolling Program")

select_frame = Frame(root)
select_frame.pack(pady=10)

label = Label(select_frame, text="Number of dice:", font=("Helvetica", 14))
label.pack(side=LEFT)

dice_var = StringVar()
dice_var.set("1")
dice_entry = Entry(select_frame, textvariable=dice_var, font=("Helvetica", 14), width=3)
dice_entry.pack(side=LEFT)

roll_frame = Frame(root)
roll_frame.pack(pady=10)

roll_button = Button(roll_frame, text="Roll Dice", font=("Helvetica", 14), command=roll_dice)
roll_button.pack(side=LEFT, padx=10)

result_label = Label(roll_frame)
result_label.pack(side=LEFT)

quit_button = Button(root, text="Quit", font=("Helvetica", 14), command=quit_app)
quit_button.pack(pady=10)

root.mainloop()
