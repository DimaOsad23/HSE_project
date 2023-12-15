from math import *  # Импорт математического модуля


# Создаётся класс с решением задачи
class Solution:

    # Создание переменных класса
    def __init__(self):
        self.space = 0  # Переменная, хранящая максимальную "площадь"
        self.answer = []  # Переменная хранящая, последовательность точек, которая соответствует максимальной "площади"

    # Метод запускающий всё решение (решение задачи)
    def main(self, coords):
        self.space = 0  # Задание начального значения площади (переменная, хранящая максимальную площадь)
        self.answer = []  # Переменная, хранящая вершины несамопересекающегося четырёхугольника с максимальной площадью
        # Перебор групп по 4 точки
        for p_1 in range(0, len(coords) - 3):
            for p_2 in range(p_1 + 1, len(coords) - 2):
                for p_3 in range(p_2 + 1, len(coords) - 1):
                    for p_4 in range(p_3 + 1, len(coords)):
                        # Проверка на то, что можно построить четырёхугольник (если нельзя, то группа отбрасывается)
                        if self.false_quadrilateral(coords[p_1], coords[p_2], coords[p_3], coords[p_4]):
                            continue
                        # Перебор возможных четырёхугольников с вершинами в данных 4 точках
                        # Сравнение их площади с максимальной
                        self.space_quadrilateral(coords[p_1], coords[p_2], coords[p_3], coords[p_4])
                        self.space_quadrilateral(coords[p_1], coords[p_3], coords[p_2], coords[p_4])
                        self.space_quadrilateral(coords[p_1], coords[p_4], coords[p_2], coords[p_3])

        return self.answer, self.space  # Передача ответа

    # Проверка на то, можно ли построить четырёхугольник по данным 4 точкам
    def false_quadrilateral(self, p_1, p_2, p_3, p_4):
        # Проверка, лежат ли 3 точчки на одной прямой с помощью определения косинуса между векторами
        if self.cos_vectors_square(self.vector(p_1, p_2), self.vector(p_1, p_3)) == 1:
            return True
        elif self.cos_vectors_square(self.vector(p_1, p_2), self.vector(p_1, p_4)) == 1:
            return True
        elif self.cos_vectors_square(self.vector(p_1, p_3), self.vector(p_1, p_4)) == 1:
            return True
        elif self.cos_vectors_square(self.vector(p_2, p_3), self.vector(p_2, p_4)) == 1:
            return True
        else:
            return False

    # Нахождение длины вектора в координатах
    def length_vector(self, p_1, p_2):
        return sqrt((p_1[0] - p_2[0]) ** 2 + (p_1[1] - p_2[1]) ** 2)

    # Определение координат вектора
    def vector(self, p_1, p_2):
        return [round(float(p_1[0] - p_2[0]), 1), round(float(p_1[1] - p_2[1]), 1)]

    # Нахаждение квадрата косинуса угла между векторами через скалярное произведение
    def cos_vectors_square(self, vector_1, vector_2):
        cosin = (vector_1[0] * vector_2[0] + vector_1[1] * vector_2[1]) ** 2 / (
                    (vector_1[1] ** 2 + vector_1[0] ** 2) * (vector_2[1] ** 2 + vector_2[0] ** 2))
        if cosin > 1:  # Эта проверка нужна из-за способа хранения вещественных чисел языком Python
            cosin = 1
        return cosin

    # Нахождение синуса угла между векторами
    def sin_vectors(self, vector_1, vector_2):
        return sqrt(1 - self.cos_vectors_square(vector_1, vector_2))

    # Сравнение площади данного четырёхугольника с максимальной площадью
    def space_quadrilateral(self, p_1, p_2, p_3, p_4):
        if self.length_vector(p_1, p_2) * self.length_vector(p_3, p_4) * self.sin_vectors(self.vector(p_1, p_2),
                                                                                          self.vector(p_3,
                                                                                                      p_4)) / 2 > \
                self.space:
            # Перезаписываетс максимальное значение площади
            self.space = self.length_vector(p_1, p_2) * self.length_vector(p_3, p_4) * self.sin_vectors(
                self.vector(p_1, p_2), self.vector(p_3, p_4)) / 2
            # Перезаписывается последовательность вершин четырёхугольника, который соответствует максимальной площади
            self.answer = [p_1, p_3, p_2, p_4]

