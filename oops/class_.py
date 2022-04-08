class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name}  {self.last_name} {self.age}'


class Employee(Person):
    def __init__(self, first_name, last_name, age, emp_no):
        super().__init__(first_name, last_name, age)
        self.emp_no = emp_no

    def __str__(self):
        return super().__str__() + f'  {self.emp_no}'


def main():
    x = Person('Sudhir', 'Shekhawat', 31)
    print(x)
    x1 = Employee("tTTT", 'SSS', 32, 345)
    print(x1)


if __name__ == '__main__':
    main()
# a = 5
# print(type(a))
# print(a.__doc__)

# class Point:
#     """This is point class created by sudhir"""
#     pass
#
#
# p1 = Point()
# print(p1.__doc__)
