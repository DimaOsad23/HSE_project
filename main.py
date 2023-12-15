from start import *  # Импорт модуля, который запускает функциональную часть 
from tkinter import *  # Импорт модуля для интерфейса


try:
    # Создаётся окно программы
    root = Tk()
    root.resizable(width=False, height=False)
    root.title("Геометрия")
    root.geometry("1120x640")
    # Создаются и размещаются две панели окна: панель с системой координат и панель для кнопок
    pn_control = Frame(root, height=640, width=480, bg='gray94')
    pn_control.pack(side=LEFT)
    pn_graph = Frame(root, height=640, width=640)
    pn_graph.pack(side=RIGHT)
    # Создаётся и размещается холст, на котором будет нарисована система координат
    canvas = Canvas(pn_graph, height=640, width=640, bg='white', highlightthickness=0)
    canvas.place(height=640, width=640)
    # Создаётся объект класса Start() и применяется метод этого класса, который запускает функциональную часть программы
    st = Start(root, pn_control, pn_graph, canvas)
    st.start()

    root.mainloop()
except:
    pass