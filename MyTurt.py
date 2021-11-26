import tkinter
import turtle
import tkinter.messagebox

window = tkinter.Tk()

canvas = tkinter.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)
draw = turtle.RawTurtle(canvas)


window.mainloop()