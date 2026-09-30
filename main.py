"""Demonstrate runtime polymorphism with the basic-shapes hierarchy."""

from circle import Circle
from rectangle import Rectangle
from square import Square


def main():
    c1 = Circle(0, 0, 4, "Circle A")
    c2 = Circle(2, -3, 1.5, "Circle B")
    r1 = Rectangle(10, 20, "Rectangle A")
    r2 = Rectangle(3, 7.5, "Rectangle B")
    sq = Square(5, "Square A")
    shapes = [c1, c2, r1, r2, sq]

    print("--- Polymorphic processing ---")
    for shape in shapes:
        print(f"{shape.name}: area = {shape.area:.2f}")

    print("\n--- Circle radius change ---")
    print(f"Before: radius={c1.radius}, area={c1.area:.2f}")
    c1.radius = 8
    print(f"After:  radius={c1.radius}, area={c1.area:.2f}")

    print("\n--- Rectangle length and width change ---")
    print(f"Before: {r1.length} x {r1.width}, area={r1.area:.2f}")
    r1.length = 12
    r1.width = 25
    print(f"After:  {r1.length} x {r1.width}, area={r1.area:.2f}")

    print("\n--- Square side change ---")
    print(f"Before: side={sq.side}, length={sq.length}, width={sq.width}, area={sq.area:.2f}")
    sq.side = 9
    print(f"After:  side={sq.side}, length={sq.length}, width={sq.width}, area={sq.area:.2f}")


if __name__ == "__main__":
    main()
