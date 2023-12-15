from work import *  # Импорт функциональной части
from tkinter import *  # Импорт модуля для интерфейса



# Создаётся класс, методы которого создают меню, события (ничинают работу функциональной части)
class Start:

    # Задаются переменные класса
    def __init__(self, root, pn_control, pn_graph, canvas):
        self.root = root  # Главное окно
        self.pn_control = pn_control  # Панель кнопок
        self.pn_graph = pn_graph  # Панель системы координат
        self.canvas = canvas  # Холст
        self.main_menu = Menu(self.root)  # Создаётся объект меню (создаётся меню)
        # Создание объекта класса, который содержит функциональную часть программы
        self.wrk = Work(root, pn_control, pn_graph, canvas)

    # Метод, который создаёт меню и начинает обработку событий
    def start(self):
        self.menu_1()  # Создаётся пункт меню для ввода
        self.menu_2()  # Создаётся пункт меню для вывода
        self.menu_3()  # Создаётся пункт меню для редактирования
        self.menu_4()  # Создаётся пункт меню для решеня
        self.menu_5()  # Создаётся пункт меню для получения информации
        self.menu_6()  # Создаётся пункт меню для настроек
        self.main_menu.add_command(label="Выход", command=self.wrk.quit)  # Создаётся пункт меню для выхода
        self.root.config(menu=self.main_menu)  # Вывод меню
        self.canvas.focus_set()  # Фокус переводится на холст
        # Начинается обработка событий
        self.canvas.bind('<MouseWheel>', self.wrk.mouse_wheel)  # Событие для изменения масштаба колёсиком мыши
        self.canvas.bind('<Motion>', self.wrk.moving_mouse)  # События для вывода координат крсора на холте
        # Начало обработки событий для перемещения по системе координат при помощи стрелок клавиатуры
        self.canvas.bind('<Left>', self.wrk.left_ar)
        self.canvas.bind('<Up>', self.wrk.up_ar)
        self.canvas.bind('<Right>', self.wrk.right_ar)
        self.canvas.bind('<Down>', self.wrk.down_ar)
        # Начинает обрабатываться cобытие для разрушения лейбла с координатами при покидании холста курсором
        self.canvas.bind('<Leave>', self.wrk.leave_canvas)
        # Начинается обрабатываться событие, которое включает обработку других событий при наведении курсора на холст
        self.canvas.bind('<Enter>', self.wrk.enter_canvas)
        # Начинают обрабатываться события для перемещения по системе координат при помощи мыши
        self.canvas.bind('<Button-3>', self.wrk.mouse_move_coords_sys_click)
        self.canvas.bind('<B3-Motion>', self.wrk.mouse_move_coords_sys_move)
        self.wrk.coord()  # Запуск метода, рисующего систему координат

    # Метод, создающий пункт меню для ввода
    def menu_1(self):
        file_menu1 = Menu(self.main_menu, tearoff=0)
        file_menu1.add_command(label="Клавиатура", command=lambda: self.wrk.keyboard('input'))
        file_menu1.add_command(label="Мышь", command=lambda: self.wrk.mouse('input'))
        file_menu1.add_command(label="Файл", command=lambda: self.wrk.file('input'))
        file_menu1.add_command(label="Random", command=lambda: self.wrk.random('input'))
        self.main_menu.add_cascade(label="Ввод", menu=file_menu1)

    # Метод, создающий пункт меню для вывода
    def menu_2(self):
        file_menu2 = Menu(self.main_menu, tearoff=0)
        file_menu2.add_command(label="Файл", command=self.wrk.output_file)
        file_menu2.add_command(label="Экран", command=self.wrk.output_screen)
        self.main_menu.add_cascade(label="Вывод", menu=file_menu2)

    # Метод, создающий пункт меню для редактирования
    def menu_3(self):
        file_menu3 = Menu(self.main_menu, tearoff=0)
        file_menu3.add_command(label="Очистить экран", command=self.wrk.clear_all)
        file_menu3.add_command(label="Редактировать точку", command=self.wrk.editing)
        vst_menu = Menu(file_menu3, tearoff=0)
        vst_menu.add_command(label='Клавиатура', command=lambda: self.wrk.keyboard('insert'))
        vst_menu.add_command(label='Мышь', command=lambda: self.wrk.mouse('insert'))
        vst_menu.add_command(label='Файл', command=lambda: self.wrk.file('insert'))
        vst_menu.add_command(label='Random', command=lambda: self.wrk.random('insert'))
        file_menu3.add_cascade(label="Вставить", menu=vst_menu)
        self.main_menu.add_cascade(label="Редактирование", menu=file_menu3)

    # Метод, создающий пункт меню для решения
    def menu_4(self):
        file_menu4 = Menu(self.main_menu, tearoff=0)
        file_menu4.add_command(label="Решение", command=self.wrk.solution_of_task)
        file_menu4.add_command(label="Решение с выпуклой оболочкой", command=self.wrk.solution_2_of_task)
        self.main_menu.add_cascade(label="Решение", menu=file_menu4)

    # Метод, создающий пункт меню для получения информации
    def menu_5(self):
        help_menu = Menu(self.main_menu, tearoff=0)
        help_menu.add_command(label="Задача", command=self.wrk.task)
        help_menu.add_command(label="Об авторе", command=self.wrk.author)
        help_menu.add_command(label="Перемещение по плоскости", command=self.wrk.moving)
        self.main_menu.add_cascade(label="Справка", menu=help_menu)

    # Метод, создающий пункт меню для настроек
    def menu_6(self):
        set_menu = Menu(self.main_menu, tearoff=0)
        set_menu.add_command(label="Цвет фона", command=self.wrk.start_change_bg_color)
        self.main_menu.add_cascade(label="Настройки", menu=set_menu)
