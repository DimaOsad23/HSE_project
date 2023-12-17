# Импорт модуля для создания меню и запуска функциональной части
from start import *

from tkinter import *

try:
    root = Tk()
    root.resizable(width=False, height=False)
    root.title("Геометрия")
    root.geometry("1120x640")
    # Размещение панели для кнопок
    pn_control = Frame(root, height=640, width=480, bg="gray94")
    pn_control.pack(side=LEFT)
    # Размещение панели для графики
    pn_graph = Frame(root, height=640, width=640)
    pn_graph.pack(side=RIGHT)
    # Создаётся и размещается холст для системы координат
    canvas = Canvas(
        pn_graph,
        height=640,
        width=640,
        bg="white",
        highlightthickness=0)
    canvas.place(height=640, width=640)
    # Запуск меню и функциональной части программы
    st = Start(root, pn_control, pn_graph, canvas)
    st.start()
    root.mainloop()
except KeyboardInterrupt:
    pass
