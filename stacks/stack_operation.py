from stacks.stack import Stack
from stacks.switch import switch


def sorting_stack(stack: Stack) -> Stack:
    sorted_stack = Stack()
    while not stack.is_empty():
        tmp = stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() >= tmp:
            stack.push(sorted_stack.pop())
        sorted_stack.push(tmp)
    return sorted_stack


def reverse_stack(stack: Stack) -> Stack:
    rstack = Stack()
    while not stack.is_empty():
        rstack.push(stack.pop())
    return rstack


def postfix_evaluation(string):
    operator_list = ['*', '-', '+', '/']
    operand_list = []
    if string:
        for ch in string:
            if ch in operator_list:
                var1 = int(operand_list.pop())
                var2 = int(operand_list.pop())
                result = switch(ch, var1, var2)
                operand_list.append(result)
            else:
                operand_list.append(ch)
    return operand_list


def check_balance_of_braces(string):
    list = []
    if string:
        for ch in string:
            if ch == ']':
                if list and list[-1] == '[':
                    list.pop()
                else:
                    return False
            if ch == '}':
                if list and list[-1] == '{':
                    list.pop()
                else:
                    return False
            if ch == ')':
                if list and list[-1] == '(':
                    list.pop()
                else:
                    return False
            if ch in ['(', '{', '[']:
                list.append(ch)
    return False if list else True


if __name__ == '__main__':
    string = '{{}}'
    print(check_balance_of_braces(string))
    string = ''
    print(check_balance_of_braces(string))
    string = ']'
    print(check_balance_of_braces(string))

    postfix_string = '123*+5-'
    result = postfix_evaluation(postfix_string)
    print(f'result = {result}')

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(f'original stack : {stack}')
    rstack = reverse_stack(stack)
    print(f'reverse stack = {rstack}')

    stack = Stack()
    stack.push(11)
    stack.push(2)
    stack.push(31)
    stack.push(4)

    print(f'original stack : {stack}')
    sorted_stack = sorting_stack(stack)
    print(f'sorted stack = {sorted_stack}')
