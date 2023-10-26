# lex_auth_01275171830954393670

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


def stack_operation(input_stack):
    temp = list()
    while not input_stack.is_empty():
        temp.append(input_stack.pop())
    if len(temp) > 3:
        for i in range(len(temp) - 4, -1, -1):
            input_stack.push(temp[i])
    input_stack.push(temp[-1])
    input_stack.push(temp[-2])
    input_stack.push(temp[-3])
    return input_stack


if __name__ == '__main__':
    stack = Stack(5)
    stack.push('E')
    stack.push('D')
    stack.push('C')
    stack.push('B')
    stack.push('A')
    print("The elements in input stack are:")
    stack.display()
    print()
    updated_stack = stack_operation(stack)
    print("The elements in the updated stack are:")
    updated_stack.display()
