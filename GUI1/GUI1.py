from tkinter import *


window = Tk() #создаём окно
window.title("Название окна") #название окна
window.geometry('400x250') #размеры окна
lbl = Label(window, text="это простой текст") #простой текст
lbl.grid(column=0, row=0) #положение текста в окне  
window.mainloop() #функция бесконечный цикл окна
