from tkinter import *  # Импорт модуля для интерфейса
from tkinter.messagebox import *  # Импорт  диалоговых окон
from tkinter.filedialog import *  # Импорт модуля для работы с файлами
from random import *  # Импорт рандома
from solution import *  # Импорт решения 
from solution_2 import *
from convex_hull import *


# Создание класса, который содержит методы функциональной части
class Work:

    # Создание переменных класса (блок получился довольно большой)
    def __init__(self, root, pn_control, pn_graph, canvas):
        self.coords = [] # Созданние переменной, хранящей координаты множества точек
        self.root = root  # Главное окно
        self.pn_control = pn_control  # Панель для кнопок
        self.pn_graph = pn_graph  # Панель для системы координат
        self.canvas = canvas  # Холст для системы координат
        # Создаётся переменная, хранящая количество клеток до правого края холста, если считать от его центра
        # (с учётом знака направления). Используется при изменении масштаба
        self.xmax = 10
        # Создаётся переменная, хранящая количество клеток до левого края холста, если считать от его центра
        # (с учётом знака направления). Используется при изменении масштаба
        self.xmin = -10
        # Создаётся переменная, хранящая количество клеток до верхнего края холста, если считать от его центра
        # (с учётом знака направления). Используется при изменении масштаба
        self.ymax = 10
        # Создаётся переменная, хранящая количество клеток до нижнего края холста, если считать от его центра
        # (с учётом знака направления). Используется при изменении масштаба
        self.ymin = -10
        # Создаётся переменная, по значению которой будет определятся состояне холста при перерисовке системы координат
        # 0 - нарисована только система координат
        # 1 - выведены точки
        # 2 - выведено решение
        self.special_arg = 0
        # Создание переменной, которая нужна для вывода координат курсора на холсте
        self.x_y = StringVar()
        self.x_y.set("({}; {})".format(0, 0))  # Задание изначального значения переменной
        # Создание лейбла с координатами курсора
        self.coord_x_y = Label(self.canvas, textvariable=self.x_y, bg="white", fg="black", font=("bold", 10))
        self.delta_x = 0  # Переменная, хранящая сдвиг в клетках относительно центра холста по оси Х
        self.delta_y = 0  # Переменная, хранящая сдвиг в клетках относительно центра холста по оси У
        self.solution = Solution()  # Создание объекта класса с решением задачи
        self.answer = []  # Переменная, в которой будет хранится часть ответа (координаты вершин четырёхугольника)
        self.red_point = []  # Переменная, хранящая координаты редактируемой точки
        self.space = 0  # Переменная, в которой будет хранится часть ответа (площадь четырёхугольника)
        # Создаются переменные, участвующие в перемещение по системе координат с помощью мыши
        self.but3_coords_x = 0  # Начальные координаты мыши по оси Х (относительно холста)
        self.but3_coords_y = 0  # Начальные координаты мыши по оси У (относительно холста)
        self.delta_mouse_x = 0  # Изменение координат по оси Х при перемещением мышкой
        self.delta_mouse_y = 0  # Изменение координат по оси У при перемещением мышкой
        self.bg_color = 'gray94'  # Задаётся цвет фона программы

    # Вспомогательные методы
    # Методы, отвечающие за рисование системы координат
    def coord(self):
        summ = -self.xmin + self.xmax
        # Рисование сетки
        for i in range(1, summ):
            self.canvas.create_line(i * 640 / summ, 0, i * 640 / summ, 640, fill="light grey",
                                    width=1)
            self.canvas.create_line(0, i * 640 / summ, 640, i * 640 / summ, fill="light grey",
                                    width=1)
        # Передача аргументов для рисования и подписи осей
        if self.delta_x <= self.xmin:
            self.create_text_y(625)
        elif self.delta_x >= self.xmax:
            self.create_text_y(15)
        else:
            self.create_system_coord_y()
            self.create_text_y(640 / 2 + 15 - 640 * self.delta_x / (2*self.xmax))
        if self.delta_y <= self.ymin:
            self.create_text_x(10)
        elif self.delta_y >= self.ymax:
            self.create_text_x(630)
        else:
            self.create_system_coord_x()
            self.create_text_x(640 / 2 + 10 + 640 * self.delta_y / (2*self.ymax))

    # Подпись чисел на оси Х
    def create_text_x(self, coordinata):
        summ = -self.xmin + self.xmax
        for i in range(1, summ):
            if i - self.xmax + self.delta_x != 0:
                self.canvas.create_text(i * 640 / summ, coordinata,
                                        text=i - self.xmax + self.delta_x, fill='black')
            elif coordinata > 10:
                self.canvas.create_text(max(320 - self.delta_x * 640 / (self.xmax - self.xmin) + 7, 15),
                                        min(320 + self.delta_y * 640 / (self.ymax - self.ymin) + 7, 630),
                                        text=0, fill='black')

    # Подпись чисел на оси У
    def create_text_y(self, coordinata):
        summ = -self.ymin + self.ymax
        for i in range(1, summ):
            if -i - self.ymin + self.delta_y != 0:
                self.canvas.create_text(coordinata, i * 640 / summ,
                                        text=-i - self.ymin + self.delta_y, fill='black')
            else:
                self.canvas.create_text(max(320 - self.delta_x * 640 / (self.xmax - self.xmin) + 7, 15),
                                        min(320 + self.delta_y * 640 / (self.ymax - self.ymin) + 7, 630),
                                        text=0, fill='black')

    # Рисование оси Х
    def create_system_coord_x(self):
        summ = -self.xmin + self.xmax
        self.canvas.create_line(0, 320 + 320 * self.delta_y / self.ymax, 640,
                                320 + 320 * self.delta_y / self.ymax,
                                fill="black", width=2, arrow=LAST, arrowshape="5 10 5")
        self.canvas.create_text(632, 330 + 320 * self.delta_y / self.ymax, text='X', anchor=W, fill="black")

        for i in range(1, summ):
            self.canvas.create_line(i * 640 / summ, 320 + 640 * self.delta_y / (2 * self.ymax),
                                    i * 640 / summ, 320 + 5 + 640 * self.delta_y / (2 * self.ymax),
                                    fill="black", width=1)

    # Рисование оси У
    def create_system_coord_y(self):
        summ = -self.xmin + self.xmax
        self.canvas.create_line(320 - 320 * self.delta_x / self.xmax, 0,
                                320 - 320 * self.delta_x / self.xmax, 640, fill="black",
                                width=2, arrow=FIRST, arrowshape="5 10 5")
        self.canvas.create_text(330 - 320 * self.delta_x / self.xmax, 10, text='Y', anchor=W, fill="black")
        for i in range(1, summ):
            self.canvas.create_line(320 - 640 * self.delta_x / (2 * self.xmax), i * 640 / summ,
                                    320 + 5 - 640 * self.delta_x / (2 * self.xmax), i * 640 / summ,
                                    fill="black", width=1)

    # Метод, очищающий массив координат (удаляет все координаты точек)
    def clear_coords(self):
        while len(self.coords) != 0:
            self.coords.pop()

    # Метод выхода из программы
    def quit(self):
        res = askyesno('Exit', 'Do you want to kill this window?')
        if res:
            self.root.destroy()

    # Обработка события по перемещению мыши для подписи координат курсора
    def moving_mouse(self, event):
        self.change_cursor_label(event.x, event.y)

    # Размещение лейбла с координатами курсора
    def place_cursor_label(self, x, y):
        size_x, size_y = self.coord_x_y.winfo_width(), self.coord_x_y.winfo_height()
        if x + 80 <= 640 and y + size_y <= 640:
            self.coord_x_y.place(x=x + 5, y=y + 5)
        elif x + 80 <= 640 and y + size_y >= 640:
            self.coord_x_y.place(x=x + 5, y=y - size_y - 5)
        elif x + 80 >= 640 and y + size_y <= 640:
            self.coord_x_y.place(x=x - size_x - 5, y=y + 5)
        else:
            self.coord_x_y.place(x=x - size_x - 5, y=y - size_y - 5)

    # Обаботка события по выходу курсора с холста
    def leave_canvas(self, event):
        self.coord_x_y.place_forget()  # Убираем лейбл с координатами
        self.canvas.unbind('<B3-Motion>')

    # Обработка события по вхождению на холст
    def enter_canvas(self, event):
        # Метод для движения по системе координат при помощи мыши
        self.canvas.bind('<B3-Motion>', self.mouse_move_coords_sys_move)
        self.canvas.bind('<Button-1>', lambda event: self.canvas.focus_set())  # Метод, устанавливающий фокус на холст

    # Считывание начального положения мыши при перемещении с помощью мыши
    def mouse_move_coords_sys_click(self, event):
        self.but3_coords_x = event.x
        self.but3_coords_y = event.y

    # Обработка события по перемещению при помощи мыши, вычисляется изменение координат
    def mouse_move_coords_sys_move(self, event):
        self.delta_mouse_x = self.delta_mouse_x + (self.but3_coords_x - event.x) / 640 * (self.xmax - self.xmin)
        self.delta_mouse_y = self.delta_mouse_y + (self.but3_coords_y - event.y) / 640 * (self.ymax - self.ymin)
        self.but3_coords_x = event.x  # Перезаписывается изначальное положение мыши по оси Х (относительно холста)
        self.but3_coords_y = event.y  # Перезаписывается изначальное положение мыши по оси У (относительно холста)
        self.change_delta_mouse_coords()
        x = round((self.but3_coords_x - 320) * self.xmax / 320 + self.delta_x, 1)
        y = round((320 - self.but3_coords_y) * self.ymax / 320 + self.delta_y, 1)
        self.x_y.set("({}; {})".format(x, y))
        self.place_cursor_label(self.but3_coords_x, self.but3_coords_y)
        self.draw_coords_mode()

    # Изменение координат, отвечающих за рисование осей, при перемещении с помощью мышки
    def change_delta_mouse_coords(self):
        if self.delta_mouse_x >= 1 and self.delta_x != 100 - self.xmax:
            self.delta_x += 1
            self.delta_mouse_x -= 1
        elif self.delta_mouse_x <= -1 and self.delta_x != -100 - self.xmin:
            self.delta_x -= 1
            self.delta_mouse_x += 1
        if self.delta_mouse_y >= 1 and self.delta_y != -100 - self.ymin:
            self.delta_y -= 1
            self.delta_mouse_y -= 1
        elif self.delta_mouse_y <= -1 and self.delta_y != 100 - self.ymax:
            self.delta_y += 1
            self.delta_mouse_y += 1

    # Метод для рисования системы координат в определённом состоянии
    # 0 - нарисована только система координат
    # 1 - выведены точки
    # 2 - выведено решение
    def draw_coords_mode(self):
        self.clear_c()
        if self.special_arg == 1:
            self.draw_points()
            if len(self.red_point) != 0:
                self.canvas.create_oval(320 + 320 / self.xmax * (float(self.red_point[0]) - self.delta_x) - 3,
                                        320 - 320 / self.ymax * (float(self.red_point[1]) - self.delta_y) - 3,
                                        320 + 320 / self.xmax * (float(self.red_point[0]) - self.delta_x) + 3,
                                        320 - 320 / self.ymax * (float(self.red_point[1]) - self.delta_y) + 3, outline='red',
                                        fill='red', width=1)
        elif self.special_arg == 2:
            self.draw_points()
            self.draw_solution(self.answer)

    # Блок событий для перемещения при помощи стрелок клавиатуры
    def left_ar(self, event):
        if self.delta_x != -100 - self.xmin:
            self.x_y.set("({}; {})".format(round(float(self.x_y.get().split()[0][1:-1]) - 1, 1),
                                           round(float(self.x_y.get().split()[1][0:-1]), 1)))
        self.delta_x = max(self.delta_x - 1, -100 - self.xmin)
        self.draw_coords_mode()

    def right_ar(self, event):
        if self.delta_x != 100 - self.xmax:
            self.x_y.set("({}; {})".format(round(float(self.x_y.get().split()[0][1:-1]) + 1, 1),
                                           round(float(self.x_y.get().split()[1][0:-1]), 1)))
        self.delta_x = min(100 - self.xmax, self.delta_x + 1)
        self.draw_coords_mode()

    def down_ar(self, event):
        if self.delta_y != -100 - self.ymin:
            self.x_y.set("({}; {})".format(round(float(self.x_y.get().split()[0][1:-1]), 1),
                                           round(float(self.x_y.get().split()[1][0:-1]) - 1, 1)))
        self.delta_y = max(-100 - self.ymin, self.delta_y - 1)
        self.draw_coords_mode()

    def up_ar(self, event):
        if self.delta_y != 100 - self.ymax:
            self.x_y.set("({}; {})".format(round(float(self.x_y.get().split()[0][1:-1]), 1),
                                           round(float(self.x_y.get().split()[1][0:-1]) + 1, 1)))
        self.delta_y = min(100 - self.ymax, self.delta_y + 1)
        self.draw_coords_mode()

    # Изменение масштаба колёсиком мыши
    def mouse_wheel(self, event):
        if event.delta == -120:
            self.xmax = min(self.xmax + 1, 15)
            self.xmin = max(self.xmin - 1, -15)
            self.ymax = min(self.ymax + 1, 15)
            self.ymin = max(self.ymin - 1, -15)
        if event.delta == 120:
            self.xmax = max(self.xmax - 1, 5)
            self.xmin = min(self.xmin + 1, -5)
            self.ymax = max(self.ymax - 1, 5)
            self.ymin = min(self.ymin + 1, -5)
        if self.delta_y >= 100 - self.ymax:
            self.delta_y = 100 - self.ymax
        elif self.delta_y <= -100 - self.ymin:
            self.delta_y = -100 - self.ymin
        if self.delta_x >= 100 - self.xmax:
            self.delta_x = 100 - self.xmax
        elif self.delta_x <= -100 - self.xmin:
            self.delta_x = -100 - self.xmin
        self.change_cursor_label(event.x, event.y)
        self.draw_coords_mode()

    # Изменения лейбла координат (точнее координат в лейбле) при изменеии масштаба
    def change_cursor_label(self, now_x, now_y):
        x = round((now_x - 320) * self.xmax / 320 + self.delta_x, 1)
        y = round((320 - now_y) * self.ymax / 320 + self.delta_y, 1)
        self.x_y.set("({}; {})".format(x, y))
        self.place_cursor_label(now_x, now_y)

    # Блок изменеия цвета фона программы (размещение цветных кнопок для выбора цвета фона)
    def start_change_bg_color(self):
        self.clear_all()
        lab = Label(self.pn_control, text='Выберете цвет фона', font='TimesNewRoman 14', bg=self.bg_color)
        lab.place(width=480, x=0, height=40)
        but_blue = Button(self.pn_control, bg='blue', activebackground='blue', command=lambda: self.change_bg_color('cornflower blue'))
        but_green = Button(self.pn_control, bg='green', activebackground='green', command=lambda: self.change_bg_color('light green'))
        but_yellow = Button(self.pn_control, bg='yellow', activebackground='yellow', command=lambda: self.change_bg_color('light goldenrod'))
        but_grey = Button(self.pn_control, bg='grey', activebackground='grey', command=lambda: self.change_bg_color('gray94'))
        but_blue.place(width=40, x=100, height=40, y=40)
        but_green.place(width=40, x=180, height=40, y=40)
        but_yellow.place(width=40, x=260, height=40, y=40)
        but_grey.place(width=40, x=340, height=40, y=40)

    # Изменение цвета фона
    def change_bg_color(self, bg_color):
        self.pn_control.config(bg=bg_color)
        self.bg_color = bg_color
        self.start_change_bg_color()

    # Вывод точек на систему координат
    def draw_points(self):
        for j in self.coords:
            self.canvas.create_oval(320 + 320 / self.xmax * (float(j[0]) - self.delta_x),
                                    320 - 320 / self.ymax * (float(j[1]) - self.delta_y),
                                    320 + 320 / self.xmax * (float(j[0]) - self.delta_x),
                                    320 - 320 / self.ymax * (float(j[1]) - self.delta_y), width=3)

    # Ввод и вставка через random
    # Режим определяет переменная mode
    # Input - ввод
    # Insert - вставка
    # Определение режима и проверка
    def random(self, mode):
        self.clear_all()
        if mode == 'input':
            self.random_range(mode)
        else:
            if len(self.coords) == 25:
                showinfo('Информация', 'Нельзя добавить точки, так как уже введено максимально допустимое количество.')
            else:
                self.random_range(mode)

    # Ввод диапазонов значений
    def random_range(self, mode):
        txt_range_x = StringVar()
        txt_range_y = StringVar()
        lab_range_x = Label(self.pn_control, text='Введите диапазон значений x', font='TimesNewRoman 10',
                            bg=self.bg_color)
        lab_range_y = Label(self.pn_control, text='Введите диапазон значений y', font='TimesNewRoman 10',
                            bg=self.bg_color)
        ent_range_x = Entry(self.pn_control, textvariable=txt_range_x)
        ent_range_y = Entry(self.pn_control, textvariable=txt_range_y)
        lab_range_x.place(width=180, x=30, height=20, y=20)
        lab_range_y.place(width=180, x=30, height=20, y=50)
        ent_range_x.place(width=60, x=230, height=20, y=20)
        ent_range_y.place(width=60, x=230, height=20, y=50)
        ent_range_x.focus()
        but_range = Button(self.pn_control, text='Задать диапазон', font='TimesNewRoman 12',
                           command=lambda: self.quantity_rand_point([txt_range_x.get(), txt_range_y.get()], mode))
        but_range.place(width=140, x=170, height=40, y=90)

    # Ввод количества задаваемых точек
    def quantity_rand_point(self, range_points, mode):
        try:
            range_random = [round(float(range_points[0].split()[0]), 1), round(float(range_points[0].split()[1]), 1),
                            round(float(range_points[1].split()[0]), 1),
                            round(float(range_points[1].split()[1]), 1)]
            if range_random[1] <= range_random[0] or range_random[3] <= range_random[2] or range_random[0] <= -100 or \
                    range_random[2] <= -100 or range_random[1] > 100 or range_random[3] > 100 or \
                    len(range_points[0].split()) > 2 or len(range_points[1].split()) > 2:
                return 1 / 0
            self.clear_pn_control()
            txt = StringVar()
            lab = Label(self.pn_control, text='Введите количество точек', font='TimesNewRoman 12', bg=self.bg_color)
            ent = Entry(self.pn_control, textvariable=txt)
            lab.place(width=480, x=0, height=20, y=20)
            ent.place(width=80, x=200, height=20, y=60)
            ent.focus()
            but_range = Button(self.pn_control, text='Задать количество', font='TimesNewRoman 12',
                               command=lambda: self.add_random(txt, range_random, mode))
            but_range.place(width=160, x=160, height=40, y=100)
        except:
            showerror('Неверный формат',
                      '''Неверный формат. Проверьте, что диапозоны аргументов имеют вид \'a b\', причём a < b; a > -100; b <=100.''')

    # Ввод (добавление) точек
    def add_random(self, txt, range_random, mode):
        try:
            quantity_points = int(txt.get())
            if (range_random[1] - range_random[0]) * (range_random[3] - range_random[2]) * 100 \
                    < quantity_points:  # Надо домножить на 100 л ч
                showerror('Проблема', 'Нельзя задать такое количество точек в данном диапазоне.')
            elif quantity_points <= 0:
                showerror('Неверный формат', 'Количество точек должно быть больше 0.')
            elif len(self.coords) + quantity_points > 25 and mode == 'insert':
                showerror('Проблема', 'Вы задаёте слишком много точек. Точек должно быть не больше 25.')
            elif quantity_points > 25:
                showerror('Проблема', 'Вы задаёте слишком много точек. Точек должно быть не больше 25.')
            else:
                if mode == 'input':
                    self.clear_coords()
                k = 0
                while k != quantity_points:
                    num = [round(uniform(range_random[0], range_random[1]), 1),
                           round(uniform(range_random[2], range_random[3]), 1)]
                    if num[0] == range_random[1]:
                        num[0] -= 0.1
                    if num[1] == range_random[3]:
                        num[1] -= 0.1
                    if not (num in self.coords):
                        k += 1
                        self.coords.append(num)
                self.clear_pn_control()
                showinfo('Информация', 'Координаты введены')
        except:
            showerror('Неверный формат', 'Неверный формат. Проверьте, что количество точек указано правильно.')

    # Ввод и вставка при помощи клавиатуры
    # Режим определяет переменная mode
    # Input - ввод
    # Insert - вставка
    # Определение режима и проверка
    def keyboard(self, mode):
        self.clear_all()
        self.special_arg = 1
        if mode == 'input':
            self.clear_coords()
            self.keyboard_add()
        else:
            if len(self.coords) == 25:
                showinfo('Информация', 'Нельзя добавить точки, так как уже введено максимально допустимое количество.')
            else:
                self.draw_points()
                self.keyboard_add()

    # Ввод и добавление с клавиатуры
    def keyboard_add(self):
        txt_x = StringVar()
        txt_y = StringVar()
        lab_x = Label(self.pn_control, text='Введите значение x', font='TimesNewRoman 10', bg=self.bg_color)
        lab_y = Label(self.pn_control, text='Введите значение y', font='TimesNewRoman 10', bg=self.bg_color)
        ent_x = Entry(self.pn_control, textvariable=txt_x)
        ent_y = Entry(self.pn_control, textvariable=txt_y)
        lab_x.place(width=120, x=30, height=20, y=20)
        lab_y.place(width=120, x=30, height=20, y=50)
        ent_x.place(width=60, x=170, height=20, y=20)
        ent_y.place(width=60, x=170, height=20, y=50)
        ent_x.focus()
        but_add_point = Button(self.pn_control, text='Добавить точку', font='TimesNewRoman 12',
                               command=lambda: self.add_point(txt_x, txt_y, ent_x, ent_y))
        stop_add_but = Button(self.pn_control, text='Прекратить добавление', font='TimesNewRoman 12',
                              command=self.clear_all)
        but_add_point.place(width=200, x=140, height=40, y=90)
        stop_add_but.place(width=200, x=140, height=40, y=140)

    # Запись координат в массив
    def add_point(self, txt_x, txt_y, ent_x, ent_y):
        try:
            x_coord = round(float(txt_x.get()), 1)
            y_coord = round(float(txt_y.get()), 1)
            if [x_coord, y_coord] in self.coords:
                showinfo('Информация', 'Точка с такими координатами уже существует')
            elif abs(x_coord) >= 100 or abs(y_coord) >= 100:
                showerror('Неверные координаты', 'Введены некорректные координаты. Координаты точек должны лежать в диапазоне (-100, 100).')
            else:
                self.coords.append([x_coord, y_coord])
                self.canvas.create_oval(320 + 320 / self.xmax * x_coord, 320 - 320 / self.ymax * y_coord,
                                        320 + 320 / self.xmax * x_coord, 320 - 320 / self.ymax * y_coord, width=3)
            ent_x.delete(0, END)
            ent_y.delete(0, END)
            ent_x.focus()
            if len(self.coords) == 25:
                self.clear_all()
                showinfo('Ввод завершён', 'Ввод завершён, так как введёно максимально допустимое количество точек (25).'
                         )
        except:
            showerror('Неверный формат', 'Проверьте правильно ли введены координаты точек.')

    # Ввод и вставка при помощи мышки
    # Режим определяет переменная mode
    # Input - ввод
    # Insert - вставка
    # Определение режима и проверка
    def mouse(self, mode):
        self.clear_all()
        if mode == 'input':
            self.clear_coords()
            self.mouse_add()
        else:
            if len(self.coords) == 25:
                showinfo('Информация', 'Нельзя добавить точки, так как уже введено максимально допустимое количество.')
            else:
                self.draw_points()
                self.mouse_add()

    # Размещение виджетов при вводе и добавлении мышкой
    def mouse_add(self):
        self.special_arg = 1
        self.canvas.unbind('<Enter>')
        self.canvas.bind('<Enter>', lambda event: self.canvas.bind('<B3-Motion>', self.mouse_move_coords_sys_move))
        self.canvas.bind('<Button-1>', self.click)
        lab = Label(self.pn_control, text='Выберете точку мышкой', font='TimesNewRoman 14', bg=self.bg_color)
        lab.place(width=480, x=0, height=90, y=0)
        stop_add_but = Button(self.pn_control, text='Прекратить добавление', font='TimesNewRoman 12',
                              command=self.clear_all)
        stop_add_but.place(width=200, x=140, height=40, y=90)

    # Обработка нажатия при вводе и добавлении мышкой
    def click(self, event):
        # Перевод координат
        x_coord = round((event.x - 320) * self.xmax / 320, 1)
        y_coord = round((320 - event.y) * self.ymax / 320, 1)
        # Проверка и добавление
        if not ([round(x_coord + self.delta_x, 1), round(y_coord + self.delta_y, 1)] in self.coords) and abs(
                round(x_coord +self.delta_x, 1)) < 100 and abs(round(y_coord + self.delta_y, 1)) < 100:
            self.canvas.create_oval(320 + 320 / self.xmax * x_coord, 320 - 320 / self.ymax * y_coord,
                                    320 + 320 / self.xmax * x_coord, 320 - 320 / self.ymax * y_coord, width=3)
            self.coords.append([round(x_coord + self.delta_x, 1), round(y_coord + self.delta_y, 1)])
        if len(self.coords) == 25:
            self.clear_all()


    # Ввод и вставка через файл
    # Режим определяет переменная mode
    # Input - ввод
    # Insert - вставка
    # Определение режима и проверка
    def file(self, mode):
        self.clear_all()
        if mode == 'input':
            self.open_file(mode)
        else:
            if len(self.coords) == 25:
                showinfo('Информация', 'Нельзя добавить точки, так как уже введено максимально допустимое количество.')
            else:
                self.open_file(mode)

    # Открытие и  чтение файла с записью координат в массив
    def open_file(self, mode):
        try:
            filename = askopenfilename()
            f = open(filename, 'r')
            list_coords = []
            for coords in f.readlines():  # Создаём список координат без повторений и проверяем эти координаты
                if not [round(float(coords.split()[0]), 1), round(float(coords.split()[1]), 1)] in list_coords:
                    list_coords.append([round(float(coords.split()[0]), 1), round(float(coords.split()[1]), 1)])
                if abs(round(float(coords.split()[0]), 1)) >= 100 and abs(round(float(coords.split()[1]), 1)) >= 100:
                    return 1 / 0
            f.close()
            if len(self.coords) + len(list_coords) > 25 and mode == 'insert':
                showerror('Проблема', 'Превышено максимально допустимое количество точек (25).')
            else:
                if mode == 'input':
                    self.clear_coords()
                for coordy in list_coords:
                    if not coordy in self.coords:
                        self.coords.append(coordy)
                showinfo('Информация', 'Координаты введены')
        except FileNotFoundError:  # Если файл не выбран
            pass
        except ZeroDivisionError:
            showerror('Неверные координаты', 'Неверные координаты в файле. Координаты должны лежать в диапозоне (-100, 100).')
        except:
            showerror('Неверный формат', 'Проверьте правильный ли формат файла и координат в нём.')

    # Вывод координат на экран и проверка количества точек
    def output_screen(self):
        self.clear_all()
        if len(self.coords) == 0:
            showinfo('Информация', 'Нет точек')
        else:
            self.draw_points()   # Вывод точек в системе координат
            self.special_arg = 1
            self.coords_output()

    # Вывод координат текстом
    def coords_output(self):
        lab_coords = Label(self.pn_control, text='Координаты (x,y):', font='TimesNewRoman 12', bg=self.bg_color)
        lab_coords.place(width=160, x=320, height=20, y=0)
        output_frame = Frame(self.pn_control, bg=self.bg_color)
        output_frame.place(width=140, x=340, y=20)
        y_scroll = Scrollbar(output_frame, orient=VERTICAL)
        if len(self.coords) > 9:
            y_scroll.pack(side=RIGHT, fill=Y)
        box_coords = Listbox(output_frame, yscrollcommand=y_scroll.set, font='TimesNewRoman 12', bg=self.bg_color,
                             selectbackground=self.bg_color, selectforeground='black', highlightthickness=0,
                             relief=FLAT, selectmode=0,height=9)
        for coords in self.coords:
            box_coords.insert(END, "({}; {})".format(coords[0], coords[1]))

        box_coords.pack(side=LEFT, fill=BOTH)
        y_scroll.config(command=box_coords.yview)

    # Вывод координат в файл
    def output_file(self):
        try:
            # Выбор файла для записи
            f = asksaveasfile(filetypes=[('Text Document', '239yearpr/*.txt')]
                              , defaultextension=[('Text Document', '239yearpr/*.txt')])
            for coords in self.coords:
                f.write(str(coords[0]) + ' ' + str(coords[1]) + '\n')
            f.close()
        except:
            pass

    # Блок методов очистки
    # Очистка всех панелей (привод программы к изначальному состоянию)
    def clear_all(self):
        for wid in self.pn_control.winfo_children():
            wid.destroy()
        self.canvas.unbind('<Button-1>')
        self.canvas.delete('all')
        self.coord()
        self.special_arg = 0
        self.red_point = []
        self.canvas.focus_set()
        self.canvas.unbind('<Enter>')
        self.canvas.bind('<Enter>', self.enter_canvas)

    # Очистка панели кнопок
    def clear_pn_control(self):
        for wid in self.pn_control.winfo_children():
            wid.destroy()

    # Очистка системы координат
    def clear_c(self):
        self.canvas.delete('all')
        self.coord()

    # Редактирование
    # Запуск выбора точек и проверка
    def editing(self):
        self.clear_all()
        self.draw_points()
        # Меняется обработка событий, так как иначе будет два события на ЛКМ
        self.canvas.unbind('<Enter>')
        self.canvas.bind('<Enter>', lambda event: self.canvas.bind('<B3-Motion>', self.mouse_move_coords_sys_move))
        if len(self.coords) == 0:
            showerror('Ошибка редактирования', 'Нет точек для редактирования.')
        else:
            self.special_arg = 1
            lab = Label(self.pn_control, text='Выберете точку для редактирования', font='TimesNewRoman 14', bg=self.bg_color)
            lab.place(x=0, y=0, width=480, height=90)
            stop_but = Button(self.pn_control, text='Прекратить редактирование', font='TimesNewRoman 12',
                              command=self.clear_all)
            stop_but.place(y=90, x=120, width=240, height=40)
            self.canvas.bind('<Button-1>', self.edit_event)

    # Начало обработка события по выбору точки для редактирования
    def edit_event(self, event):
        x_coord = round((event.x - 320) * self.xmax / 320, 1)
        y_coord = round((320 - event.y) * self.ymax / 320, 1)
        if [round(x_coord + self.delta_x, 1), round(y_coord + self.delta_y, 1)] in self.coords:
            self.canvas.create_oval(320 + 320 / self.xmax * x_coord - 3, 320 - 320 / self.ymax * y_coord - 3,
                                    320 + 320 / self.xmax * x_coord + 3, 320 - 320 / self.ymax * y_coord + 3, outline='red',
                                    fill='red', width=1)
            self.red_point = [round(x_coord + self.delta_x, 1), round(y_coord + self.delta_y, 1)]
            self.canvas.unbind('<Button-1>')
            self.edit_but()

    # Создаются кнопки для выбора режима редактирования
    def edit_but(self):
        self.clear_pn_control()
        lab_info = Label(self.pn_control, text='Редактируемая точка', font='TimesNewRoman 12', bg=self.bg_color)
        lab_point = Label(self.pn_control, text='('+str(self.red_point[0])+' ,'+str(self.red_point[1])+')',
                          font='TimesNewRoman 12', bg=self.bg_color)
        lab_info.place(width=480, x=0, y=10, height=30)
        lab_point.place(width=480, x=0, y=50, height=30)
        del_but = Button(self.pn_control, text='Удалить', font='TimesNewRoman 12', command=self.del_point)
        del_but.place(width=140, x=170, height=40, y=90)
        change_but = Button(self.pn_control, text='Изменить', font='TimesNewRoman 12', command=self.change)
        change_but.place(width=140, x=170, height=40, y=140)
        cancel_but = Button(self.pn_control, text='Отмена', font='TimesNewRoman 12', command=self.cancel_point)
        cancel_but.place(width=140, x=170, height=40, y=190)

    # Удаление выбранной точки
    def del_point(self):
        self.coords.remove(self.red_point)
        self.red_point = []
        if len(self.coords) == 0:
            self.clear_all()
            showinfo('Завершение редактирования', 'Редактирование прекращено, так как недостаточно точек (нет точек).')
        else:
            self.editing()

    # Блок замены точки
    # Создание полей и кнопок для ввода новых координат точки
    def change(self):
        self.clear_pn_control()
        lab_info = Label(self.pn_control, text='Редактируемая точка', font='TimesNewRoman 12', bg=self.bg_color)
        lab_point = Label(self.pn_control, text='(' + str(self.red_point[0]) + ' ,' + str(self.red_point[1]) + ')',
                          font='TimesNewRoman 12', bg=self.bg_color)
        lab_info.place(width=480, x=0, y=10, height=30)
        lab_point.place(width=480, x=0, y=50, height=30)
        txt_x = StringVar()
        txt_y = StringVar()
        lab_x = Label(self.pn_control, text='Введите значение x', font='TimesNewRoman 10', bg=self.bg_color)
        lab_y = Label(self.pn_control, text='Введите значение y', font='TimesNewRoman 10', bg=self.bg_color)
        ent_x = Entry(self.pn_control, textvariable=txt_x)
        ent_y = Entry(self.pn_control, textvariable=txt_y)
        lab_x.place(width=120, x=30, height=20, y=100)
        lab_y.place(width=120, x=30, height=20, y=130)
        ent_x.place(width=60, x=170, height=20, y=100)
        ent_y.place(width=60, x=170, height=20, y=130)
        ent_x.focus()
        but_change_point = Button(self.pn_control, text='Заменить', font='TimesNewRoman 12',
                                  command=lambda: self.change_point(txt_x, txt_y, ent_x, ent_y))
        but_change_point.place(width=140, x=170, height=40, y=170)
        self.canvas.unbind('<Enter>')
        self.canvas.bind('<Enter>', self.enter_canvas)

    # Замена точки с проверками
    def change_point(self, txt_x, txt_y, ent_x, ent_y):
        try:
            x_coord = round(float(txt_x.get()), 1)
            y_coord = round(float(txt_y.get()), 1)
            if abs(x_coord) >= 100 or abs(y_coord) >= 100:
                return 1 / 0
            if not [x_coord, y_coord] in self.coords:
                self.coords[self.coords.index(self.red_point)] = [x_coord, y_coord]
                self.editing()
            else:
                showinfo('Информация', 'Тточка с такими кооррдинатами уже существует.')
                ent_x.delete(0, END)
                ent_y.delete(0, END)
                ent_x.focus()
        except:
            showerror('Неверный фоормат', 'Проверьте правильно ли введены координаты. \
            Значения координат должны лежать в диапозоне (-100, 100).')

    # Отмена выбора точки
    def cancel_point(self):
        self.red_point = []
        self.editing()

    # Блок информации (справки)
    # Вывод условия задачи
    def task(self):
        showinfo('Задача',
                 ''' На плоскости задано множество точек. Найти из них такие 4 точки, что построенный по ним 4-хугольник не является самопересекающимся и имеет при этом максимальную площадь.''')

    # Вывод имени и класса втора
    def author(self):
        showinfo('Автор', 'Осадчий Дмитрий Александрович, БИБ231')
        
    # Вывод информации про перемещение по плоскости
    def moving(self):
        showinfo('Перемещение', 'Перемещение по плоскости осуществляется при помощи стрелок клавиатуры или при помощи зажатой ПКМ')
    
    # Блок вывода решения
    # Запись координат вершин и площади четырёхугольника в переменные. Проверка на существования решения,
    # то есть на существование хотя бы одного четырёхугольника, который не самопересекается
    # Вызов решения обычным перебором
    def solution_of_task(self):
        self.answer, self.space = self.solution.main(self.coords)
        if len(self.answer) == 0:
            showerror('Проблема', 'Невозможно построить четырёхугольник по заданным точкам.')
        else:
            self.clear_all()
            self.draw_points()
            self.coords_output()
            self.draw_solution(self.answer)
    # Вызов решения перебором по выпуклой оболочке
    def solution_2_of_task(self):
        self.answer, self.space = self.solution.main(convex_hull(self.coords))
        if len(self.answer) == 0:
            showerror('Проблема', 'Невозможно построить четырёхугольник по заданным точкам.')
        else:
            self.clear_all()
            self.draw_points()
            self.coords_output()
            self.draw_solution(self.answer)



    # Рисование четырёхугольника в системе координат (вывод ответа графически)
    def draw_solution(self, solution):
        self.canvas.create_line(320 + 320 / self.xmax * (float(solution[0][0]) - self.delta_x),
                                320 - 320 / self.ymax * (float(solution[0][1]) - self.delta_y),
                                320 + 320 / self.xmax * (float(solution[1][0]) - self.delta_x),
                                320 - 320 / self.ymax * (float(solution[1][1]) - self.delta_y))
        self.canvas.create_line(320 + 320 / self.xmax * (float(solution[1][0]) - self.delta_x),
                                320 - 320 / self.ymax * (float(solution[1][1]) - self.delta_y),
                                320 + 320 / self.xmax * (float(solution[2][0]) - self.delta_x),
                                320 - 320 / self.ymax * (float(solution[2][1]) - self.delta_y))
        self.canvas.create_line(320 + 320 / self.xmax * (float(solution[2][0]) - self.delta_x),
                                320 - 320 / self.ymax * (float(solution[2][1]) - self.delta_y),
                                320 + 320 / self.xmax * (float(solution[3][0]) - self.delta_x),
                                320 - 320 / self.ymax * (float(solution[3][1]) - self.delta_y))
        self.canvas.create_line(320 + 320 / self.xmax * (float(solution[3][0]) - self.delta_x),
                                320 - 320 / self.ymax * (float(solution[3][1]) - self.delta_y),
                                320 + 320 / self.xmax * (float(solution[0][0]) - self.delta_x),
                                320 - 320 / self.ymax * (float(solution[0][1]) - self.delta_y))
        self.special_arg = 2
        self.write_answer()

    # Вывод вершин и площади четырёхугольника на панели кнопок текстом (вывод ответа текстом)
    def write_answer(self):
        text_answer = 'Ответ:'
        text_coords = 'Координаты вершин четырёхугольника:\n' + '(' + str(self.answer[0][0]) + ', ' + \
                      str(self.answer[0][1]) + ')\n' + '(' + str(self.answer[1][0]) + ', ' + str(
            self.answer[1][1]) + ')\n' + '(' + str(self.answer[2][0]) + ', ' + str(
            self.answer[2][1]) + ')\n' + '(' + str(self.answer[3][0]) + ', ' + str(self.answer[3][1]) + ')\n'

        lab_answer = Label(self.pn_control, text=text_answer, font='TimesNewRoman 14', bg=self.bg_color)
        lab_answer.place(width=480, x=0, height=20, y=215)
        lab_coords = Label(self.pn_control, text=text_coords, font='TimesNewRoman 12', bg=self.bg_color)
        lab_coords.place(width=480, x=0, height=105, y=250)
        lab_space = Label(self.pn_control, text='Площадь:\n'+str(round(self.space, 3)), font='TimesNewRoman 12',
                          bg=self.bg_color)
        lab_space.place(width=480, x=0, y=355)
