from tkinter import *  
from tkinter import scrolledtext, messagebox, filedialog, Menu
from tkinter.ttk import Progressbar  
from tkinter import ttk

def clicked():  
    messagebox.showinfo('Заголовок', 'Сотри кнопка ОК!')
    messagebox.showwarning('Заголовок', 'Оуууууууууу!')  # показывает предупреждающее сообщение
    messagebox.showerror('Заголовок', 'АААААААААААА!')  # показывает сообщение об ошибке
    res = messagebox.askquestion('Заголовок', 'Да или Нет?')
    res = messagebox.askyesno('Заголовок', 'Ты уверен(а)?')
    res = messagebox.askyesnocancel('Заголовок', 'Слушай может передумаешь?')
    res = messagebox.askokcancel('Заголовок', 'Ну смотри тебе чинить!')
    res = messagebox.askretrycancel('Заголовок', 'БААААААбАААААххххххххххX!')
    
window = Tk()  
window.title("Добавление виджета ScrolledText")  
window.geometry('400x250')

menu = Menu(window)  
new_item = Menu(menu, tearoff=0)  
new_item.add_command(label='Новый')  
menu.add_cascade(label='Файл', menu=new_item)
new_item.add_command(label='Новый', command=clicked)
window.config(menu=menu)

txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.insert(INSERT, 'Это текстовое поле, сотри меня! Напиши что нибудь очень очень длинное') #это метод введённого текста
#txt.delete(1.0, END)  # мы передали координаты очистки
txt.grid(column=0, row=0)

btn = Button(window, text='Жмякни', command=clicked)  
btn.grid(column=1, row=1)

var = IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
#spin = Spinbox(window, from_=0, to=10, width=5)
#spin = Spinbox(window, values=(3, 8, 11), width=5)
spin.grid(column=0, row=1)

style = ttk.Style()  
style.theme_use('default')  
style.configure("black.Horizontal.TProgressbar", background='black')  
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')  
bar['value'] = 70  
bar.grid(column=0, row=2)

window.mainloop()
