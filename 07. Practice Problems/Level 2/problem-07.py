# lex_auth_01275172167565312069
"""
TODO: Problem Description goes here
"""


# Stack Implementation
class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        return self.__top == self.__max_size - 1

    def is_empty(self):
        return self.__top == -1

    def push(self, data):
        if self.is_full():
            print("The stack is full!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if self.is_empty():
            print("The stack is empty!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if self.is_empty():
            print("The stack is empty!")
        else:
            index = self.__top
            while index >= 0:
                print(self.__elements[index], end='<-')
                index -= 1
        print()

    def get_max_size(self):
        return self.__max_size


def sort_stack(stack1):
    temp = list()
    while not stack1.is_empty():
        temp.append(stack1.pop())
    temp.sort(reverse=True)
    for element in temp:
        stack1.push(element)
    return stack1


if __name__ == '__main__':
    stack = Stack(7)
    stack.push(4)
    stack.push(7)
    stack.push(2)
    stack.push(6)
    stack.push(56)
    stack.push(3)
    stack.push(9)
    result = sort_stack(stack)
    print("The sorted elements are:")
    result.display()
