from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I walk")


class Snake(Animal):
    def move(self):
        print("I crawl")


def main():
    a = Human()
    b = Snake()
    a.move()
    b.move()


if __name__ == '__main__':
    main()
