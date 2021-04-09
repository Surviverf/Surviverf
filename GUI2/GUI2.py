from tkinter import *


window = Tk() #создаём окно
window.title("Название окна") #название окна
window.geometry('400x250') #размеры окна
lbl = Label(window, text="это простой текст") #добавить текст
lbl.grid(column=0, row=0) #позиция текста
btn = Button(window, text="Кнопка жми!") #добавить кнопку  
btn.grid(column=1, row=0) #позиция кнопки
window.mainloop() #функция бесконечный цикл окна
