"""
PROBLEM STATEMENT:
-----------------
Consider a stack (input_stack) containing English words and two '@' symbols.

Write a Python function which takes the above-mentioned stack as input parameter, populates and returns an output_stack,
as per the logic below:
    a)  The processed English words in output_stack would appear in the same order as in input_stack
    b)  Both the '@' symbols have to be replaced with dot (".") and the English words in between two '@' symbols would
        be converted to upper case.

Example:
    - input_stack (top -> bottom): 'stay', 'Happy', '@', 'Infosys', 'in', 'are', 'you', '@', 'WelCome', 'hi'
    - output_stack (top -> bottom): 'stay', 'Happy', '.', 'INFOSYS', 'IN', 'ARE', 'YOU', '.', 'WelCome', 'hi'

Assumption:
    - input_stack will contain only two "@" symbols.
    - input_stack will contain at least two elements.
"""


class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        if self.__top == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__top == -1:
            return True
        return False

    def push(self, data):
        if self.is_full():
            print("The stack is full!!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if self.is_empty():
            print("The stack is empty!!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            index = self.__top
            while index >= 0:
                print(self.__elements[index])
                index -= 1

    def get_max_size(self):
        return self.__max_size

    def __str__(self):
        msg = []
        index = self.__top
        while index >= 0:
            msg.append(str(self.__elements[index]))
            index -= 1
        msg = " ".join(msg)
        msg = "Stack data(Top to Bottom): " + msg
        return msg


def regenerate_stack(input_stack):
    output_stack = Stack(input_stack.get_max_size())
    temp_stack = Stack(input_stack.get_max_size())
    flag = False
    while not input_stack.is_empty():
        element = input_stack.pop()
        if element == '@':
            flag = not flag
            temp_stack.push('.')
        else:
            if flag:
                element = element.upper()
            temp_stack.push(element)
    while not temp_stack.is_empty():
        output_stack.push(temp_stack.pop())
    return output_stack


# Tests
if __name__ == '__main__':
    stack = Stack(10)
    stack.push('stay')
    stack.push('Happy')
    stack.push('@')
    stack.push('infosys')
    stack.push('in')
    stack.push('are')
    stack.push('you')
    stack.push('@')
    stack.push('WelCome')
    stack.push('hi')
    result_stack = regenerate_stack(stack)
    result_stack.display()
