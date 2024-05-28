import tkinter as tk 
from tkinter import  *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("750x75")
box = tk.Label(window,width = 10, borderwidth=4, relief=SUNKEN)
plus = tk.Label(text = "x")
box2 = tk.Label(window, width = 10, borderwidth=4, relief=SUNKEN)
equal = tk.Label(text = "=")
box3 = tk.Label(window, width = 20, borderwidth=4, relief=SUNKEN)


box.place(x=0,y=25)
plus.place(x=85,y=25)
box2.place(x=105,y=25)
equal.place(x=200,y=25)
box3.place(x=230,y=25)


window.mainloop()