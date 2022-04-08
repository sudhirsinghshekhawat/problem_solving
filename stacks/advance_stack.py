from stacks.stack import Stack


class AdvanceStack:

    def __init__(self) -> None:
        self.element_stack = Stack()
        self.min_stack = Stack()

    def push(self, data):
        self.element_stack.push(data)
        if (self.min_stack.is_empty()) or (self.min_stack.peek() >= data):
            self.min_stack.push(data)
        else:
            self.min_stack.push(self.min_stack.peek())

    def pop(self):
        self.min_stack.pop()
        return self.element_stack.pop()

    def get_minimum(self):
        return self.min_stack.peek()

    def is_empty(self):
        return self.element_stack.is_empty()


if __name__ == '__main__':
    advance_stack = AdvanceStack()
    advance_stack.push(12)
    advance_stack.push(10)
    advance_stack.push(9)

    print(f'minimum: {advance_stack.get_minimum()}')
    advance_stack.pop()
    print(f'minimum: {advance_stack.get_minimum()}')
    advance_stack.pop()
    print(f'minimum: {advance_stack.get_minimum()}')
