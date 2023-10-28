from tkinter import *
from math import *
import sys

window = Tk()
window.title('Calculadora')
window.geometry('500x600+500+100')
window.config(bg = '#778899')

num = Entry(window, width = 50)
num.place(x = 100, y = 25)

bt1 = Button(window, text ='7', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
bt1.place(x = 50, y = 150)

bt2 = Button(window, text ='8', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
bt2.place(x = 150, y = 150)

bt3 = Button(window, text ='9', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
bt3.place(x = 250, y = 150)

bt4 = Button(window, text ='4', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
bt4.place(x = 50, y = 225)

bt5 = Button(window, text ='5', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
bt5.place(x = 150, y = 225)

bt6 = Button(window, text ='6', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
bt6.place(x = 250, y = 225)

bt7 = Button(window, text ='1', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
bt7.place(x = 50, y = 300)

bt8 = Button(window, text ='2', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
bt8.place(x = 150, y = 300)

bt9 = Button(window, text ='3', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
bt9.place(x = 250, y = 300)

btn10 = Button(window, text ='+/-', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
btn10.place(x = 50, y = 375)

btn11 = Button(window, text ='0', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
btn11.place(x = 150, y = 375)

btn12 = Button(window, text =',', relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
btn12.place(x = 250, y = 375)

div = Button(text = "/", relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
div.place(x = 350, y = 75)

multi = Button(text = "*", relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
multi.place(x = 350, y = 150)

sub = Button(text = "-", relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
sub.place(x = 350, y = 225)

soma = Button(text = "+", relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
soma.place(x = 350, y = 300)

igual = Button(text = "=", relief = FLAT, width = 10, height = 3, fg='#FFFAFA', bg='#1C1C1C')
igual.place(x = 350, y = 375)

window.mainloop()
