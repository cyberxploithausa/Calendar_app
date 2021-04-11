from tkinter import *
import calendar


text = calendar.calendar(2021)

root = Tk()
root.geometry("700x800")
root.title("Cyber Calendar")
root.config(background='White')

label = Label(root, text='CALENDAR', bg="dark gray", font=('times', 28, 'bold'))
label.grid(row=1, column=1)

label1 = Label(root, text=text, font="consolas 10 bold")
label1.grid(row=2, column=1, padx=20)


root.mainloop()