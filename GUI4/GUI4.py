from tkinter import *

def clicked():
    res = "Введённый текст: {}".format(txt.get()) #функция get считывает строку
    lbl.configure(text=res) #вывод текста и текста с формы ввода
    
window = Tk() #создаём окно
window.title("Название окна") #название окна
window.geometry('440x250') #размеры окна

lbl = Label(window, text="Введённый текст: ") #добавить текст
lbl.grid(column=0, row=0) #позиция текста

txt = Entry(window, width=10) #форма ввода. Для выключения формы ввода , state='disabled
txt.grid(column=1, row=0) #позиция ввода

btn = Button(window, text="Жми", command=clicked) #добавить кнопку  
btn.grid(column=2, row=0) #позиция кнопки

window.mainloop() #функция бесконечный цикл окна
