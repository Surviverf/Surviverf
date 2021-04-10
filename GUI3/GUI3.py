from tkinter import *

def clicked():
    lbl.configure(text="Видишь, работает!")

window = Tk() #создаём окно
window.title("Название окна") #название окна
window.geometry('440x250') #размеры окна
lbl = Label(window, text="Простой текст", font=("Arial Bold", 30)) #добавить текст
lbl.grid(column=0, row=0) #позиция текста
btn = Button(window, text="Жмякни!", bg="black", fg="red", command=clicked) #добавить кнопку  
btn.grid(column=1, row=0) #позиция кнопки
window.mainloop() #функция бесконечный цикл окна
