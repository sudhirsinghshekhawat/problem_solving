from stacks.exceptions import StackException


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise StackException("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise StackException("Stack is empty")
        return self.items[-1]

    def __str__(self):
        return f'stack : {self.items}'


if __name__ == '__main__':
    stack = Stack()
    print(f'is stack is empty : {stack.is_empty()}')
    # stack.pop()
    # stack.peek()
    stack.push(1)
    print(stack)
    stack.push(2)
    print(stack)
    stack.push(3)
    print(stack)
    stack.push(4)
    print(stack)
    stack.push(5)
    print(stack)
    print(f'stack peek is : {stack.peek()}')
    stack.pop()
    stack.pop()
    print(stack)
