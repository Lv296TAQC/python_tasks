class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        return "Rectangle({!r}, {!r})".format(self.side_a, self.side_b)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return "Circle({!r})".format(self.radius)

    @classmethod
    def circle_from_rectangle(cls, rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)


def demonstrate_class_method():
    rect = Rectangle(3, 4)
    circ1 = Circle(5)
    circ2 = Circle.circle_from_rectangle(rect)
    print(rect)
    print(circ1)
    print(circ2)


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance


def demonstrate_new_func():
    single1 = Singleton()
    single2 = Singleton()
    print(single1, single2, sep='\n')


class SomeClass:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == "closed" and self.password == "asdf":
            return "secret value"
        else:
            return object.__getattribute__(self, item)


def demonstrate_getattribute():
    sc1 = SomeClass()
    sc1.password = "asdf"  # try to comment this
    print(sc1.closed)


def is_instance(obj, cls):
    return is_subcls(cls, obj.__class__)


def is_subcls(base, kid):
    if base is kid:
        return True
    for inst in kid.__mro__:
        if inst == base:
            return True
    return False


def demonstrate_is_instance():
    print(is_instance(12, int))
    print(is_instance(True, bool))
    print(is_instance(True, int))
    print(is_instance(True, str))
    print(is_instance(object, type))
    print(is_instance(Singleton, type))
    print(is_instance(bool, type))
    print(is_instance(type, type))
    print()
    print(is_subcls(int, int))
    print(is_subcls(int, bool))
    print(is_subcls(int, str))
    print(is_subcls(int, object))
    print(is_subcls(object, int))
