from tkinter import * #звёздочка в конце означает имортируем всё что есть в данном модуле
from tkinter.ttk import Combobox, Checkbutton, Radiobutton

def clicked():
    res = "Виджет Entry: {}".format(txt.get()) #функция get считывает ввод строки
    lbl.configure(text=res) #вывод текста и текста с формы ввода
    
window = Tk() #создаём окно
window.title("Название окна") #название окна
window.geometry('440x250') #размеры окна

lbl = Label(window, text="Текст Label: ") #добавить текст
lbl.grid(column=0, row=0) #позиция текста

txt = Entry(window, width=10) #форма ввода. Для выключения формы ввода , state='disabled
txt.grid(column=1, row=0) #позиция ввода

btn = Button(window, text="▲ Кнопка", command=clicked) #добавить кнопку  
btn.grid(column=2, row=0) #позиция кнопки

combo = Combobox(window) #создаём окно  
combo['values'] = ("Виджет Combobox →", 1, 2, 3, 4, 5 )#вводим значение  
combo.current(0)  #какую строку выводит?  
combo.grid(column=0, row=1) #размеры окна

chk_state = BooleanVar() #логический тип данных
chk_state.set(0)  # задайте проверку состояния чекбокса 0 False(Ложь), 1 True(Истина)  
chk = Checkbutton(window, text='← Виджет Checkbutton', var=chk_state) # 
chk.grid(column=0, row=2) #позиция кнопки

rad1 = Radiobutton(window, text='Первый', value=1) #Кнопка чекбокс с названием  
rad2 = Radiobutton(window, text='Второй', value=2) 
rad3 = Radiobutton(window, text='Третий', value=3)
rad1.grid(column=0, row=3) #позиция 
rad2.grid(column=1, row=3) #позиция 
rad3.grid(column=2, row=3) #позиция 

window.mainloop() #функция бесконечного окна
