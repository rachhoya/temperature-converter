from tkinter import *
import tkinter.font as font

window=Tk()
window.geometry("500x250")
window.config(background="pink")
window.title("temperature converter")

title=Label(window,text="Celsius to Fahrenheit",font=font.Font(size=20),fg="black")
title.place(x=130,y=20)

enter=Label(window,text="Enter temperature in Celsius:",font=font.Font(size=10))
enter.place(x=80,y=80)

entry1=Entry(window,width=30)
entry1.place(x=260,y=80)

convert=Button(window,text="Convert",font=font.Font(size=13),relief="raised")
convert.place(x=230,y=120)


window.mainloop()

