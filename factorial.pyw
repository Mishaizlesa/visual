from tkinter import *
from math import factorial
def answer():
    lbl_2.configure(text=str(factorial(int(entry.get()))))
window = Tk()
window.title("Calculate the factorial")
window.geometry("400x250")
lbl=Label(window, text="What's the number, that you wanna know factorial of?", bg="blue", fg="red")
lbl.grid(column=0, row=0)
window["bg"]="blue"
entry=Entry(window, width=20)
entry.grid(column=0, row=1)
lbl_2=Label(window, text="", bg="blue", fg="red", font=("Arial bold", 20))
lbl_2.grid(column=0, row=2)
button=Button(window, text="get the answer", command=answer, bg="blue", fg="red")
button.grid(column=1, row=1)
mainloop()