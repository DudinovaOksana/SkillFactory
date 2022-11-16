# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода init().
# На выходе в консоли вам необходимо получить площадь данной фигуры.

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'

    def get_square(self):
        return self.width * self.height

rectangle = Rectangle(2,6,10,12)
print(rectangle)
print(rectangle.get_square())
