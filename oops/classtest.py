class ParentA:
    def how_to_talk(self):
        print("hello")


class ParentB:
    def how_to_talk(self):
        print("Namaste")


class Toddler(ParentA, ParentB):
    def how_to_walk(self):
        print("slowly")


class Car:
    wheel_count = 4


class Car1(object, metaclass=type):
    ...


if __name__ == '__main__':
    t1 = Toddler()
    t1.how_to_walk()
    t1.how_to_talk()
    my_car = Car()
    print(type(my_car))
    my_car1 = Car1()
    print(type(my_car1))
