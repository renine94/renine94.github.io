# LSP 리스코프 치환 원칙
# https://blog.itcode.dev/posts/2021/08/15/liskov-subsitution-principle


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


# 정사각형
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected an area of {expected}, got {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)


# 사각형에서는 작동하지만, 정사각형 클래스(파생 클래스) 에서는 작동하지 않는다.
# 이것은 리스코프 원칙을 위반하는 것
