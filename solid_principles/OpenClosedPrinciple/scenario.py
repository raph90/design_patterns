from solid_principles.OpenClosedPrinciple.good_example import (
    AndSpecification,
    BetterFilter,
    ColorSpecification,
    SizeSpecification,
)
from solid_principles.OpenClosedPrinciple.bad_example import ProductFilter
from solid_principles.OpenClosedPrinciple.base import Color, Product, Size


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.RED, Size.LARGE)

products = [apple, tree, house]

# Old Approach
pf = ProductFilter()
print("Green products (old):")
for p in pf.filter_by_color(products, Color.GREEN):
    print(f" - {p.name} is green")


bf = BetterFilter()
print("Green products (new): ")
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f" - {p.name} is green")

print("Large products: ")
large = SizeSpecification(Size.LARGE)

for p in bf.filter(products, large):
    print(f" - {p.name} is large")

large_red = AndSpecification(large, ColorSpecification(Color.RED))
print("Large and red products: ")

for p in bf.filter(products, large_red):
    print(f" - {p.name} is large and red")
