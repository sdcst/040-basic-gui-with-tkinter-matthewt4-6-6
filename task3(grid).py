import tkinter as tk 
from tkinter import  *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("400x300")

dogphoto = PhotoImage(file="dog.png")
photo = tk.Label(window, image=dogphoto)
text1 = tk.Label(window, text = "Pochacco!",)
text2 = tk.Label(window,text="A cuddy little puppy! This is from the same\n creators who brought you Keropi and Kero Kero", bg="cyan")

text2.grid(row = 2, column = 1, columnspan = 4)
photo.grid(row = 1, column = 2)
text1.grid(row = 1, column = 3)


window.mainloop()