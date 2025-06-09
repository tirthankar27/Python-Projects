from tkinter import *

window=Tk()
window.minsize(height=80,width=200)
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

label1=Label(text="Miles")
label1.grid(row=0,column=2)
label2=Label(text="is equal to")
label2.grid(row=1,column=0)
label3=Label(text="Km")
label3.grid(row=1,column=2)

input=Entry(width=10)
input.grid(row=0,column=1)

def change_val():
    val=float(input.get())*1.61
    label4.config(text=f"{val}")

label4=Label(text=f"{0.0}")
label4.grid(row=1,column=1)

button=Button(text="Calculate",command=change_val)
button.grid(row=2,column=1)
window.mainloop()
