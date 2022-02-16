import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
  
  
  
# adjust window
root=tk.Tk()
root.geometry("200x200")
  
# loading the images
img=ImageTk.PhotoImage(Image.open("Goa1.jpg"))
img2=ImageTk.PhotoImage(Image.open("Goa2.jpg"))
img3=ImageTk.PhotoImage(Image.open("Goa3.jpg"))
  
l=Label()
l.pack()
  
  
  
# using recursion to slide to next image
x = 1
  
# function to change to next image
def move():
    global x
    if x == 4:
        x = 1
    if x == 1:
        l.config(image=img)
    elif x == 2:
        l.config(image=img2)
    elif x == 3:
        l.config(image=img3)
    x = x+1
    root.after(2000, move)
  
# calling the function
move()
  
  
  
root.mainloop()
