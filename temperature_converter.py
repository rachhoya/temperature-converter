from tkinter import *
import tkinter.font as font

window=Tk()
window.geometry("500x250")
window.config(background="pink")
window.title("temperature converter")

def convert():
    answer=entry1.get()
    if(answer.replace('.','',1).isdigit()):
        error.grid_forget()
        fahrenheit=(float(answer)*1.8)+32
        output.config(text="temperature in Fahrenheit: " + str(fahrenheit))
    else:
        error.place(x=315,y=105)



title=Label(window,text="Celsius to Fahrenheit",font=font.Font(size=20),fg="black")
title.place(x=130,y=20)

enter=Label(window,text="Enter temperature in Celsius:",font=font.Font(size=10))
enter.place(x=125,y=80)

entry1=Entry(window,width=10,font=font.Font(size=11))
entry1.place(x=315,y=80)

convert=Button(window,text="Convert",font=font.Font(size=13),relief="raised",command=convert)
convert.place(x=220,y=150)

error=Label(window,text="Please enter valid input",font=font.Font(size=8),fg="red")

output=Label(window,font=12)
output.place(x=150,y=200)

window.mainloop()
