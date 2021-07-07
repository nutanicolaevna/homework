# Задание 1
# import time
#
# class TrafficLight:
#     __color = 'Красный'
#     def running(self):
#         self.__color = 'Красный'
#         print(f'Горит - {self.__color}')
#         time.sleep(7)
#
#         self.__color = 'Желтый'
#         print(f'Горит - {self.__color}')
#         time.sleep(2)
#
#         self.__color = 'Зеленый'
#         print(f'Горит - {self.__color}')
#         time.sleep(6)
#
#
# example = TrafficLight()
# print(example.running())

# Задание 2
# class Road:
#     def __init__ (self, length, width):
#         self._length = length
#         self._width = width
#         res = self._length * self._width * 25 * 0.05
#         print(f'Масса асфальта = {res}')
# per = Road(5000, 50)
#
# Задание 3
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.possition = position
#         self.wage = wage
#         self.bonus = bonus
#
#
# class Position(Worker):
#
#
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def get_total_incom(self):
#         self._incom = {'Wage': self.wage, 'Bonus': self.bonus}
#         return self._incom['Wage'] + self._incom['Bonus']
#
# person = Position('Анна', 'Харькова', 'менеджер', 20000, 40000)
# print(person.get_full_name())
# print(person.get_total_incom())

# # Задание 4
# class Car:
#
#     def __init__(self, name, speed, color, is_police=False):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
#
#     def go(self):
#         return f'Машина {self.name} поехала'
#     def stop(self):
#         return f'Машина  {self.name} остановилась'
#     def turn(self, direction):
#         return f'Машина {self.name} повернула {direction}'
#     def show_speed(self):
#         return f'Скорость автомобиля {self.name} = {self.speed} км\час'
#
# class PoliseCar(Car):
#     pass
#
# class SportCar(Car):
#     pass
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed >= 40:
#             return f'Превышена допустимая скорость'
#         else:
#             return f'Скорость автомобиля {self.name} = {self.speed} км\час'
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed >= 60:
#             return f'Превышена допустимая скорость'
#         else:
#             return f'Скорость автомобиля {self.name} = {self.speed} км\час'
#
# car1 = PoliseCar('Honda', 45, 'Черный', True)
# print(f'Марка машины: {car1.name}, Cкорость машины: {car1.speed}, Цвет машины: {car1.color}, Машина является полицейской? {car1.is_police}')
# print(car1.go())
# print(car1.turn('налево'))
# print(car1.show_speed())
# print(car1.stop())
#
# car2 = SportCar('Audi', 70, 'Красный', False)
# print(f'Марка машины: {car2.name}, Cкорость машины: {car2.speed}, Цвет машины: {car2.color}, Машина является полицейской? {car2.is_police}')
# print(car2.go())
# print(car2.turn('направо'))
# print(car2.show_speed())
# print(car2.stop())
#
# car3 = WorkCar('Lada', 40, 'Синий', False)
# print(f'Марка машины: {car3.name}, Cкорость машины: {car3.speed}, Цвет машины: {car3.color}, Машина является полицейской? {car3.is_police}')
# print(car3.go())
# print(car3.turn('направо'))
# print(car3.show_speed())
# print(car3.stop())
#
# car4 = TownCar('BMW', 120, 'Серый', False)
# print(f'Марка машины: {car4.name}, Cкорость машины: {car4.speed}, Цвет машины: {car4.color}, Машина является полицейской? {car4.is_police}')
# print(car4.go())
# print(car4.turn('направо'))
# print(car4.show_speed())
# print(car4.stop())

# Задача 5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'
class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки с помощью {self.title}'

class Pen(Stationery):
    def draw(self):
        return f'Для отрисовки воспользоваться инструментом {self.title}'
class Handle(Stationery):
    def draw(self):
        return f'Для отрисовки необходимо воспользоваться {self.title}'

exampl1 = Pen('Ручкой')
print(exampl1.draw())

exampl2 = Pencil('Карандаш')
print(exampl2.draw())

exampl3 = Handle('Маркер')
print(exampl3.draw())
