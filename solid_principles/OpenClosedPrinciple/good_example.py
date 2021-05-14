# The idea is that we extend these classes. We inherit and extend


# Base Class
class Specification:
    def is_satisfied(self, item):
        pass


# Base Class
class Filter:
    def filter(self, items, specification):
        pass


# Specifications
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    # here is satisfied just checks if the item color
    # is the same as the one in the specification
    def is_satisfied(self, item):
        return item.color == self.color

        # The specification determines the behaviour


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    # here is satisfied just checks if the item color
    # is the same as the one in the specification
    def is_satisfied(self, item):
        return item.size == self.size


# This filter is just one way of filtering based on the specification
# We could have multiple other ways of filtering
class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


class AndSpecification(Specification):
    def __init__(self, *args):
        # variable number of args
        self.args = args

    def is_satisfied(self, item):
        # we go through each of the args, each of which is a specification, and we check that
        # the item conforms to all of them

        # all here will return True if all of the values are true, otherwise false
        return all(map(lambda spec: spec.is_satisfied(item), self.args))