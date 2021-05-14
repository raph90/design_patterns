# this violates the open closed principle, because we are modifying the class to add functionality.
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    # we could go on adding filters ad infinitum
    # This is BAD - we should not be modifying a class. Instead we should be
    # extending an idea
