# DIP
from enum import Enum
from abc import abstractmethod


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


class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    """
    This is the right place for this.
    The client no longer cares about how the storage is implemented
    """

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# There is a big problem here
"""
I am accessing the internal storage method of relationships in a higher level module
This means that the higher level module is dependent on the implementation of the lower level module
"""


# BAD
# class Research:
#     def __init__(self, relationships):
#         relations = relationships.relations
#         for r in relations:
#             if r[0].name == "John" and r[1] == Relationship.PARENT:
#                 print(f"John has a child called {r[2].name}")


class Research:
    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)