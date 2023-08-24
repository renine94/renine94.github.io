# DIP (의존성 역전 원칙)
# 고수준 모듈은 저수준 모듈에 의존해서는 안된다.

from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass

class Relationships(RelationshipBrowser):  # low-level module
    def __init__(self):
        self.relations = []  # 이것을 list가 아니라 dict 로 바꿀 수 있는가?


    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# 클라이언트쪽에서는 구체적인 구현에 의존하지 않는게 좋다.
class Research:  # high-level module
    # def __init__(self, relationships: Relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}.')


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()

relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)


