from tkinter import *
import time
root = Tk()

Current_Time = ('%I:%M:%S %p')
Current_Date = ('%A, %B %d, %Y')

clock = Label(root, font=('times', 75, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)
def tick():
    s = time.strftime(Current_Time)
    if s != clock["text"]:
        clock["text"] = s
    clock.after(200, tick)
tick()

date = Label(root, font=('times', 41, 'bold'), fg='white', bg='black')
date.pack(fill=BOTH, expand=1)

def tick2():
    s2 = time.strftime(Current_Date)
    if s2 != date["text"]:
        date["text"] = s2
    date.after(200, tick2)
tick2()


root.mainloop()

