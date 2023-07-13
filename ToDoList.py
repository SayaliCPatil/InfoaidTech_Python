from tkinter import *
from PIL import ImageTk, Image

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

root = Tk()
root.title("To-Do List")

# Load the image and resize it to fit the window
image = Image.open("C:/Users/sayali c. patil/Desktop/python/TO_DO/image/1top.gif")
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)

# Load the icon image
add_icon = ImageTk.PhotoImage(Image.open("C:/Users/sayali c. patil/Desktop/python/TO_DO/image/icon.gif").resize((30, 30), Image.ANTIALIAS))
delete_icon = ImageTk.PhotoImage(Image.open("C:/Users/sayali c. patil/Desktop/python/TO_DO/image/delete.gif").resize((30, 30), Image.ANTIALIAS))




# Create a Label widget with the image as the background
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create task entry frame
frame = Frame(root)
frame.pack(pady=10)

task_entry = Entry(frame, font=("Helvetica", 14))
task_entry.pack(side=LEFT, padx=5)

add_button = Button(frame,image=add_icon, command=add_task, bd=0)
add_button.pack(side=LEFT)


# Create task listbox frame
listbox_frame = Frame(root)
listbox_frame.pack(pady=20)

listbox = Listbox(listbox_frame, width=50, height=10, font=("Helvetica", 12))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

delete_button = Button(root, image=delete_icon, command=delete_task, bd=0)
delete_button.pack(pady=10)

root.mainloop()
