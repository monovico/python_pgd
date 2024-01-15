from tkinter import *

w = Tk()
def left_clicked(event):
    print('left mouse button clicked')
    return

def right_clicked(event):
    print('right mouse button clicked')
    return    

button = Button(w,text='!!!CLICK HERE!!!')
button.pack()
button.bind('<Button-1>',left_clicked)
button.bind('<Button-3>',right_clicked)

w.mainloop()