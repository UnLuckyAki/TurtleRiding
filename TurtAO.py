import tkinter
import turtle
import tkinter.messagebox
from tkinter import ttk
window = tkinter.Tk()

canvas = tkinter.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
#draw = turtle.Turtle()
draw = turtle.RawTurtle(canvas)

def Board(a, x, y, size):
    pass

def Board2():
    pass

def Button_click ():
    tkinter.messagebox.showinfo("Game", "Tic Tac Toe")

#button = tkinter.Button(window, text = "Play!", command = Button_click)
#button = Tk.Button(window, text = "Play!", command = Button_click)
#button.pack()
#
Play_Button = tkinter.Button(master = window, text ="Старт!", command = Button_click)
Play_Button.config(bg="cyan",fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

Board_Button = tkinter.Button(master = window, text ="Начать скачки", command = Board2)
Board_Button.config(bg="cyan",fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')


list_down = ttk.Combobox(window) #Создали выпадающий список, указали - где он будет вообще
list_down['values']= (1, 2, 3, 4, 5, "Text") #Указали значения, которые будут в выпадающем списке
list_down.current(4) #set the selected item #Указали значение "По-умолчанию" - важно не забывать, что отсчет в Python идет с нуля ;) т.е. в данном случае значением "по-умолчанию" будет цифра 5.
list_down.config(font=("Courier", 44), width=2)
list_down.grid(padx=2, pady=1, row=2, column=11, sticky='nsew')



window.mainloop()
