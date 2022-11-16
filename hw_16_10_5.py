# Создать класс SquareException. Добавить в конструктор класса SquareException собственное
# исключение NonPositiveDigitException, унаследованное от ValueError, которое будет срабатывать каждый раз,
# когда сторона квадрата меньше или равна 0.


class NonPositiveDigitException(ValueError):
    def __init__(self):
        super(NonPositiveDigitException, self).__init__()

class SquareException:
    def __init__(self, side):
        if side < 1:
            raise NonPositiveDigitException
        self.side = side

