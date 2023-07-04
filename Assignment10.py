import tkinter as tk
import webbrowser as wb
obj=tk.Tk()

#button
e=tk.Entry(obj,font=("Times New Roman",30),width=30,background="blue")
e.grid(row=0,column=0)

def display():
    s=e.get()
    print(s)   
    wb.open(f"https://www.twitch.tv//search?keyword={s}") 

b1=tk.Button(obj,text="Search",font=("Times New Roman",20),command=display,activebackground="yellow")
b1.grid(row=1,column=0)

b=tk.Button(obj,text="Close",font=("Times New Roman",20),command=obj.destroy,activebackground="yellow")
b.grid(row=2,column=0)
obj.mainloop()