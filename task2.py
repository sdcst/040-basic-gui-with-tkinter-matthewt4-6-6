import tkinter as tk 
from tkinter import  *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic")
window.geometry("600x180")

dogphoto = PhotoImage(file="dog.png")
label = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text = "Search by Name", width = 12, borderwidth=4, relief=SUNKEN)
box2 = tk.Label(window, text = "          ",width = 12, borderwidth=4, relief=SUNKEN)
text1 = tk.Label(window, text = "Client Database",)
text2 = tk.Label(window, text = "Name",)
text3 = tk.Label(window, text = "Type",)
text4 = tk.Label(window, text = "Breed",)
text5 = tk.Label(window, text = "Owner",)
text6 = tk.Label(window, text = "Birth Date",)
nbox = tk.Label(window,width = 10, borderwidth=4, relief=SUNKEN)
tbox = tk.Label(window,width = 10, borderwidth=4, relief=SUNKEN)
bbox = tk.Label(window,width = 10, borderwidth=4, relief=SUNKEN)
obox = tk.Label(window,width = 10, borderwidth=4, relief=SUNKEN)
bdbox = tk.Label(window,width = 10, borderwidth=4, relief=SUNKEN)
label3 = tk.Label(window, text = "< Previous", width = 12, borderwidth=4, relief=SUNKEN)
label4 = tk.Label(window, text = "Next >", width = 12, borderwidth=4, relief=SUNKEN)
label5 = tk.Label(window,text="Save Entry", bg="#808080")


text1.grid(row = 2, column = 1, columnspan = 10)
text2.grid(row = 4, column = 1)
text3.grid(row = 4, column = 2)
text4.grid(row = 4, column = 3)
text5.grid(row = 4, column = 4)
text6.grid(row = 4, column = 5)
nbox.grid(row = 5, column = 1)
tbox.grid(row = 5, column = 2)
bbox.grid(row = 5, column = 3)
obox.grid(row = 5, column = 4)
bdbox.grid(row = 5, column = 5)
label.grid(row = 1, rowspan = 3, column = 1)
label2.grid(row = 1, column = 4)
box2.grid(row = 1, column = 5)
label3.grid(row = 6, column = 1)
label4.grid(row = 6, column = 5)
label5.grid(row = 6, column = 3)






window.mainloop()
