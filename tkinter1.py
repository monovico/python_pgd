from tkinter import *

w = Tk()

def click(event):
    print("X:{},Y:{}".format(event.x,event.y))   

frame = Frame(w,width=200,height=200)
frame.pack()
frame.bind('<Button-1>',click)


w.mainloop()