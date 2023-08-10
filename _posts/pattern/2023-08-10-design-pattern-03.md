---
layout: single

header:
  teaser: /assets/images/logo/pattern.jpeg
  overlay_image: /assets/images/logo/pattern.jpeg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[pattern] 디자인패턴(3) - 개방 폐쇄 원칙 (OCP)"
excerpt: "🚀 디자인패턴 & SOLID 원칙"

categories: pattern
tag: [pattern, design, solid, ocp]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---
# 01. OCP (Open Close Principal)

```python
"""
OCP 개방폐쇄원칙은 새로운 기능을 추가할 때 확장을 통해 추가하고, 수정을 통해서가 아니다.
"""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# OCP = open for extension, closed for modification
# 확장을 위해서는 열려 있지만, 수정을 위해서는 클래스를 닫아야 한다.


class ProductFilter:
    """요구사항이 추가됨에 따라 계속해서 함수가 생겨나는것은 OCP 원칙에 위배된다."""

    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product

    def filter_by_size(self, products, size):
        for product in products:
            if product.size == size:
                yield product

    def filter_by_size_and_color(self, products, size, color):
        for product in products:
            if product.color == color and product.size == size:
                yield product

    # 2 가지 옵션이 있다면 모든 경우의수 는 3 = 2C1 + 2C2
    # 3 가지 옵션이 있다면 모든 경우의수 는 7 = 3C1 + 3C2 + 3C3 (이름, 색상, 크기)
    # OCP 원칙은 새 필터를 추가할 때마다 필터함수를 추가하는 것이 아니라, 확장을 통해 추가한다는 것을 의미한다.


# Specification


class Specification:
    def is_satisfied(self, item):
        raise NotImplementedError

    def __and__(self, other):
        return AndSpecification(self, other)


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class Filter:
    def filter(self, items, spec):
        raise NotImplementedError


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print("Green products (old):")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green")

    print('--------------------------------')

    bf = BetterFilter()

    print("Green products (new):")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} is green")

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is Large")

    print("Large Blue products:")
    # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    large_blue = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is Large and Blue")


# OCP 개방 폐쇄 원칙은 기본적으로 코드를 계속 수정하는 상황을 피하고, 새롭게 만드는것.
```