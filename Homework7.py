# Задача 1
# class Matrix:
#     def __init__(self, my_list):
#         self.my_list = my_list
#     def __str__(self):
#         return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.my_list]))
#
#     def __add__(self, other):
#         for i in range(len(self.my_list)):
#             for j in range(len(other.my_list[i])):
#                 self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
#         return Matrix.__str__(self)
#
#
#
#
# a = Matrix([[-1, 2, 3], [-2, 1, 9], [7, -4, 5]])
# b = Matrix([[-2, 4, 6], [3, 4, 6], [-2, -1, 0]])
# # print(a)
# #
# # print(b)
#
# print(a + b)

# Задача 2

# from abc import ABC, abstractmethod
# class MyAbstractClass(ABC):
#     def __init__(self, size, height):
#         self.size = size
#         self.height = height
#
#     @abstractmethod
#     def cloth_rate(self):
#         pass
#
# class Suit(MyAbstractClass):
#
#
#     def suit(self):
#         return f'Для пошива костюма нужно: {2 * self.height + 0.3}'
#     @property
#     def height(self):
#         return self.__height
#     @height.setter
#     def height(self, height):
#         if height >= 200:
#             self.__height = 200
#         elif height <= 120:
#             self.__height = 120
#         else:
#             self.__height = height
#
#
#     def cloth_rate(self):
#         return f'Расход ткани общий: {(2 * self.height + 0.3) + (self.size/6.5 + 0.5)}'
# class Coat(MyAbstractClass):
#
#
#     def coat(self):
#         return f'Для пошива пальто нужно: {self.size/6.5 + 0.5}'
#
#     @property
#     def size(self):
#         return self.__size
#
#     @size.setter
#     def size(self, size):
#         if size >= 54:
#             self.__size = 54
#         elif size <= 42:
#             self.__size = 42
#         else:
#             self.__size = size
#
#
#     def cloth_rate(self):
#         return f'Расход ткани общий: {(2 * self.height + 0.3) + (self.size/6.5 + 0.5)}'
#
# a = Suit(46, 180)
# b = Coat(50, 210)
#
# print(a.suit())
# print(b.coat())
# print(a.cloth_rate())
# print(b.cloth_rate())
#
#

# Задача 3
class Cell:
    def __init__(self, value: int):
        self.value = value
    def __str__(self):
        return f'value = {self.value}'
    def __add__(self, other):
        return f'Общая клетка равна: {self.value + other.value}'
    def __sub__(self, other):
        if self.value - other.value <= 0:
            return f'Операция невозможна. Результат должен быть больше 0'
        else:
            return f' Результат выяитания клеток: {self.value - other.value}'
    def __mul__(self, other):
        return f'Общая клетка равна: {self.value * other.value}'
    def __truediv__(self, other):
        return f'Результат деления клеток: {round(self.value / other.value)}'
    def make_order(self, cell):
        result = ''
        for i in range(int(self.value / cell)):
            result += '*' * cell + '\n'
        result += '*' * (self.value % cell) + '\n'
        return result
cell1 = Cell(11)
cell2 = Cell(10)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(4))
print(cell2.make_order(4))
