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

photo.place(x = 100, y = 10)
text1.place(x = 170, y = 50)
text2.place(x = 50, y = 120)


window.mainloop()