# Импорт функциональной части
from work import *

from tkinter import *


class Start:
    '''
    Class with functions that create menu and start processing of first events

    :param root: main window
    :type root: toplevel widget (instance of the Tk class)
    :param pn_control: panel for buttons and other widgets
    :type pn_control: widget (Frame)
    :param pn_graph: panel for coordinate system
    :type pn_graph: widget (Frame)
    :param canvas: canvas for coordinate system and drawing
    :type canvas: widget (Canvas)
    :ivar root: this is where we store root object
    :vartype root: toplevel widget (instance of the Tk class)
    :ivar pn_control: this is where we store pn_control object
    :vartype pn_control: widget (Frame)
    :ivar pn_graph: this is where we store pn_graph object
    :vartype pn_graph: widget (Frame)
    :ivar canvas: this is where we store canvas object
    :vartype canvas: widget (Canvas)
    :ivar main_menu: main menu
    :vartype main_menu: instance of the Menu class
    :ivar wrk: this is where we store functional part of project (most of the
    functions)
    :vartype wrk: instance of the Work class
    '''
    def __init__(self, root, pn_control, pn_graph, canvas):
        self.root = root
        self.pn_control = pn_control
        self.pn_graph = pn_graph
        self.canvas = canvas
        # Начало создания меню
        self.main_menu = Menu(self.root)
        # Подключение функциональной части
        self.wrk = Work(root, pn_control, pn_graph, canvas)

    def start(self):
        '''
        Call functions, that create menu and draw coordinate system,
        and star first events of canvas

        :returns: None
        :seealso: menu_1, menu_2, menu_3, menu_4, menu_5, menu_6, Work
        '''
        self.menu_1()  # Создаётся пункт меню для ввода
        self.menu_2()  # Создаётся пункт меню для вывода
        self.menu_3()  # Создаётся пункт меню для редактирования
        self.menu_4()  # Создаётся пункт меню для решеня
        self.menu_5()  # Создаётся пункт меню для получения информации
        self.menu_6()  # Создаётся пункт меню для настроек
        self.main_menu.add_command(label="Выход", command=self.wrk.quit)
        self.root.config(menu=self.main_menu)
        self.canvas.focus_set()
        # Начинается обработка событий
        # Начало события для изменения масштаба колёсиком мыши
        self.canvas.bind("<MouseWheel>", self.wrk.mouse_wheel)
        # Начало события для вывода и изменения координат кусора
        self.canvas.bind("<Motion>", self.wrk.moving_mouse)
        # Начало обработки событий для перемещения по СК клавиатурой
        self.canvas.bind("<Left>", self.wrk.left_ar)
        self.canvas.bind("<Up>", self.wrk.up_ar)
        self.canvas.bind("<Right>", self.wrk.right_ar)
        self.canvas.bind("<Down>", self.wrk.down_ar)
        # События для обработки положения курсора
        self.canvas.bind("<Leave>", self.wrk.leave_canvas)
        self.canvas.bind("<Enter>", self.wrk.enter_canvas)
        # События для перемещения СК мышкой
        self.canvas.bind("<Button-3>", self.wrk.mouse_move_coords_sys_click)
        self.canvas.bind("<B3-Motion>", self.wrk.mouse_move_coords_sys_move)
        self.wrk.coord()

    def menu_1(self):
        '''
        Create input menu

        :returns: None
        '''
        file_menu1 = Menu(self.main_menu, tearoff=0)
        file_menu1.add_command(
            label="Клавиатура", command=lambda: self.wrk.keyboard("input")
        )
        file_menu1.add_command(label="Мышь",
                               command=lambda: self.wrk.mouse("input"))
        file_menu1.add_command(label="Файл",
                               command=lambda: self.wrk.file("input"))
        file_menu1.add_command(label="Random",
                               command=lambda: self.wrk.random("input"))
        self.main_menu.add_cascade(label="Ввод", menu=file_menu1)

    def menu_2(self):
        '''
        Create output menu

        :returns: None
        '''
        file_menu2 = Menu(self.main_menu, tearoff=0)
        file_menu2.add_command(label="Файл", command=self.wrk.output_file)
        file_menu2.add_command(label="Экран", command=self.wrk.output_screen)
        self.main_menu.add_cascade(label="Вывод", menu=file_menu2)

    def menu_3(self):
        '''
        Create editing menu

        :returns: None
        '''
        file_menu3 = Menu(self.main_menu, tearoff=0)
        file_menu3.add_command(
            label="Очистить экран",
            command=self.wrk.clear_all)
        file_menu3.add_command(
            label="Редактировать точку",
            command=self.wrk.editing)
        vst_menu = Menu(file_menu3, tearoff=0)
        vst_menu.add_command(
            label="Клавиатура", command=lambda: self.wrk.keyboard("insert")
        )
        vst_menu.add_command(label="Мышь",
                             command=lambda: self.wrk.mouse("insert"))
        vst_menu.add_command(label="Файл",
                             command=lambda: self.wrk.file("insert"))
        vst_menu.add_command(label="Random",
                             command=lambda: self.wrk.random("insert"))
        file_menu3.add_cascade(label="Вставить", menu=vst_menu)
        self.main_menu.add_cascade(label="Редактирование", menu=file_menu3)

    def menu_4(self):
        '''
        Create solution menu

        :returns: None
        '''
        file_menu4 = Menu(self.main_menu, tearoff=0)
        file_menu4.add_command(
            label="Решение",
            command=self.wrk.solution_of_task)
        file_menu4.add_command(
            label="Решение с выпуклой оболочкой",
            command=self.wrk.solution_2_of_task
        )
        self.main_menu.add_cascade(label="Решение", menu=file_menu4)

    def menu_5(self):
        '''
        Create help menu

        :returns: None
        '''
        help_menu = Menu(self.main_menu, tearoff=0)
        help_menu.add_command(label="Задача", command=self.wrk.task)
        help_menu.add_command(label="Об авторе", command=self.wrk.author)
        help_menu.add_command(
            label="Перемещение по плоскости",
            command=self.wrk.moving)
        self.main_menu.add_cascade(label="Справка", menu=help_menu)

    def menu_6(self):
        '''
        Create settings menu

        :returns: None
        '''
        set_menu = Menu(self.main_menu, tearoff=0)
        set_menu.add_command(
            label="Цвет фона",
            command=self.wrk.start_change_bg_color)
        self.main_menu.add_cascade(label="Настройки", menu=set_menu)
