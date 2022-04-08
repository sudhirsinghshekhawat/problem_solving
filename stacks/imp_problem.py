from collections import deque

from stacks.stack import Stack


def finding_spans(input_arr):
    list_span = []

    for i, val in enumerate(input_arr):
        span = 1
        j = i - 1
        while j >= 0 and input_arr[j] <= input_arr[i]:
            span = span + 1
            j = j - 1
        list_span.append(span)
    return list_span


def finding_span_using_stack(input_arr):
    list_span = []
    stack = Stack()
    p = 0

    for i, val in enumerate(input_arr):
        while not stack.is_empty() and input_arr[i] >= input_arr[stack.peek()]:
            stack.pop()
        if stack.is_empty():
            p = -1
        else:
            p = stack.peek()

        stack.push(i)
        list_span.append(i - p)
    return list_span


def finding_span_using_stack1(input_arr):
    list_span = []
    stack = deque()
    p = 0
    for i, val in enumerate(input_arr):
        while not stack and input_arr[i] >= input_arr[stack[-1]]:
            stack.pop()

        if not stack:
            p = -1
        else:
            p = stack[-1]
        stack.append(i)
        list_span.append(i - p)
    return list_span


def max_area(input_arr):
    stack = Stack()
    max_area = 0

    for i, val in enumerate(input_arr):
        if stack.is_empty() or input_arr[stack.peek()] <= input_arr[i]:
            stack.push(i)
        else:
            while not stack.is_empty():
                top = stack.pop()
                width = i if stack.is_empty() else (i - stack.peek() - 1)
                max_area = max(max_area, input_arr[top] * width)
            stack.push(i)

    while not stack.is_empty():
        top = stack.pop()
        width = i if stack.is_empty() else (i - stack.peek() - 1)
        max_area = max(max_area, (input_arr[top] * width))

    return max_area


def max_area1(input_arr):
    stack = list()
    max_area = 0
    index = 0

    while index < len(input_arr):
        if not stack or input_arr[stack[-1]] <= input_arr[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = input_arr[top] * (index - stack[-1] - 1 if stack else index)
            max_area = max(max_area, area)
    while stack:
        top = stack.pop()
        area = input_arr[top] * (index - stack[-1] - 1 if stack else index)
        max_area = max(max_area, area)

    return max_area


if __name__ == '__main__':
    stocks = [6, 3, 4, 5, 2]
    list_span = finding_spans(stocks)
    print(list_span)
    list_span1 = finding_span_using_stack(stocks)
    print(list_span1)

    input_arr = [3, 2, 4, 5, 1, 3, 3, ]
    area = max_area(input_arr)
    print(f'area = {area}')

    area = max_area1(input_arr)
    print(f'area = {area}')
