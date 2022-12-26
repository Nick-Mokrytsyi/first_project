"""
Реализовать класс цифрового счетчика. В классе реализовать методы:

начальной инициализации счётчика (предусмотреть установку счётчика значениями по умолчанию 0-100) (метод __init__())
увеличения счетчика на 1 (метод increase())
возвращения текущего значения счётчика (метод get_current_value())
"""


class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        self.__start = start  # Protected
        self.__end = end  # Protected
        self.current = current
        if self.current is None:
            self.current = self.__start

    def increase(self):

        if self.__start <= self.current < self.__end:
            self.current += 1
        else:
            raise ValueError("Out of range")

    def get_current_value(self):
        if self.current < 0:
            raise ValueError("Work with Positive Numbers Only")
        else:
            return self.current


a = DigitalCounter()
print(a.get_current_value())
a.increase()
print(a.get_current_value())
# a.increase()
# a.increase()
# a.increase()
# a.increase()
# a.increase()
# a.increase()
# a.increase()
# a.increase()
# a.increase()
# print(a.get_current_value())
# a.current = 95
# print(a.get_current_value())
# a.increase()
# print(a.get_current_value())
# a.increase()
# print(a.get_current_value())
# a.increase()
# a.increase()
# print(a.get_current_value())
# a.increase()
# print(a.get_current_value())
# a.increase()
# print(a.get_current_value())
